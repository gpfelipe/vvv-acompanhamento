# Projeto: Acompanhamento VVV (Venice Token)

Este arquivo orienta o Claude Code que trabalha nesta pasta. Leia-o no início de cada sessão.

## Quem é o usuário

- Felipe — **não é programador**. Explique tudo em **português, de forma simples**, sem jargão técnico.
- **Sempre peça aprovação antes de criar ou alterar arquivos** (modo "perguntar antes de editar"). Mostre o que vai mudar e por quê.
- Avance **um passo de cada vez** e confirme com ele antes de seguir. Ensine enquanto faz: ele quer aprender a usar o Claude Code.

## O que é o projeto

Acompanhamento do token **VVV (Venice Token)**, da Venice.ai. A pasta guarda relatórios gerados por três rotinas automáticas:

1. `vvv-diaria-sentimento-risco` — diária: preço, sentimento, cobertura asiática, regulatório e contrato.
2. `on-chain-produto-e-dev` — semanal (segundas): on-chain, produto e desenvolvimento.
3. `terceiros-upstream` — semanal (segundas): projetos de terceiros relevantes.

Os arquivos `VVV-*.md` e `VVV-*.html` são os relatórios já produzidos. **Não apague nem reescreva relatórios antigos** sem pedir.

## Objetivo atual

Dois objetivos, nesta ordem:

1. **Construir um dashboard web** (página HTML) que mostre o preço e os dados do protocolo do VVV. Começar localmente, nesta pasta.
2. Depois, **migrar o projeto para a nuvem** para rodar sozinho todo dia, sem o computador ligado.

## Especificação do dashboard (acordada com Felipe)

- Moeda: **somente USD**.
- **Topo — painel de status**: "bandeira do dia" (verde/amarelo/vermelho) + resumo curto do último relatório diário (`VVV-diaria-sentimento-risco-AAAA-MM-DD.md`).
- **Cabeçalho de métricas**: preço atual, variação 24h (verde = subiu / vermelho = caiu), market cap, volume 24h.
- **Gráfico de preço** com seletor de período (botões 7d / 30d / 1 ano + intervalo por datas) e área preenchida abaixo da linha.
- **Gráfico dos últimos 7 dias** (linha verde se subiu, vermelha se caiu).
- **Tabela histórica de 7 dias**: data, preço de fechamento, variação do dia, volume.
- **Painel "dados do protocolo"**: supply circulante, % queimado acumulado, emissão programada (4M → 3M VVV/ano em jul/2026), holders na Base, APR de staking, % em staking (marcar "não divulgado"), ARR da Venice, buyback & burn.
- Estilo: limpo, fundo escuro opcional, sem exageros. Funciona em celular e computador.

## Fontes de dados (ao vivo, gratuitas)

- **Preço / market cap / volume / histórico**: CoinGecko Demo API (grátis, sem chave, sem cadastro). ID da moeda: `venice-token`.
  - Preço atual: `https://api.coingecko.com/api/v3/simple/price?ids=venice-token&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true`
  - Histórico: `https://api.coingecko.com/api/v3/coins/venice-token/market_chart?vs_currency=usd&days=365`
  - Limites do plano grátis: ~100 chamadas/min, 10.000/mês. Guardar os dados baixados em arquivo para não estourar o limite.
- **Dados on-chain (rede Base, chain id 8453)**: holders, supply, staking. Contrato de staking sVVV: `0x321b7ff7...116f340ff` (confirmar endereço completo antes de usar).
- **Status + resumo**: extrair do relatório diário mais recente nesta pasta.

## Plano de migração para a nuvem (fase 2)

- **GitHub**: repositório que guarda o projeto e hospeda o dashboard (GitHub Pages).
- **GitHub Actions (cron)**: "despertador" que roda os scripts todo dia sem o PC ligado.
- **Análise de IA na nuvem**: usará uma **chave da API Anthropic** (a configurar como segredo no GitHub) — só nesta fase.
- Felipe criará a conta do GitHub e a chave quando chegarmos aqui; guie clique a clique.

## Roteiro (faça em ordem, confirmando cada passo)

1. Ler esta pasta e confirmar o entendimento com Felipe.
2. Criar um script simples que baixa o preço e o histórico do VVV da CoinGecko e salva em um arquivo (ex.: `dados/vvv.json`).
3. Criar o dashboard `index.html` lendo esses dados, com todas as seções da especificação acima.
4. Abrir o dashboard no navegador e ajustar com o Felipe.
5. (Fase 2) Publicar no GitHub + agendar no GitHub Actions + publicar no GitHub Pages.

## Estilo de trabalho

- Português simples, sempre.
- Peça aprovação antes de editar.
- Um passo de cada vez.
- Explique o "porquê" de cada coisa, como se ensinasse alguém que nunca programou.
