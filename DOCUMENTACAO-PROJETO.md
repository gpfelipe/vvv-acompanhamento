# Documentação do Projeto — Acompanhamento VVV (Venice Token)

> Documento de referência. Última atualização: 06/06/2026.
> Projeto **pausado** no Claude Code — Felipe vai continuar rodando no Cowork.

---

## 1. O que é o projeto

Acompanhamento automático do token **VVV (Venice Token)** da Venice.ai. Tem duas partes:

1. **Tarefas automáticas** que geram relatórios (rodando na nuvem, via GitHub Actions).
2. **Dashboard** (página web) que mostra preço, dados e os relatórios de forma visual.

- **Usuário:** Felipe (não é programador — explicar sempre em português simples).
- **Repositório GitHub:** `gpfelipe/vvv-acompanhamento` (PÚBLICO).
- **Moeda de referência:** somente USD.

---

## 2. Estado atual (o que está pronto)

| Item | Status |
|------|--------|
| Repositório no GitHub criado e público | ✅ Pronto |
| Chave da API guardada como segredo (`ANTHROPIC_API_KEY`) | ✅ Pronto |
| Script que roda as tarefas (`scripts/rodar_tarefa.py`) | ✅ Pronto e testado |
| 3 agendamentos (GitHub Actions) | ✅ Prontos |
| Tarefa diária testada (gera relatório limpo) | ✅ Funcionando |
| Tarefa semanal on-chain testada | ✅ Funcionando |
| Tarefa semanal terceiros | ⚠️ Falhou por falta de créditos (não por erro) |
| Dashboard `index.html` | ✅ Pronto (testado localmente) |
| Publicar dashboard no GitHub Pages | ❌ Pendente |
| Créditos da API | ⚠️ Zerados — precisa recarregar |

---

## 3. Como funciona a automação na nuvem

Fluxo de cada execução:

1. **GitHub Actions** "acorda" no horário agendado (grátis).
2. Roda o script `scripts/rodar_tarefa.py <nome-da-tarefa>` (grátis).
3. O script **chama o Claude (API Anthropic)** com busca na web → **isto consome créditos**.
4. O relatório é salvo como arquivo `.md` no repositório (commit automático, grátis).

**Importante:** o GitHub é só o "despertador" + "arquivo". O custo vem **só** da etapa 3 (a IA escrevendo o relatório). Esta automação roda **sem o computador ligado**.

### Modelo de IA
- Atual: **`claude-opus-4-8`** (o mais caro).
- Definido na linha `MODELO = "..."` em `scripts/rodar_tarefa.py`.
- Para economizar: trocar por `claude-sonnet-4-6` (faz os créditos durarem ~5x mais, qualidade continua ótima). **Decisão pendente de Felipe.**

---

## 4. As 3 tarefas (rotinas)

Os "moldes" de cada tarefa (prompt + horário) estão nos arquivos `.md` na raiz:

| Arquivo do molde | Tarefa | Horário (Brasília) | Cron (UTC) | Agendamento |
|------------------|--------|--------------------|-----------|-------------|
| `vvv-diaria-sentimento-risco.md` | Diária — sentimento e risco | Todo dia 06:07 | `7 9 * * *` | `.github/workflows/diaria.yml` |
| `on-chain-produto-e-dev.md` | Semanal — on-chain, produto, dev | Segundas 06:00 | `0 9 * * 1` | `.github/workflows/semanal-onchain.yml` |
| `terceiros-upstream.md` | Semanal — terceiros (upstream) | Segundas 06:06 | `6 9 * * 1` | `.github/workflows/semanal-terceiros.yml` |

> Horários no GitHub usam UTC. Brasília = UTC − 3h.

### Conteúdo atual da tarefa DIÁRIA (após edições de Felipe)
Foca em 4 itens (com bandeira 🔴/🟡/🟢 cada):
1. Sentimento (X / Binance Square)
2. Cobertura asiática (Odaily, PANews, BlockBeats)
3. Regulação (IA / privacidade / uncensored)
4. Contrato / tokenomics (emissão, inflação, burn)

**Removidos por decisão de Felipe:** Preço, Derivativos/liquidações e a "fonte de preço obrigatória".
Gatilhos de alerta 🔴: deslistagem/rumor regulatório; mudança de contrato; sentimento virando abruptamente.

### Os relatórios gerados
Salvos na raiz do repositório com o nome:
- `VVV-diaria-sentimento-risco-AAAA-MM-DD.md`
- `VVV-on-chain-produto-e-dev-AAAA-MM-DD.md`
- `VVV-terceiros-upstream-AAAA-MM-DD.md`

Antes de escrever, cada tarefa lê o relatório anterior da mesma categoria para comparar.

---

## 5. O dashboard (`index.html`)

Página única, visual escuro, responsiva (celular e PC). Tem **3 abas**:

1. **Visão diária:**
   - Painel "Status do dia": bandeira geral (🟢🟡🔴) + resumo + lista detalhada de cada item do relatório diário (com setinhas ▲▼, valores em destaque, bullish/bearish coloridos).
   - "Mercado agora": preço, variação 24h, market cap, volume (ao vivo da CoinGecko).
   - Tabela "Histórico de 7 dias".
   - "Dados do protocolo": supply circulante/total/máximo (CoinGecko) + emissão programada.
2. **On-chain, produto & dev:** mostra o último relatório semanal on-chain, renderizado.
3. **Terceiros (upstream):** mostra o último relatório semanal de terceiros, renderizado.

### Fontes de dados do dashboard
- **Preço/market cap/volume/supply/histórico:** CoinGecko (API pública, sem chave). ID da moeda: `venice-token`.
- **Status e relatórios:** lidos direto do GitHub (API pública de conteúdo do repositório).

### Decisões de layout (já aprovadas por Felipe)
- Setinhas ▲ verde (alta) / ▼ vermelho (baixa).
- Números alinhados (tabulados).
- Status estruturado em tópicos, com faixa colorida por item.
- **Gráficos de preço foram REMOVIDOS** (a pedido de Felipe). Mantida a tabela de 7 dias.

---

## 6. Créditos da API (entender bem)

- São **pré-pagos e por utilização** — funcionam como um "tanque de combustível".
- **Não renovam sozinhos** todo mês. Quando acabam, as tarefas param.
- Recarregar em: [console.anthropic.com](https://console.anthropic.com) → **Plans & Billing** → **Add credits**.
- Dá para ligar **Auto-reload** (recarrega sozinho quando o saldo fica baixo).
- Consumo depende de: quantas vezes as tarefas rodam + qual modelo (Opus gasta mais; Sonnet menos).
- **Plano Claude Pro NÃO cobre a API** — são coisas separadas.

---

## 7. Como rodar uma tarefa manualmente (sem esperar o horário)

1. Abrir [github.com/gpfelipe/vvv-acompanhamento/actions](https://github.com/gpfelipe/vvv-acompanhamento/actions)
2. Clicar na tarefa desejada (lista à esquerda)
3. Botão **Run workflow** → botão verde **Run workflow**
4. Aguardar ~2–4 min. Verde = sucesso; vermelho = erro (ver o log).

---

## 8. Pendências / próximos passos

1. **Recarregar créditos** da API (estão zerados).
2. **Decidir o modelo:** manter Opus 4.8 ou trocar para Sonnet 4.6 (economia). Recomendação dada: Sonnet + auto-reload.
3. **Rodar a tarefa de terceiros** de novo (falhou só por falta de saldo) para popular a 3ª aba.
4. **Publicar o dashboard no GitHub Pages** (deixar acessível por link de qualquer lugar):
   - Settings → Pages → Source: branch `main`, pasta `/root` → Save.
   - URL ficará: `https://gpfelipe.github.io/vvv-acompanhamento/`

---

## 9. Histórico de testes (06/06/2026)

- 3 execuções da tarefa diária (testando o formato de saída) — sucesso.
- 1 execução semanal on-chain — sucesso.
- 1 execução semanal terceiros — falhou (saldo de créditos zerado, erro 400 "credit balance too low").

---

## 10. Arquivos importantes no repositório

```
vvv-acompanhamento/
├── index.html                       ← o dashboard
├── scripts/rodar_tarefa.py          ← script que chama a IA e salva o relatório
├── requirements.txt                 ← dependência (biblioteca anthropic)
├── .github/workflows/
│   ├── diaria.yml                    ← agendamento diário
│   ├── semanal-onchain.yml          ← agendamento semanal (on-chain)
│   └── semanal-terceiros.yml        ← agendamento semanal (terceiros)
├── vvv-diaria-sentimento-risco.md   ← molde da tarefa diária
├── on-chain-produto-e-dev.md        ← molde da tarefa on-chain
├── terceiros-upstream.md            ← molde da tarefa terceiros
├── VVV-*-AAAA-MM-DD.md              ← relatórios gerados
├── CLAUDE.md                         ← guia do projeto para o Claude
└── DOCUMENTACAO-PROJETO.md          ← este documento
```

---

## 11. Observação sobre o Cowork

Felipe vai continuar rodando o projeto no **Cowork**. As 3 rotinas originais já existiam lá (mesmos prompts dos arquivos `.md` deste repositório). A automação por GitHub Actions descrita aqui é uma alternativa que roda na nuvem sem o PC ligado — pode ser mantida, pausada ou retomada quando quiser.
