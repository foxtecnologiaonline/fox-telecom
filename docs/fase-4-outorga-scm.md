# Fase 4 — Estruturação da outorga SCM própria

> Detalha a Fase 4 do `docs/roteiro-lancamento.md` ("Outorga própria / MVNO formal"). Complementa a seção 3.3 do `docs/parcerias-revenda-numeros.md`, onde já se concluiu que, nas Fases 1–3, a FOX opera sob a outorga de um parceiro (CPaaS ou operadora licenciada), nunca com numeração própria. Este documento estrutura o que muda quando a FOX decide buscar a **outorga SCM (Serviço de Comunicação Multimídia) em nome próprio**.

## 1. O que é a outorga SCM e por que ela é diferente de uma licitação

SCM é um serviço de telecomunicações de interesse coletivo prestado em **regime privado**, outorgado pela ANATEL por **autorização administrativa** — não há leilão/licitação nem número limitado de outorgas, como ocorre no SMP (telefonia móvel). Em tese, qualquer empresa que cumpra os requisitos jurídicos, técnicos, econômico-financeiros e fiscais pode obter a outorga. Isso torna o SCM a via regulatória mais acessível para a FOX "ter outorga própria" — bem mais simples do que buscar SMP ou STFC, e sem a necessidade de vencer um certame.

Isso não elimina trabalho: o pedido tramita formalmente pela ANATEL (**Sistema Mosaico**), exige documentação completa de habilitação da empresa e, desde 2025, não há mais atalho por porte (ver seção 2).

## 2. Mudança regulatória crítica (2025) — ler antes de planejar prazos

A pesquisa para este documento encontrou uma mudança relevante e recente que impacta diretamente o gatilho da Fase 4:

- **Fim da dispensa de outorga por porte reduzido.** A antiga regra permitia que prestadoras de SCM de pequeno porte (até 5.000 acessos) operassem sem outorga formal. O **Acórdão ANATEL nº 176, de 30/06/2025**, suspendeu cautelarmente essa dispensa. O prazo para as antigas dispensadas se regularizarem terminou em **28/10/2025**. Na prática: **hoje toda prestadora de SCM precisa de autorização formal, independente do volume de acessos** — não existe mais um "modo leve" para operação pequena.
- **Consolidação normativa em curso.** Houve mais de uma rodada de revisão regulatória em 2024–2025 (ex.: Resolução 769/2024, citada no `docs/parcerias-revenda-numeros.md`, e um novo RGST — Regulamento Geral de Serviços de Telecomunicações — associado à Resolução 777/2025, com vigência a partir de ~out/2025). As fontes encontradas nesta pesquisa **divergem em detalhes** sobre qual resolução está em vigor em cada ponto. **Antes de iniciar o pedido, confirmar diretamente no site da ANATEL (gov.br/anatel) qual é o regulamento consolidado vigente** — não tomar o número de resolução deste ou do outro documento como definitivo sem checar a data da consulta.
- **O que isso muda para o roteiro da FOX:** nas Fases 0–3 (revenda/CPaaS, sem rede/estação própria), nada muda — a FOX continua sem precisar de outorga, pois não está operando estações de telecomunicações em nome próprio. O impacto é só sobre a Fase 4: quando chegar a hora, **não há mais a opção de operar pequeno e informal "por baixo do radar" do porte reduzido** — o caminho é o pedido de autorização completo desde o primeiro dia de operação com rede própria.

## 3. Pré-requisitos de habilitação (base: Regulamento Geral de Outorgas — RGO, Resolução ANATEL nº 720/2020, Anexo I)

| Categoria | O que é exigido |
|---|---|
| **Habilitação jurídica** | Razão social, CNPJ, endereço; contrato social/estatuto e alterações, registrado na Junta Comercial; inscrição estadual (se aplicável ao objeto); CNAE compatível (telecomunicações — mesmo CNAE já mapeado na Fase 2 do roteiro de lançamento: 61.90-6/99, 61.10-8). |
| **Qualificação técnica** | Declaração (no próprio sistema da ANATEL) de que a empresa tem aptidão para a atividade e corpo técnico qualificado disponível; indicação de **responsável técnico habilitado** (registro ativo no CREA ou CFT). |
| **Qualificação econômico-financeira** | Declaração de boa situação financeira e de que a empresa não está em processo de falência/recuperação judicial. |
| **Regularidade fiscal e trabalhista** | Certidões negativas (ou positivas com efeito de negativa) de: Receita Federal/PGFN, FGTS (CRF), Justiça do Trabalho (CNDT), e verificação de pendências junto à própria ANATEL/Fistel. Em etapa posterior do processo, normalmente também se exige regularidade estadual e municipal. |
| **Projeto técnico** | Descrição da rede/infraestrutura a ser usada para prestar o serviço (mesmo que inicialmente modesta — ex.: rede própria, capacidade alugada, ou interconexão com outra prestadora). |

> Boa notícia prática: boa parte dessas certidões (Federal/PGFN, FGTS, Trabalhista, Estadual, Municipal) **já está no checklist de prontidão para licitar da Fase 2** (`docs/roteiro-lancamento.md`, seção "Checklist de prontidão"). Rodar a Fase 2 completa deixa a FOX com quase toda a documentação societária/fiscal pronta para também pedir a outorga SCM — as duas frentes compartilham pré-requisitos.

## 4. Passo a passo do pedido (Sistema Mosaico)

1. **Cadastro como usuário externo da ANATEL (via SEI/Mosaico):** o responsável legal ou representante se cadastra como pessoa física; é necessário apresentar (presencialmente em unidade da ANATEL ou por Correios ao Protocolo Sede) cópia de RG/CPF, comprovante de residência e o Termo de Declaração de Concordância e Veracidade assinado.
2. **Abertura do pedido no Mosaico:** o formulário tem três etapas — (a) dados do formulário, (b) anexos, (c) termos e condições. Ao informar o CNPJ, o sistema consulta a Receita Federal e pré-preenche parte dos dados.
3. **Upload dos anexos:** para cada item exigido (listados na seção 3), anexar o documento correspondente e preencher a validade quando solicitado.
4. **Indicação do responsável técnico** (CREA/CFT) e do projeto técnico básico.
5. **Aceite dos termos e condições de outorga** (compromissos de prestação do serviço, regras do RGO/RGST aplicáveis).
6. **Análise pela ANATEL:** a agência confere a documentação e pode solicitar complementação — responder rápido evita perder posição na fila (mesma lógica de caminho crítico já usada na Fase 0 com KYC de fornecedor).
7. **Publicação do ato de outorga** (Despacho/Portaria) e emissão do **Termo de Autorização**.
8. **Habilitação no FISTEL** e pagamento da TFI (ver seção 5) antes de iniciar a operação da(s) estação(ões).
9. **Licenciamento de cada estação** usada na prestação do serviço (etapa separada e recorrente — não é só a outorga em si).

## 5. Custos regulatórios a orçar

| Item | O que é | Observação |
|---|---|---|
| **TFI** (Taxa de Fiscalização de Instalação) | Paga uma única vez, no início da operação de cada estação | Valor varia por tipo/abrangência (local, regional, nacional); fontes de 2025 mencionam proposta de redução para abrangência local/estadual (ex.: R$400 local vs. ~R$9.000 nacional) — **valor em discussão regulatória, confirmar tabela vigente antes de orçar**. |
| **TFF** (Taxa de Fiscalização de Funcionamento) | Anual, recorrente | Alíquota de referência: ~33% do valor da TFI por estação. |
| **FUST / FUNTTEL** | Contribuições setoriais recorrentes | Aplicável a prestadoras com outorga; valores e periodicidade variam — consolidar junto ao Guia das Obrigações das PPPs (ver seção 6). |
| **Custo de projeto técnico / consultoria regulatória** | Opcional, mas comum | Boa parte das prestadoras pequenas contrata consultoria especializada (ex.: escritórios de regulatório de telecom) para montar o pedido e evitar retrabalho — avaliar custo-benefício vs. fazer internamente. |

> Nota: a TFI/TFF está sendo questionada no STF (ADI 7787, sobre as alíquotas — não sobre a existência da taxa). Isso não deve travar o planejamento da FOX, mas vale monitorar caso haja mudança de valor antes do pedido.

## 6. Obrigações pós-outorga (o que muda no dia a dia depois de aprovado)

Ao obter a outorga, a FOX passa a ser uma **Prestadora de Pequeno Porte (PPP)** — definida pela ANATEL como grupo com menos de 5% de participação de mercado em cada mercado de varejo em que atua (Resolução nº 779/2025). Isso implica obrigações recorrentes, consolidadas no **Guia das Obrigações das PPPs** (publicado pela ANATEL, revisado periodicamente):

- Licenciamento de estações (cada ponto de rede operado precisa de licença própria, renovável).
- Envio periódico de dados à ANATEL (indicadores de qualidade, base de acessos, etc. — ver se o conjunto de obrigações de uma PPP de SCM é mais leve que o de SMP/STFC).
- Pagamento dos fundos setoriais (FUST, FUNTTEL) e das taxas Fistel (TFI/TFF).
- Atendimento às regras de atendimento ao consumidor e de qualidade aplicáveis ao SCM.
- **Atribuição de numeração própria** (DIDs em nome da FOX, não mais sob o guarda-chuva de um parceiro) — processo tratado separadamente junto ao Plano de Numeração da ANATEL; a Resolução nº 749/2022 trata dos planos de numeração para SCM, mas (conforme já registrado no `docs/parcerias-revenda-numeros.md`) a atribuição efetiva de numeração ao SCM dependia da revisão das regras de interconexão/remuneração — **confirmar status atualizado dessa condicionante antes de contar com numeração própria como certeza da Fase 4**.
- Possível necessidade de **acordo de interconexão** com outras prestadoras (SMP/STFC) para completar chamadas fora da própria rede.

## 7. Critério de decisão — quando disparar esta fase

Mantém o gatilho já definido no `docs/roteiro-lancamento.md` (Fase 4): **volume e caixa suficientes para sustentar a outorga**. Na prática, isso significa que o caixa recorrente da FOX precisa cobrir, de forma folgada, pelo menos:

- TFI inicial (estação(ões)) + TFF anual recorrente + FUST/FUNTTEL.
- Custo de montar/manter o projeto técnico e, se optado, consultoria regulatória.
- Tempo de dedicação do responsável técnico (CREA/CFT) e do time societário para manter certidões e licenciamentos sempre válidos — é uma obrigação contínua, não um evento único.
- Margem para o período de análise do pedido pela ANATEL (prazo varia; não há SLA curto garantido — tratar como meses, não semanas, no planejamento de caixa).

**Alternativa a considerar em paralelo:** antes de assumir o custo/esforço da outorga própria, reavaliar o acordo de MVNO formal com uma SMP (Vivo/Claro/TIM/Algar) — já mapeado na seção 3.3 do `docs/parcerias-revenda-numeros.md` — como caminho possivelmente mais rápido para destravar as licitações da Fase 3 que exigem execução direta, sem todo o ciclo de outorga SCM. A decisão entre "outorga SCM própria" vs. "MVNO formal" deve pesar: velocidade (MVNO tende a ser mais rápido, depende de acordo comercial) vs. independência/margem de longo prazo (outorga própria remove a dependência de terceiros definitivamente).

## 8. Checklist resumido da Fase 4

- [ ] Confirmar no site oficial da ANATEL o regulamento consolidado vigente (RGO + regulamento de SCM/RGST atual) antes de iniciar o pedido
- [ ] Fase 2 do roteiro de lançamento 100% concluída (certidões, CNAE, capital social) — pré-requisito compartilhado
- [ ] Responsável técnico identificado e com registro ativo no CREA ou CFT
- [ ] Projeto técnico básico da rede/infraestrutura documentado
- [ ] Cadastro como usuário externo ANATEL feito (RG/CPF/comprovante de residência + Termo de Declaração enviados)
- [ ] Pedido aberto no Sistema Mosaico (formulário + anexos + termos)
- [ ] Orçamento de TFI/TFF/FUST/FUNTTEL confirmado com valores vigentes
- [ ] Decisão tomada entre outorga SCM própria vs. MVNO formal (ou as duas, em sequência)
- [ ] Termo de Autorização publicado e estação(ões) licenciada(s) antes de iniciar operação

## 9. Fontes

- [ANATEL — Tutorial do Sistema Mosaico](https://sistemas.anatel.gov.br/anexar-api/publico/anexos/download/ded8a405672b210c6ca58b4607e560cb)
- [LinkedIn — Sistema Mosaico para obtenção da licença SCM](https://pt.linkedin.com/pulse/sistema-mosaico-para-obten%C3%A7%C3%A3o-da-licen%C3%A7a-scm-servi%C3%A7o-rafael-paneque)
- [CIANET — Passo a passo para obter a licença SCM](https://www.cianet.com.br/gestao-e-boas-praticas/passo-a-passo-para-obter-licenca-scm-online-em-poucos-dias/)
- [Semeo Consultoria — Como obter a outorga SCM da ANATEL](https://semeoconsultoria.com.br/como-obter-a-outorga-scm-da-anatel-passo-a-passo-completo/)
- [Transmitter — Como solicitar Licença SCM, STFC e SeAC](https://transmitter.com.br/licenca-scm-anatel/)
- [Diretolegaliza — O Processo de Outorga e Regulamentação do SCM na ANATEL](https://diretolegaliza.com/?p=12689)
- [Diretolegaliza — Guia da ANATEL para PPPs exige regularização até outubro](https://dplnews.com/?p=283071)
- [DPL News — Anatel revoga 42 resoluções e redefine regras (novo RGST)](https://dplnews.com/?p=273293)
- [SipPulse — Resolução 777 e o novo marco do STFC: o que muda para provedores](https://sippulse.com/en/blog/resolucao-777-e-o-novo-marco-do-stfc-o-que-muda-para-provedores)
- [TeleTime — Ação das teles no STF contra as taxas de fiscalização da ANATEL (TFI/TFF, ADI 7787)](https://teletime.com.br/11/03/2025/a-acao-das-teles-no-stf-contra-as-taxas-de-fiscalizacao-da-anatel/)
- Ver também as fontes regulatórias já listadas em `docs/parcerias-revenda-numeros.md` (Resolução ANATEL 769/2024, 749/2022) e `docs/roteiro-lancamento.md`.

> **Aviso importante:** este documento é um estruturador de processo, não aconselhamento jurídico/regulatório. Os resultados de pesquisa usados aqui vieram majoritariamente de blogs de consultoria e notícias setoriais, não do texto oficial consolidado da ANATEL — há pontos sinalizados acima como "confirmar" porque fontes diferentes deram respostas distintas ou desatualizadas. Antes de submeter qualquer pedido real no Sistema Mosaico, validar os requisitos e taxas atuais diretamente em gov.br/anatel ou com um advogado/consultor especializado em regulatório de telecom.
