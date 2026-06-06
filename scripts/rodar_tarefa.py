#!/usr/bin/env python3
"""Roda uma tarefa de acompanhamento do VVV usando o Claude e salva o relatório.

Uso:
    python scripts/rodar_tarefa.py <nome-da-tarefa>

Onde <nome-da-tarefa> é um de:
    vvv-diaria-sentimento-risco
    on-chain-produto-e-dev
    terceiros-upstream
"""
import glob
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

import anthropic

# Qual "cérebro" (modelo de IA) usar. Para trocar, basta mudar esta linha.
MODELO = "claude-opus-4-8"

# Mapa: nome da tarefa -> prefixo do arquivo de relatório que será gerado.
PREFIXOS = {
    "vvv-diaria-sentimento-risco": "VVV-diaria-sentimento-risco",
    "on-chain-produto-e-dev": "VVV-on-chain-produto-e-dev",
    "terceiros-upstream": "VVV-terceiros-upstream",
}


def ler_prompt(arquivo_tarefa):
    """Lê o texto que vem depois de '## Prompt' no arquivo da tarefa."""
    with open(arquivo_tarefa, encoding="utf-8") as f:
        texto = f.read()
    marcador = "## Prompt"
    if marcador not in texto:
        raise SystemExit(f"Não encontrei '## Prompt' em {arquivo_tarefa}")
    return texto.split(marcador, 1)[1].strip()


def ler_relatorio_anterior(prefixo):
    """Encontra o relatório mais recente da mesma categoria (para comparar)."""
    arquivos = sorted(glob.glob(f"{prefixo}-*.md"))
    if not arquivos:
        return None, None
    ultimo = arquivos[-1]
    with open(ultimo, encoding="utf-8") as f:
        return ultimo, f.read()


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Uso: python scripts/rodar_tarefa.py <nome-da-tarefa>")

    tarefa = sys.argv[1]
    if tarefa not in PREFIXOS:
        opcoes = ", ".join(PREFIXOS)
        raise SystemExit(f"Tarefa desconhecida: {tarefa}. Opções: {opcoes}")

    prefixo = PREFIXOS[tarefa]
    prompt_tarefa = ler_prompt(f"{tarefa}.md")
    nome_anterior, conteudo_anterior = ler_relatorio_anterior(prefixo)

    hoje = datetime.now(ZoneInfo("America/Sao_Paulo")).strftime("%Y-%m-%d")

    # Monta a mensagem: o prompt da tarefa + o relatório anterior, se existir.
    mensagem = prompt_tarefa
    if conteudo_anterior:
        mensagem += (
            f"\n\n---\nPara comparação, segue o relatório anterior "
            f"({nome_anterior}):\n\n{conteudo_anterior}"
        )

    # O cliente lê a chave da variável de ambiente ANTHROPIC_API_KEY.
    client = anthropic.Anthropic()

    mensagens = [{"role": "user", "content": mensagem}]
    ferramentas = [{"type": "web_search_20260209", "name": "web_search"}]

    # A busca na web roda no servidor da Anthropic; quando ela faz uma pausa
    # (pause_turn), reenviamos para continuar. O limite evita loop infinito.
    resposta = None
    for _ in range(10):
        resposta = client.messages.create(
            model=MODELO,
            max_tokens=16000,
            tools=ferramentas,
            messages=mensagens,
        )
        if resposta.stop_reason == "pause_turn":
            mensagens.append({"role": "assistant", "content": resposta.content})
            continue
        break

    # Pega só o relatório final: o texto que vem DEPOIS da última busca na web.
    # Assim descartamos a narração de bastidores que fica entre as buscas.
    indice_ultima_ferramenta = -1
    for i, bloco in enumerate(resposta.content):
        if bloco.type != "text":
            indice_ultima_ferramenta = i

    blocos_finais = resposta.content[indice_ultima_ferramenta + 1:]
    texto_final = "".join(b.text for b in blocos_finais if b.type == "text").strip()

    # Segurança: se não sobrou nada, cai de volta para todo o texto.
    if not texto_final:
        texto_final = "".join(
            b.text for b in resposta.content if b.type == "text"
        ).strip()

    nome_saida = f"{prefixo}-{hoje}.md"
    with open(nome_saida, "w", encoding="utf-8") as f:
        f.write(texto_final)

    print(f"Relatório salvo: {nome_saida}")


if __name__ == "__main__":
    main()
