# Rotina: vvv-diaria-sentimento-risco

> Arquivo para recriar esta rotina no Claude Code.

## Agendamento
- **Frequência:** diária
- **Horário:** 06:07 (manhã)
- **Cron:** `0 6 * * *`
- **Ativa:** sim

## Descrição
Checagem diária do projeto Acompanhamento VVV (Venice Token) — preço, sentimento, cobertura asiática, regulatório e contrato.

## Prompt

Execute a checagem diária do projeto "Acompanhamento VVV" (Venice Token, ticker VVV — AI/privacy/uncensored crypto). Use WebSearch e web_fetch. Saída: bloco curto (< 1 página), com bandeira 🔴/🟡/🟢 por item. Para cada item: número + 1 linha de interpretação + sinal de alerta se aplicável. Responda em português (Brasil).

FONTE DE PREÇO OBRIGATÓRIA: verifique o preço primeiro no CoinGecko (https://www.coingecko.com/pt-br/moedas/venice-token) via web_fetch, e confirme em uma 2ª fonte (Kraken, Crypto.com, CoinGlass ou CoinMarketCap). Reporte preço + variação 24h.

ITENS:
1. Preço VVV confirmado em 2 fontes (CoinGecko como âncora) + variação 24h.
2. Sentimento no X e Binance Square — tom predominante e mudança vs. dia anterior.
3. Qualquer cobertura asiática nova (Odaily, PANews, BlockBeats).
4. Qualquer notícia regulatória sobre IA / privacidade / uncensored.
5. Alerta se houver mudança em parâmetros do contrato (checar GoPlus / tokenomics, ex.: emissão/inflação, burn).

GATILHOS DE ALERTA (sinalizar 🔴 se ocorrer): deslistagem ou rumor regulatório; mudança de parâmetro de contrato; sentimento virando abruptamente; divergência de preço > 10% entre fontes.

Inclua seção "Sources:" com links markdown ao final. Comece a resposta com título e a data de hoje.

Salve este relatório como VVV-diaria-sentimento-risco-{data}.md na pasta de trabalho e, antes de começar, leia o relatório mais recente da mesma categoria nessa pasta para fazer a comparação.
