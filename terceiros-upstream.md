# Rotina: terceiros-upstream

> Arquivo para recriar esta rotina no Claude Code.

## Agendamento
- **Frequência:** semanal (segunda-feira)
- **Horário:** 06:06 (manhã)
- **Cron:** `0 6 * * 1`
- **Ativa:** sim

## Descrição
Acompanhar projetos de terceiros relevantes (fornecedores upstream).

## Prompt

Execute a checagem semanal de Terceiros (Upstream) do projeto Acompanhamento VVV. Cubra os fornecedores — modelos: DeepSeek, Qwen (Alibaba), Llama (Meta), Seedance (ByteDance), Flux (Black Forest Labs); infra: provedores de GPU descentralizada e Aerodrome (liquidez). Para cada um, traga: (1) qualquer atualização de roadmap, lançamento de versão ou anúncio com PRAZO DATADO na última semana; (2) mudanças de licença, preço de API ou disponibilidade que afetem a Venice; (3) se a Venice já integrou ou anunciou a novidade; (4) qualquer reação observável de preço/sentimento do VVV ao evento. Ordene o relatório do fornecedor MAIS relevante para o VVV ao MENOS relevante, com 1 linha justificando a ordem. Para cada item: o que mudou + data/prazo + 1 linha de impacto potencial no VVV + sinal de alerta se aplicável. Marque como NÃO CONFIRMADA qualquer ligação evento→preço sem fonte direta.

- Saída esperada: lista rankeada (mais → menos relevante para o VVV), 1–2 páginas.
- Critério de ordenação (relevância para o VVV): peso do fornecedor na stack da Venice + grau de integração + sensibilidade histórica do preço. No momento, o DeepSeek tende ao topo (modelo central roteado pela Venice + narrativa de mercado ativa); ByteDance/Seedance ganha peso pela dependência do Venice Studio; Aerodrome importa pelo risco de liquidez.
- Gatilhos de alerta: lançamento de versão de modelo ou de recurso de agentes por fornecedor central (potencial catalisador de preço); descontinuação ou mudança de licença de um modelo-chave (risco de dependência); reação de preço do VVV atribuída a evento de terceiro sem confirmação (tratar como sentimento).

Salve este relatório como VVV-terceiros-upstream-{data}.md na pasta de trabalho e, antes de começar, leia o relatório mais recente da mesma categoria nessa pasta para fazer a comparação.
