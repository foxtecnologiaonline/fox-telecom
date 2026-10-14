# Estrutura de Criação do SVA — FOX Telecom

> Como formalizar a FOX Telecom como **prestadora de Serviço de Valor Adicionado (SVA)**, revendendo sobre a infraestrutura de um ou mais parceiros atacadistas já homologados (SCM/STFC) — sem precisar de outorga própria da ANATEL. Complementa `docs/parcerias-revenda-numeros.md` (candidatos a parceiro) e `docs/roteiro-lancamento.md` (fases de lançamento, em especial a Fase 3, que já apontava o SVA como o enquadramento compatível com revenda/intermediação).

## 1. Por que SVA é o enquadramento certo

SVA é definido no **art. 61 da Lei 9.472/1997 (LGT)** como a atividade que acrescenta novas utilidades relacionadas a acesso, armazenamento, apresentação, movimentação ou recuperação de informações a um serviço de telecomunicações que lhe dá suporte, **sem se confundir com ele**. Dois pontos decorrem diretamente disso:

- **§1º — natureza jurídica:** o SVA **não constitui serviço de telecomunicações**. Quem presta SVA é tratado como **usuário** do serviço de telecomunicações de base (o SCM/STFC do parceiro), e não como prestadora de telecomunicações.
- **§2º — direito de acesso à rede:** a lei assegura aos interessados o uso das redes de telecomunicações para prestar SVA, cabendo à ANATEL regular as condições de acesso e o relacionamento entre o provedor de SVA e a prestadora de base — inclusive sob critérios de isonomia e tratamento não discriminatório.

Na prática, isso confirma o que já havia sido levantado em `docs/parcerias-revenda-numeros.md`: **a prestação de SCM/STFC (exploração da rede em si) exige outorga/autorização da ANATEL; o SVA, não.** Há inclusive jurisprudência nesse sentido (ex.: TRF da 1ª Região, tratando provedor que distribui acesso à internet como SVA sem necessidade de autorização, por não se confundir com a exploração do SCM). Isso é o que permite à FOX Telecom operar **sem outorga própria**, apoiada no(s) contrato(s) de acesso à rede do(s) parceiro(s) atacadista(s).

> **Atenção regulatória:** esse enquadramento tem um histórico de disputa — a ANATEL e a maioria das Secretarias da Fazenda estaduais tendem a entender que *provimento de acesso à internet* (ainda que vendido como "SVA") é, na prática, SCM, por envolver a própria capacidade de transmissão, e não só uma "camada" sobre uma rede de terceiro. O ponto de distinção relevante para a FOX é: **a FOX não presta conectividade/transporte por conta própria — ela compra conectividade/numeração pronta de um parceiro outorgado e agrega produto por cima (URA, CRM, automação, billing, atendimento).** É essa divisão de papéis que sustenta o enquadramento como SVA puro. Validar com advogado de telecom antes de formalizar qualquer contrato, principalmente se o produto evoluir para algo que se pareça com "prover a própria rede".

## 2. O que muda em relação ao SCM/STFC (resumo prático)

| | Prestadora de SCM/STFC | Prestadora de SVA (modelo da FOX) |
|---|---|---|
| Precisa de outorga/autorização ANATEL? | Sim | **Não** |
| Como se relaciona com a rede | É dona/operadora da rede de telecom | É **usuária** da rede de um parceiro outorgado, via contrato |
| Numeração | Recebe atribuição direta da ANATEL (plano de numeração) | Opera sobre numeração **atribuída ao parceiro**, cedida/sublicenciada contratualmente |
| Responsabilidade regulatória pela prestação do serviço de telecom em si | Da própria empresa, perante a ANATEL | **Permanece com o parceiro outorgado** — ponto crítico a deixar explícito em contrato |
| ICMS sobre o serviço | Normalmente incide (serviço de comunicação) | Tende a **não incidir** sobre a camada de SVA (mas é um ponto de controvérsia fiscal — não presumir sem orientação contábil/tributária específica) |
| Regime de entrada | Processo de licitação/outorga da ANATEL, prazos longos | Constituição societária + contrato comercial/técnico com o(s) parceiro(s) — muito mais rápido |

## 3. Passo a passo para constituir a FOX como prestadora de SVA

1. **Base societária.** CNPJ já aberto (ver `docs/fase-0-execucao.md`); confirmar CNAE compatível com SVA junto ao contador — candidatos usuais: `63.19-4/00` (portais, provedores de conteúdo e outros serviços de informação na internet) e/ou `61.90-6/99` (outras atividades de telecomunicações, já referenciado em `docs/roteiro-lancamento.md` para fins de licitação). Não existe um CNAE único e oficialmente "do SVA" — a escolha certa depende de como o objeto social descreve a atividade; confirmar com o contador antes de formalizar.
2. **Due diligence regulatória do(s) parceiro(s).** Antes de contratar, confirmar que o parceiro atacadista tem outorga **vigente e válida** de SCM e/ou STFC junto à ANATEL (consulta pública no Sistema Mosaico da ANATEL) — é essa outorga que dá cobertura legal para a atividade de SVA da FOX existir sem outorga própria. Sem isso, a cadeia toda perde o amparo do art. 61 da LGT.
3. **Contrato de acesso à rede / parceria comercial** com cada parceiro (ver seção 4) — é o documento que formaliza o "guarda-chuva regulatório" mencionado em `docs/parcerias-revenda-numeros.md`.
4. **Camada de produto própria.** Para reforçar a distinção de que a FOX é SVA (não SCM disfarçado), construir e documentar a camada de "novas utilidades" sobre a rede do parceiro: URA, roteamento inteligente, CRM/atendimento, relatórios, billing próprio, automações — é essa camada que caracteriza juridicamente o acréscimo de utilidade exigido pelo art. 61.
5. **Adequação à LGPD.** Como a FOX vai tratar dados pessoais de clientes finais (números, chamadas, possivelmente conteúdo de atendimento), mapear bases legais de tratamento e cláusulas de proteção de dados no contrato com o parceiro (quem é controlador/operador de cada dado) — ponto frequentemente esquecido em contratos de revenda de telecom.
6. **Registro contábil/fiscal correto da receita de SVA**, separando-a de qualquer atividade que possa ser lida como SCM, para evitar risco de requalificação tributária (ver seção 5).
7. **Formalizar múltiplos parceiros em paralelo, se aplicável** (ver seção 6) — cada parceiro tem seu próprio contrato independente; não há um "guarda-chuva" regulatório único que cubra vários parceiros ao mesmo tempo.

## 4. Cláusulas essenciais do contrato com o parceiro atacadista (SCM/STFC)

Modelo de referência a negociar com cada parceiro (Zenvia, Telnyx, Plivo, Algar etc. — ver `docs/parcerias-revenda-numeros.md` seção 3 para o mapeamento já feito):

| Cláusula | O que deve conter | Por quê |
|---|---|---|
| **Objeto** | Uso da rede/numeração do parceiro pela FOX para prestação de SVA a clientes finais da FOX | Ancora o contrato no art. 61 §2º da LGT (direito de acesso) |
| **Responsabilidade pela prestação do serviço de telecom** | Explicitar que a responsabilidade regulatória pela qualidade/continuidade do serviço de telecomunicações em si (voz, SMS, transporte) é do parceiro outorgado perante a ANATEL — a FOX responde apenas pela camada de produto/SVA | Evita que a FOX assuma responsabilidade por algo que não controla, e reforça a separação de papéis que sustenta o enquadramento como SVA |
| **Cessão/sublicenciamento de numeração** | Se envolver DID/0800: cláusula de cessão não onerosa de uso (modelo adotado pela Zenvia) ou sublicenciamento equivalente, com reversibilidade caso o contrato termine (o que acontece com os números em uso pelos clientes da FOX) | Numeração só pode ser atribuída pela ANATEL a quem tem outorga — a FOX nunca é "dona" do número, só usuária cedida |
| **Isonomia e não discriminação** | Condições de acesso equivalentes às oferecidas a outros clientes/parceiros de porte similar do mesmo parceiro | Decorre do art. 61 §2º — a ANATEL regula esse relacionamento justamente para evitar discriminação |
| **SLA técnico** | Disponibilidade, qualidade de voz, tempo de portabilidade, suporte técnico, janelas de manutenção | Base para o atestado técnico futuro (Fase 2/3 do roteiro de lançamento) e para honrar o SLA que a FOX oferecer aos próprios clientes |
| **Modelo comercial/repasse** | Tabela de preços de atacado, regras de reajuste, moeda (USD vs BRL — relevante para Telnyx/Plivo), volume mínimo se houver | Insumo direto da precificação já modelada em `docs/parcerias-revenda-numeros.md` seção 6 |
| **Dados pessoais (LGPD)** | Papéis de controlador/operador, prazo de retenção, local de processamento (alguns fornecedores processam fora do Brasil) | Clientes finais são titulares de dados pessoais (número, histórico de chamadas) |
| **Reversibilidade/portabilidade de saída** | O que acontece com números, histórico de chamadas e clientes ativos se o contrato com aquele parceiro terminar | Crítico quando a FOX usa múltiplos parceiros e pode trocar o principal |
| **Vigência e rescisão** | Prazo mínimo (ex.: Telnyx Channel Reseller Program exige 12 meses), aviso prévio, multas | Já mapeado por fornecedor em `docs/parcerias-revenda-numeros.md` |
| **Marca/white-label** | Se o cliente final vê a marca do parceiro ou só a marca FOX | Afeta posicionamento comercial e percepção de quem presta o serviço |

## 5. Riscos regulatórios e fiscais a monitorar

- **Risco de requalificação SVA → SCM:** se a atividade da FOX crescer a ponto de parecer que ela mesma está "fornecendo a rede" (ex.: revenda bruta de capacidade sem camada de produto própria), há risco de a ANATEL ou o Fisco estadual reclassificar a atividade como SCM — o que traria exigência de outorga e incidência de ICMS. Manter a camada de produto (item 3.4) documentada é a principal mitigação.
- **Tomada de Subsídios nº 1/2026 (ANATEL):** consulta pública em andamento sobre tráfego OTT e sobre como os SVAs são vendidos, aderidos, cobrados e cancelados — pode resultar em revisão do Regulamento de Deveres dos Usuários e em um guia de boas práticas de transparência para ofertas digitais. Acompanhar esse processo, pois pode trazer novas obrigações de transparência/consentimento para cobrança de SVA.
- **Cobrança de SVA exige consentimento prévio e expresso do consumidor** — posição já manifestada pela ANATEL em respostas a reclamações. Qualquer upsell/cobrança adicional dentro do produto da FOX deve ter aceite explícito documentado.
- **Dependência de outorga alheia:** se a outorga do parceiro principal for suspensa, cassada ou não renovada pela ANATEL, a operação da FOX para — reforça a recomendação da seção 6 de nunca depender de um único parceiro na fase de escala.
- **Tributação (ICMS vs. não incidência):** a diferenciação fiscal entre SCM (tributado) e SVA (não tributado) é uma área de disputa ativa entre contribuintes e Secretarias de Fazenda estaduais — não presumir isenção automática; validar o enquadramento tributário específico com contador especializado em telecom antes de precificar.

## 6. Múltiplos parceiros atacadistas: por que e como estruturar

A pergunta original já prevê "um ou mais parceiros atacadistas" — isso é uma decisão de arquitetura, não só comercial:

- **Redundância:** se a FOX depender de um único parceiro (ex.: só Telnyx), qualquer instabilidade técnica, bloqueio de conta ou mudança de política do fornecedor paralisa toda a operação. Dois parceiros ativos (ex.: Telnyx como principal + Plivo ou Zenvia como secundário) permitem failover.
- **Segmentação por caso de uso:** nada impede usar parceiros diferentes para produtos diferentes — ex.: Telnyx/Plivo para números/voz internacional de baixo custo, Zenvia para SMS/WhatsApp com operadora parceira nacional, Algar para uma futura oferta regional via modelo de parceiro formal.
- **Negociação de margem:** ter mais de um parceiro cotado dá poder de negociação (evita lock-in de preço).
- **Cada parceiro = um contrato independente.** Não existe um "guarda-chuva" regulatório único: cada relação precisa da sua própria due diligence (seção 3.2) e do seu próprio contrato (seção 4). A camada de produto da FOX (item 3.4) é o que integra tecnicamente as diferentes infraestruturas de baixo nível em uma experiência única para o cliente final — essa orquestração técnica (roteamento entre fornecedores, normalização de API, billing consolidado) é, inclusive, mais um elemento que reforça o enquadramento como SVA (é exatamente a "nova utilidade" que o art. 61 da LGT descreve).
- **Atenção a conflito de cláusulas de exclusividade:** confirmar que nenhum contrato de parceiro assinado tem cláusula de exclusividade que impeça a FOX de operar com outros fornecedores em paralelo.

## 7. Checklist resumido

- [ ] CNAE revisado com contador para refletir atividade de SVA (não misturar com CNAE de SCM/STFC próprio)
- [ ] Due diligence de outorga ANATEL de cada parceiro candidato (Sistema Mosaico)
- [ ] Contrato de acesso à rede assinado com o(s) parceiro(s), contendo as cláusulas da seção 4
- [ ] Camada de produto própria (URA/CRM/billing/automação) documentada e funcionando — já validada tecnicamente na Fase 0 (`docs/fase-0-execucao.md`)
- [ ] Mapeamento LGPD (controlador/operador, retenção, local de processamento) feito com cada parceiro
- [ ] Parecer tributário sobre enquadramento SVA x ICMS obtido com contador especializado
- [ ] Pelo menos 1 parceiro secundário avaliado para redundância, mesmo que ainda não contratado
- [ ] Acompanhamento da Tomada de Subsídios nº 1/2026 da ANATEL (regras de transparência/cobrança de SVA)

## 8. Como isso se encaixa no roteiro de lançamento

Este documento formaliza juridicamente o que `docs/roteiro-lancamento.md` já apontava na Fase 3 ("priorizar editais de objetos compatíveis com revenda/intermediação... SVA... que não exigem execução direta via STFC/SMP"). Na prática:

- **Fase 0–1** (autoconsumo e primeiros clientes): já operam de fato sob o guarda-chuva de SVA, mesmo sem essa formalização ter sido redigida — este documento é o que transforma a prática em enquadramento jurídico explícito e documentado.
- **Fase 2** (formalização plena): o contrato de acesso à rede formalizado aqui (seção 4) é exatamente o que vira "carta de respaldo técnico ou atestado conjunto" citado na Fase 2 do roteiro.
- **Fase 3** (licitações): o enquadramento como SVA é o que evita o problema identificado no roteiro — editais que exigem execução direta via STFC/SMP e vedam subcontratação do serviço-fim.
- **Fase 4** (outorga própria/MVNO): quando/se a FOX migrar para outorga própria, este documento deixa de ser a base regulatória principal — mas as cláusulas de reversibilidade (seção 4) ajudam a migrar clientes/numeração de forma organizada.

## 9. Fontes

- [Lei nº 9.472/1997 (LGT) — Planalto](https://www.planalto.gov.br/ccivil_03/leis/l9472.htm)
- [Migalhas — Novos serviços em telecomunicações enfrentam insegurança interpretativa (art. 61 LGT, SVA x SCM)](https://www.migalhas.com.br/depeso/333649/novos-servicos-em-telecomunicacoes-enfrentam-inseguranca-interpretativa)
- [Teletime — Base Mobile diz que operadoras têm obrigação de fornecer serviço para a prestação do SVA (art. 61 §1º e §2º)](https://teletime.com.br/04/04/2023/base-mobile-diz-que-operadoras-tem-obrigacao-de-fornecer-servico-para-a-prestacao-do-servico-de-valor-adicionado/)
- [Teletime — Todos os usuários de telecomunicações são iguais (isonomia no acesso à rede para SVA)](https://teletime.com.br/07/10/2022/todos-os-usuarios-de-telecomunicacoes-sao-iguais/)
- [Migalhas — Serviço de provedor de internet não precisa de autorização da Anatel (jurisprudência TRF1)](https://www.migalhas.com.br/quentes/208967/servico-de-provedor-de-internet-nao-precisa-de-autorizacao-da-anatel)
- [Econet — Diferenças entre SCM e SVA (tributação, ICMS)](https://blog.econeteditora.com.br/diferencas-entre-servico-de-comunicacao-multimidia-scm-e-servico-de-valor-adicionado-sva/blog_1100x398-3)
- [Teletime — Possíveis desdobramentos da extinção da Norma 4 no mercado de banda larga](https://teletime.com.br/27/06/2025/possiveis-desdobramentos-da-extincao-da-norma-4-no-mercado-de-banda-larga/)
- [Demarest — Client Alert sobre Tomada de Subsídios nº 1/2026 (tráfego OTT e regras de SVA)](https://www.demarest.com.br/?p=166742)
- [Reclame Aqui — resposta da Anatel sobre cobrança de SVA exigir consentimento prévio e expresso](https://www.reclameaqui.com.br/op-telecom/cobranca-indevida-de-sva_SWJoCbdoh9oyXw1i/)
- [Resolução ANATEL nº 769/2024 (revoga/atualiza o Regulamento do SCM, Res. 614/2013)](https://www.lex.com.br/resolucao-anatel-no-769-de-30-de-setembro-de-2024/)
- Ver também as fontes já listadas em `docs/parcerias-revenda-numeros.md` (parceiros candidatos) e `docs/roteiro-lancamento.md` (fases e licitações).
