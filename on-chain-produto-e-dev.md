# Rotina: on-chain-produto-e-dev

> Arquivo para recriar esta rotina no Claude Code.

## Agendamento
- **Frequência:** semanal (segunda-feira)
- **Horário:** 06:00 (manhã)
- **Cron:** `0 6 * * 1`
- **Ativa:** sim

## Descrição
Mapeamento On-chain, produto e Desenvolvimento.

## Prompt

Execute a checagem semanal do projeto Acompanhamento VVV. Traga, comparando com a semana anterior: (1) on-chain — supply circulante/queimado, VVV em staking, DIEM cunhado, concentração de holders top-10; (2) produto — qualquer atualização de ARR/usuários/visitas, novos tiers ou recordes; (3) dev — commits e issues nos repos oficiais, novos lançamentos no changelog, qualquer auditoria publicada; (4) posição vs. pares (TAO, FET, NEAR, Akash) em market cap. Para cada bloco: números + 1–2 linhas de interpretação + sinais de alerta.

- Saída esperada: 1–2 páginas, tabela de variação semanal + comentário.
- Gatilhos de alerta: queda de VVV em staking (perda de convicção); auditoria de privacidade publicada (positivo); estagnação de commits por > 3 semanas; perda relevante de share vs. pares.

Salve este relatório como VVV-on-chain-produto-e-dev-{data}.md na pasta de trabalho e, antes de começar, leia o relatório mais recente da mesma categoria nessa pasta para fazer a comparação.
