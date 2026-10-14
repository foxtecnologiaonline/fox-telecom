# Mapa Estratégico — Tornar-se uma "Nova Telnyx" no Brasil

> Mapa de longo prazo: o que precisa ser construído, em paralelo, para a FOX Telecom deixar de ser uma revenda sobre CPaaS de terceiros e se tornar uma operadora full-stack nos mesmos moldes da Telnyx — rede própria + plataforma de software própria + catálogo de produto amplo + self-service + compliance de nível carrier. Este documento **não substitui** `docs/roteiro-lancamento.md` (fases de negócio 0–4) nem `docs/escopo-plataforma-fox-telecom.md` (catálogo de produto) — ele os conecta em um mapa único, de execução multi-eixo, e estende o horizonte além da Fase 4.

## 0. O que "ser a Telnyx" realmente significa (e o que isso NÃO é)

A Telnyx não nasceu full-stack. Foi fundada em 2009, operou mais de uma década como CPaaS sobre rede alugada/parceira, e só nos últimos anos consolidou: outorga própria (CLEC nos EUA), rede e PoPs próprios, núcleo móvel próprio, e — mais recentemente — GPUs próprias para IA. **Isso foi construído com centenas de milhões de dólares de capital e a maior parte de 15 anos.**

Logo, o objetivo realista não é "virar a Telnyx em 1–2 anos", e sim:

1. Seguir a mesma **lógica de produto e de plataforma** (API-first, self-service, pay-as-you-go, portal completo, catálogo amplo) **desde já**, mesmo operando sobre rede de terceiros — isso é 100% possível a curto prazo e é puramente execução de software.
2. Avançar na **internalização de rede e outorga** de forma gradual e financiada por caixa real gerado pela operação (não especulativamente) — isso é um horizonte de 3–10 anos, dependente de tração comercial.
3. Tratar a camada de **IA/infraestrutura de borda** (onde a Telnyx está investindo agora) como uma aposta de longuíssimo prazo, não como pré-requisito.

Este mapa está organizado em **7 eixos que evoluem em paralelo** (seção 1) e **6 fases de maturidade** (seção 2, que estende as Fases 0–4 já definidas em `roteiro-lancamento.md` com uma Fase 5 e 6 de paridade plena com a Telnyx).

---

## 1. Os 7 eixos que precisam evoluir em paralelo

Virar uma "nova Telnyx" não é uma fila de tarefas — é 7 trilhas correndo ao mesmo tempo, cada uma no seu próprio ritmo. Atrasar uma trava as outras (ex.: não dá para vender para governo sem o eixo B regulatório pronto, mesmo que o eixo D de produto já esteja ótimo).

### Eixo A — Regulatório / Outorga (ANATEL)
O que legitima a empresa a operar telecom por conta própria, não como revenda.

- **Hoje (confirmado via Resolução 769/2024 e 749/2022, já documentado em `parcerias-revenda-numeros.md`):** sem outorga, a FOX só existe dentro do guarda-chuva de uma operadora parceira.
- **Atenção a um movimento recente da ANATEL:** a agência endureceu a fiscalização de provedores sem outorga em 2025 — prazo final de regularização via sistema **Mosaico** foi 29/out/2025, e quem não regularizou passou a ser tratado como operação clandestina, inclusive com corte de fornecimento de link por fornecedores no atacado. Isso confirma que **não ter outorga registrada corretamente deixou de ser uma zona cinzenta tolerada** — é um risco operacional real a monitorar desde já, mesmo na Fase 1 de revenda.
- **Trajetória de outorga:** SCM (dados/multimídia) é a mais acessível; STFC e SMP (telefonia fixa/móvel "de verdade") têm barreira maior. MVNO formal com uma SMP (Vivo/Claro/TIM/Algar) é o caminho mais rápido para voz móvel própria sem licitar espectro.
- **Novo item regulatório a monitorar: "Origem Verificada" (o STIR/SHAKEN brasileiro).** A ANATEL tornou obrigatória a adoção de autenticação de identidade de chamada (Ato nº 10.413, rollout iniciado em jan/2024, prazo de até 3 anos para as operadoras implementarem, operacionalizado pela ABR Telecom). **Qualquer operadora própria que a FOX vier a ser vai precisar implementar isso** — é o equivalente exato ao "STIR/SHAKEN nível A" que a Telnyx já anuncia como certificação (ver `escopo-plataforma-fox-telecom.md`, seção 4).

### Eixo B — Rede e Infraestrutura
O que hoje é 100% terceirizado (Telnyx/Plivo/Zenvia) e precisaria, no limite, ser próprio.

- **Camada 1 (atual):** nenhuma rede própria — tudo via API de fornecedor.
- **Camada 2 (intermediária, com outorga SCM):** softswitch/SBC próprio (ex.: Kamailio na frente de uma farm FreeSWITCH, ou um SBC comercial) rodando em nuvem/colocation, ainda dependente de troncos SIP de operadoras parceiras para originar/terminar chamadas — FOX já controla o roteamento e a lógica, mas não a "última milha".
- **Camada 3 (rede própria real):** interconexão direta com outras operadoras via **PTT.br** (Ponto de Troca de Tráfego, para peering IP) e acordos de interconexão de voz (CIDs/inteligência de rede) regulados pela ANATEL — isso remove a dependência de um único fornecedor por completo.
- **Camada 4 (paridade com Telnyx):** múltiplos pontos de presença (PoPs) redundantes, núcleo móvel próprio (se for a via MVNO/SMP), link direto com data centers/nuvens (equivalente ao "Virtual Cross Connect" da Telnyx).

### Eixo C — Plataforma de Software
Isto é o que **pode e deve começar a ser construído já, na Fase 1**, independente do eixo B. É também o eixo onde a FOX ganha mais vantagem competitiva rápida, porque nenhum fornecedor terceiro resolve isso pronto para o mercado brasileiro.

- API REST própria (camada FOX por cima da API do fornecedor atual) — abstrai o fornecedor de baixo, permite trocar de Telnyx para outro sem quebrar o cliente.
- Portal self-service do cliente (equivalente ao Mission Control, mas em português e com Pix/boleto nativo).
- Motor de billing/rating (CDR → tarifação → fatura) — ponto que a Telnyx não resolve para o Brasil e que é a maior lacuna de valor a capturar.
- Backoffice interno (provisionamento, suporte, antifraude, auditoria).
- Documentação de API pública + webhooks assinados, nos mesmos moldes do OpenAPI da Telnyx.
- Sub-contas / managed accounts (multi-tenant) — necessário a partir do momento em que a FOX quiser ter revendedores próprios.

### Eixo D — Catálogo de Produto
Replicar, na ordem certa, o catálogo já mapeado em `escopo-plataforma-fox-telecom.md`, seção 2 e 6. Resumo da ordem de prioridade:

1. Número virtual + encaminhamento + URA simples (já em andamento).
2. WhatsApp Business API + Verify/OTP (alta demanda, baixo custo de implementação).
3. Portal + billing nativo + Branded Calling/antifraude.
4. SIP Trunking/Elastic SIP Trunking com rede própria + Wireless/IoT (depende do Eixo B avançar).
5. Camada de IA (voicebot, TTS/STT em PT-BR) como diferenciação, não fundação.

### Eixo E — Segurança, Compliance e Certificações
O que dá credibilidade de "nível carrier" perante clientes enterprise e licitações públicas.

- Curto prazo: política de segurança básica, LGPD (equivalente brasileiro ao GDPR que a Telnyx certifica), contrato de processamento de dados com clientes.
- Médio prazo: ISO/IEC 27001 (mesma certificação que a Telnyx tem) — já citada como objetivo em `roteiro-lancamento.md`, Fase 2/3, por ser exigida/valorizada em licitações.
- Médio/longo prazo: SOC 2 (se a FOX for vender para clientes enterprise que exigem relatório de auditoria), PCI DSS (se processar cartão diretamente em vez de delegar a um gateway).
- Obrigatório assim que tiver rede própria: "Origem Verificada" (Eixo A) e qualquer regra ANATEL de antifraude de SMS que vier a ser regulamentada.

### Eixo F — Comercial / GTM (Go-to-Market)
- Hoje: venda direta/indicação para PME (Fase 1 do roteiro).
- Self-service completo (sign-up sem tocar em humano, como a Telnyx) é uma meta de produto, não só de vendas — depende do Eixo C.
- Modelo de 3 camadas comerciais, no estilo Telnyx (ver `escopo-plataforma-fox-telecom.md`, seção 3): varejo self-service sem mínimo → contrato com volume mínimo e desconto → enterprise com SLA e conta dedicada. Vale adotar essa estrutura de precificação desde já, mesmo revendendo.
- Revenda/white-label para terceiros (parceiros regionais) como camada de crescimento — usa o mesmo mecanismo de sub-contas do Eixo C.

### Eixo G — Time e Capital
O eixo que decide a velocidade de todos os outros.

- **Fase 1 (atual):** fundador(a) + freelancers pontuais — já dimensionado em `parcerias-revenda-numeros.md`, seção 6.
- **Fase 2–3 (plataforma própria):** 1–2 desenvolvedores backend (API/billing/portal), part-time ou PJ.
- **Fase 4–5 (outorga + rede própria):** advogado(a) especializado em telecom (recorrente, não só pontual), engenheiro(a) de rede/VoIP (Kamailio/FreeSWITCH/SBC), pessoa de compliance/regulatório dedicada.
- **Fase 6 (paridade Telnyx):** time de NOC 24/7, engenharia de infraestrutura distribuída, segurança da informação dedicada — isso já é "empresa de telecom de verdade", na escala de centenas de milhares a milhões de reais de operação mensal.
- Capital: cada salto de camada no Eixo B (softswitch próprio → interconexão PTT.br → PoPs redundantes → núcleo móvel) multiplica o CAPEX necessário por uma ordem de grandeza. Não avançar o Eixo B sem o Eixo F (receita real) sustentar o salto.

---

## 2. Linha do tempo de maturidade (estende `roteiro-lancamento.md`)

| Fase | Nome | Granularidade (eixos que avançam) | Duração estimada |
|---|---|---|---|
| 0 | Autoconsumo (✅ já documentada) | A (observar), C (nenhuma ainda) | 2–4 semanas |
| 1 | Primeiros clientes externos (✅ já documentada) | D (produto básico), F (venda direta) | 3–6 meses |
| 2 | Formalização plena (✅ já documentada) | A (certidões/CNAE), E (início) | 3–6 meses, paralelo à Fase 1 |
| 3 | Licitações pequeno/médio porte (✅ já documentada) | A, E (ISO 27001 como objetivo) | 6–12 meses após Fase 2 |
| 4 | Outorga própria / MVNO (✅ já documentada) | A (outorga/MVNO), B (camada 2) | 18–24+ meses |
| **5** | **Plataforma própria completa (novo)** | C (API, portal, billing, sub-contas) + D (catálogo amplo) rodando sobre a rede híbrida da Fase 4 | 12–24 meses, pode começar em paralelo à Fase 3 |
| **6** | **Paridade de rede e certificação carrier (novo)** | B (camada 3–4: PTT.br, PoPs redundantes, núcleo móvel), E (SOC2/PCI se necessário), G (time NOC 24/7) | 3–7 anos, dependente de caixa gerado |

> **Leitura crítica:** a Fase 5 (plataforma de software) **não depende** da Fase 4 estar completa — é o eixo que a FOX pode e deve adiantar enquanto ainda opera sobre o fornecedor atual, porque é onde a diferenciação de produto acontece mais rápido e mais barato. A Fase 6 (rede própria em paridade total) é o verdadeiro "virar a Telnyx" e é de longe o salto mais caro e mais lento — só deve ser perseguido quando a Fase 3/4 já estiverem gerando caixa suficiente para sustentar o investimento sem comprometer a operação.

---

## 3. Decisões críticas de arquitetura (a resolver antes de comprometer capital)

| Decisão | Opção enxuta | Opção carrier-grade | Quando decidir |
|---|---|---|---|
| Softswitch/SBC | Nenhum (delega 100% ao fornecedor) | Kamailio + FreeSWITCH (open source) ou SBC comercial | Só na Fase 4+, quando outorga SCM estiver ativa |
| Outorga | Nenhuma (revenda) | SCM própria → depois MVNO com SMP → eventualmente STFC/SMP própria | Fase 4, decisão de negócio, não técnica |
| Billing/rating | Planilha/SaaS de cobrança (Pix/boleto) | Motor de rating próprio (CDR → tarifa → fatura) integrado ao backoffice | Fase 2–3, é o item de maior ROI de construir cedo |
| Interconexão | Nenhuma (sem rede própria) | Peering via PTT.br + acordos de interconexão de voz regulados | Fase 6, só com rede própria funcionando |
| Antifraude de identidade de chamada | Nenhuma (delega ao fornecedor) | Implementação de "Origem Verificada" (ANATEL/ABR Telecom) | Obrigatório a partir do momento em que operar rede própria (Fase 4+), prazo regulatório de até 3 anos desde jan/2024 |
| Certificação de segurança | Política interna básica + LGPD | ISO 27001 → SOC 2 (se enterprise exigir) | ISO 27001 na Fase 3 (já é objetivo do roteiro); SOC2/PCI só se o cliente-alvo exigir |

---

## 4. Riscos principais do caminho

1. **Regulatório:** operar além do que a outorga/parceria permite (ex.: um edital que exige execução direta via STFC/SMP) — já mapeado em `roteiro-lancamento.md`, Fase 3. Agora reforçado pelo endurecimento de 2025 da ANATEL contra operação sem outorga registrada.
2. **Capital mal sequenciado:** investir em rede própria (Eixo B, camada 3–4) antes de ter receita recorrente que sustente — é o erro clássico de "virar operadora" sem ser operadora financeiramente ainda.
3. **Dependência de fornecedor único:** sem a camada de abstração do Eixo C (API própria por cima do fornecedor), trocar de Telnyx para outro parceiro no futuro vira reescrita de produto, não só troca de conta.
4. **Compliance desatualizado:** regras como "Origem Verificada" têm prazo regulatório correndo (3 anos desde jan/2024) — se a FOX avançar para rede própria depois desse prazo sem ter isso pronto, nasce em não-conformidade.
5. **Subestimar o horizonte de tempo:** tratar "ser a nova Telnyx" como meta de curto prazo gera decisões de capital erradas. O benchmark real (a própria Telnyx) levou a maior parte de uma década só para consolidar rede própria, e mais de 15 anos para chegar à posição atual.

---

## 5. Próximos passos imediatos (não bloqueantes, começam já)

- [ ] Confirmar que o CNPJ/operação atual da FOX está fora de qualquer exigência de registro no Mosaico (se em algum momento operar como SCM de fato, não só como cliente de CPaaS) — risco regulatório novo identificado nesta pesquisa.
- [ ] Começar o desenho da API própria da FOX (Eixo C) por cima da API da Telnyx — mesmo que hoje só repasse chamadas, já cria a camada de abstração que paga dividendos em todas as fases seguintes.
- [ ] Priorizar o motor de billing/rating nativo (Pix/boleto) como primeiro grande investimento de engenharia — é o maior gap de valor não resolvido por nenhum fornecedor CPaaS.
- [ ] Mapear o prazo e custo real de uma outorga SCM junto a um advogado de telecom (ação já recomendada em `roteiro-lancamento.md`, mas agora com urgência adicional dado o endurecimento da fiscalização ANATEL em 2025).
- [ ] Acompanhar a implementação de "Origem Verificada" pela ABR Telecom como item de roadmap de compliance de médio prazo, não como surpresa futura.

---

## 6. Fontes

- [Convergência Digital — Acórdão nº 176/2025, fim da isenção de outorga](https://convergenciadigital.com.br/?p=43598)
- [Convergência Digital — Anatel recusa prorrogação do prazo](https://convergenciadigital.com.br/?p=46205)
- [Teletime — Provedores sem outorga Anatel tratados como clandestinos](https://teletime.com.br/28/10/2025/provedores-sem-outorga-anatel/)
- [Teletime — Anatel registra 149 mil provedores regularizados](https://teletime.com.br/02/10/2025/anatel-registra-149-mil-provedores-de-banda-larga-regularizados/)
- [Tecnoblog — Anatel cogita tecnologia para barrar fraude em ligações (Origem Verificada)](https://tecnoblog.net/noticias/anatel-cogita-seguir-eua-com-tecnologia-para-barrar-fraude-em-ligacoes/)
- [Teletime — A implantação da tecnologia STIR/SHAKEN pela Anatel](https://teletime.com.br/20/09/2024/a-implantacao-da-tecnologia-stir-shaken-pela-anatel/)
- [Consumidor Moderno — STIR/SHAKEN "Origem Verificada"](https://consumidormoderno.com.br/stir-shaken-origem-verificada/)
- [asipto.com — Arquitetura Kamailio + FreeSWITCH para VoIP carrier-grade](https://kb.asipto.com/freeswitch:index)
- Ver também as fontes já listadas em `docs/escopo-plataforma-fox-telecom.md`, `docs/roteiro-lancamento.md` e `docs/parcerias-revenda-numeros.md`.
