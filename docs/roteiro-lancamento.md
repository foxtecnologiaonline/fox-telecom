# Roteiro de Lançamento — FOX Telecom

> Fases de evolução: começar com a estrutura mínima para uso próprio (autoconsumo/validação), avançar para clientes externos, e só então mirar licitações públicas — que exigem um patamar de formalização e, possivelmente, enquadramento regulatório diferente do modelo de revenda puro. Complementa `docs/parcerias-revenda-numeros.md` (parceiros) e sua seção 6 (custo/break-even).

## Visão geral das fases

| Fase | Objetivo | Gatilho para avançar | Duração estimada |
|---|---|---|---|
| 0 — Autoconsumo | Validar tecnicamente o serviço usando a própria FOX como primeiro "cliente" | Operação testada (chamada, portabilidade, cobrança) funcionando sem erro | 2–4 semanas |
| 1 — Primeiros clientes externos | Vender para PMEs via indicação/venda direta, modelo enxuto já dimensionado | Base ativa estável + ARPU/margem reais confirmados | 3–6 meses |
| 2 — Formalização plena | Virar "empresa licitável": certidões, CNAE, capital social, atestados técnicos | Documentação 100% pronta + 1º atestado técnico emitido | 3–6 meses (em paralelo à fase 1) |
| 3 — Licitações de pequeno/médio porte | Disputar pregões municipais/estaduais compatíveis com o modelo de revenda | 1ª licitação vencida ou habilitada | 6–12 meses após fase 2 |
| 4 — Outorga própria / MVNO formal | Destravar licitações que exigem execução direta via STFC/SMP | Volume e caixa suficientes para sustentar outorga | 18–24+ meses |

---

## Fase 0 — Estrutura para me fornecer (autoconsumo/validação)

Objetivo: montar o mínimo possível para operar o serviço "para si mesmo" antes de vender para terceiros — validar tecnicamente, não comercialmente.

**Montar:**
- CNPJ simples (MEI ou ME) — suficiente nesta fase, sem necessidade de LTDA ainda.
- Conta self-service em 1 fornecedor CPaaS sem contrato mínimo (Telnyx ou Plivo, conforme seção 3.1 do doc de parcerias).
- 1–3 números ativados (DID/0800) usados internamente — testar qualidade de chamada, portabilidade, billing, e a experiência completa fim a fim.
- Conta de cobrança recorrente básica (gateway Pix/boleto) configurada, mesmo que ainda sem clientes pagantes.

**Custo:** fração do CAPEX já estimado (seção 6.1 do doc de parcerias) — nesta fase, foco é só CNPJ + conta no fornecedor, ~R$500–2.000.

**Critério de saída:** o serviço funciona de ponta a ponta sob seu próprio uso, sem surpresas técnicas ou de custo.

## Fase 1 — Primeiros clientes externos

Já coberta em detalhe no documento de parcerias (estrutura enxuta, precificação, break-even). Aqui o objetivo adicional é começar a **gerar os registros que vão virar atestado técnico depois**: guardar contratos assinados, notas fiscais emitidas, prints/relatórios de SLA — mesmo sendo poucos clientes, isso é o que comprova capacidade técnica na Fase 3.

**Critério de saída:** base ativa estável (ver break-even na seção 6.4), e pelo menos um cliente disposto a emitir um atestado/declaração de prestação de serviço.

## Fase 2 — Formalização plena (pré-requisito para licitar)

Esta fase roda em paralelo à Fase 1, mas precisa estar 100% concluída antes de participar de qualquer pregão.

**Jurídico/societário:**
- Migrar de MEI/ME para LTDA se ainda não for (a maioria dos editais exige capital social mínimo, o que MEI não sustenta).
- CNAE compatível com o objeto que será licitado (ex.: 61.90-6/99 "outras atividades de telecomunicações", 61.10-8 se envolver STFC/SCM próprio).
- Capital social integralizado compatível com os valores dos certames-alvo (regra comum: ≥10% do valor estimado do contrato, exigida via qualificação econômico-financeira, art. 69 da Lei 14.133/2021).

**Fiscal/trabalhista (certidões negativas, renovadas periodicamente):**
- Receita Federal/PGFN (débitos federais)
- FGTS (CRF)
- Trabalhista (CNDT)
- Estadual e Municipal (do domicílio da empresa)

**Cadastros:**
- SICAF, se for mirar licitações federais (Sistema de Cadastro de Fornecedores).
- Cadastro de fornecedores de cada prefeitura/estado-alvo, conforme exigido no edital.
- Acompanhamento ativo do **PNCP** (Portal Nacional de Contratações Públicas) — hoje concentra a publicação de editais de todos os entes federativos.

**Capacidade técnica:**
- Consolidar o(s) atestado(s) de capacidade técnica da Fase 1 (editais normalmente aceitam somar atestados de objeto equivalente, mas não de objetos diferentes — ex.: "telefonia" não se mistura com "câmeras IP" ou "Wi-Fi").
- Formalizar com o parceiro CPaaS/operadora (Zenvia, Algar, etc.) uma carta de respaldo técnico ou atestado conjunto, se o parceiro topar — fortalece a habilitação técnica enquanto a FOX ainda não tem outorga própria.

**Critério de saída:** checklist completo (ver seção "Checklist de prontidão" abaixo) + pelo menos 1 atestado técnico válido.

## Fase 3 — Licitações de pequeno/médio porte

> **Atenção regulatória — ponto crítico encontrado na pesquisa:** editais de telefonia para órgãos públicos costumam exigir que o **próprio licitante execute o serviço via outorga STFC/SMP**, e limitam a subcontratação a partes acessórias (ex.: um termo de referência de 2026 de Porto Alegre permite subcontratar apenas "assistência técnica" e "longa distância nacional/internacional", mantendo a contratada como intermediária — não permite subcontratar o serviço-fim de telefonia em si, com base no art. 122 da Lei 14.133/2021 e no Acórdão 963/2024 do TCU). Isso significa que **nem todo edital de telefonia vai aceitar o modelo de revenda puro da FOX** — é preciso ler cada edital com atenção a essa cláusula antes de disputar.

**Estratégia recomendada:**
1. Priorizar editais de **objetos compatíveis com revenda/intermediação** — ex.: fornecimento de números virtuais, URA, central telefônica em nuvem, SVA (serviço de valor adicionado) — que não exigem execução direta via STFC/SMP.
2. Evitar, nesta fase, editais que peçam explicitamente "prestação direta de STFC/SMP" ou linha dedicada/tronco — esses tendem a barrar quem não tem outorga própria.
3. Começar por municípios menores e certames de menor valor (menos concorrência, habilitação mais simples) para construir histórico de atestados antes de disputar contratos grandes.
4. Avaliar participação via consórcio com uma operadora licenciada (alguns editais permitem, com acréscimo de até 20% na exigência de qualificação técnica) — pode ser o caminho mais rápido para disputar editais "fechados" para STFC/SMP.
5. Monitorar o PNCP com filtros por CNAE/objeto (telefonia, URA, central telefônica, SVA) nos entes-alvo.

**Critério de saída:** primeira licitação vencida ou pelo menos habilitada tecnicamente (mesmo que não vencida).

## Fase 4 — Outorga própria ou MVNO formal (escala)

Quando o volume e o caixa sustentarem, buscar outorga SCM própria e/ou acordo formal de MVNO com uma SMP (Vivo/Claro/TIM/Algar) — como já mapeado no documento de parcerias (seção 3.3). Isso remove a limitação da Fase 3 e abre o leque de licitações que hoje exigem execução direta via STFC/SMP, além de melhorar a margem (sem a camada de revenda de terceiros).

---

## Checklist de prontidão para licitar (resumo rápido)

- [ ] LTDA constituída, CNAE compatível com o objeto-alvo
- [ ] Capital social integralizado compatível com o valor dos certames-alvo
- [ ] Certidões negativas em dia (Federal/PGFN, FGTS, Trabalhista, Estadual, Municipal)
- [ ] Cadastro no SICAF (federal) e nos cadastros de fornecedores dos entes-alvo
- [ ] Pelo menos 1 atestado de capacidade técnica compatível com o objeto (telefonia/URA/SVA — não misturar com objetos diferentes)
- [ ] Parceria formal com operadora licenciada, com possibilidade de carta de respaldo técnico ou consórcio
- [ ] Leitura do edital confirmando se aceita intermediação/revenda ou exige execução direta via STFC/SMP
- [ ] Capacidade de prestar garantia de proposta/contrato, se exigida

## Fontes

- [TR Porto Alegre PE 2026.147 — subcontratação em telefonia](https://prefeitura.poa.br/sites/default/files/usu_doc/hotsites/pgm/diretoria-de-licitacoes-e-contratos/CCRP_PE_2026.147_TR.pdf)
- [TRE-RN — análise de qualificação técnica, soma de atestados](https://www.tre-rn.jus.br/transparencia-e-prestacao-de-contas/licitacoes-contratos-e-instrumentos-de-cooperacao-1/licitacoes-1/pregoes-eletronicos_15-05-2020/arquivos-nl-15-05-2020/analise-qualificacao-tecnica-pe-60-2020)
- [Edital padrão Bahia — habilitação ME/EPP, Lei 14.133/LC 123](https://www.ba.gov.br/car/sites/site-car/files/2026-05/PE182026.pdf)
- [TRT14 — edital, soma de atestados por objeto equivalente](https://portal.trt14.jus.br/portal/sites/default/files/editais-licitacoes/2023-12/17314_2.pdf)
- Ver também as fontes regulatórias já listadas em `docs/parcerias-revenda-numeros.md` (Resolução Anatel 769/2024 e 749/2022).
