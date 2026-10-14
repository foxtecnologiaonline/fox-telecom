# Parcerias para Revenda de Números de Operadoras Especializadas — FOX Telecom

> Pesquisa de mercado para a fase 1 de lançamento da FOX Telecom: revenda de números (DID/numeração virtual) de operadoras especializadas, antes de buscar outorga própria.

## 1. Por que essa é a porta de entrada certa

Revender numeração de terceiros evita o maior custo e o maior prazo do setor: obter outorga própria da ANATEL (SCM/STFC), montar rede, e homologar numeração. O modelo de entrada rápida no Brasil é sempre uma destas duas vias:

- **Via CPaaS (software sobre numeração de terceiros):** você contrata uma API de voz/SMS de uma plataforma (global ou nacional) e repassa isso white-label para seus clientes. A plataforma já resolve a ANATEL por trás (como "Operadora Parceira").
- **Via parceria comercial com operadora licenciada:** você vira revenda/correspondente de uma operadora SCM/STFC já outorgada (modelo que a Algar Telecom, por exemplo, formalizou em 2025 para provedores regionais), faturando com margem sobre o plano dela.

Importante: no Brasil, **numeração só pode ser atribuída pela ANATEL a quem tem outorga (SCM/STFC/SMP)**. Logo, nenhuma empresa sem outorga "revende números" de forma própria — ela sempre está dentro do guarda-chuva regulatório de uma operadora parceira. Isso molda todas as opções abaixo.

## 2. Enquadramento regulatório (contexto, não aconselhamento jurídico)

- A Resolução ANATEL nº 769/2024 revogou e atualizou o regulamento do SCM (substituindo a Res. 614/2013).
- A Resolução nº 749/2022 criou os planos de numeração para SCM e SMGS, mas a atribuição efetiva de numeração ao SCM ficou condicionada à revisão de regras de interconexão/remuneração — ou seja, a numeração "pura" de SCM ainda não é simples de obter diretamente.
- A ANATEL sinalizou que ainda vai regular MVNOs e redes neutras, trazendo esse mercado para o PGMC (regras de competição) — hoje o MVNO só existe via acordo comercial com uma SMP detentora de outorga (Vivo, Claro, TIM, Algar).
- Conclusão prática: **a FOX Telecom não vai "ter numeração própria" nessa fase 1** — vai operar como revenda/distribuidora sobre a numeração de um parceiro outorgado. Isso é normal e é como praticamente todo CPaaS e toda revenda de telefonia no Brasil funciona hoje.
- Recomendação: validar com advogado especializado em telecom antes de fechar contrato, principalmente a cláusula de "cessão não onerosa de numeração" (modelo usado pela Zenvia) e os limites de responsabilidade sobre a prestação do serviço de telecom em si (que permanece com a operadora parceira, nunca com o revendedor).

## 3. Candidatos a parceiro, por categoria

### 3.1 CPaaS globais (entrada mais rápida, menor custo inicial, numeração já disponível para BR)

| Empresa | Prós | Contras | Custo/benefício | Custo estimado de parceria |
|---|---|---|---|---|
| **Twilio** | Maior ecossistema de APIs (voz, SMS, WhatsApp), documentação excelente, confiabilidade alta, usado por grandes CPaaS brasileiros como lastro | Preço acima da média, suporte em português limitado, exige CNPJ + comprovação para números BR (até 3 dias úteis de aprovação) | Alto para MVP técnico, mas margem de revenda fica apertada se o concorrente também usa Twilio por trás | Pay-as-you-go, sem fidelidade; números BR a partir de poucos dólares/mês + minutagem; não há "taxa de parceria" pública — modelo self-service |
| **Telnyx** | Números BR a partir de US$ 1/mês, portal self-service (Mission Control), preços agressivos, boa reputação em qualidade de voz | Marca pouco conhecida no Brasil, suporte em inglês, exige CNPJ/documentos para compliance BR | Ótimo custo-benefício para operação enxuta | Sem setup fee relevante; pay-as-you-go |
| **Plivo** | Preço competitivo (DID ~US$5/mês, chamadas a partir de US$0,018-0,02/min), calculadora de comparação direta com Twilio | Ecossistema menor, menos integrações prontas no Brasil | Bom para quem já sabe o volume esperado | Pay-as-you-go, sem contrato mínimo divulgado |
| **Sinch** | Forte presença global, atua também como back-end de vários players brasileiros (ex-Movile/Wavy), 145 países de cobertura de numeração | Pouca transparência de preço BR específico, atendimento mais voltado a contas enterprise | Bom para quem já quer negociar volume desde o início | Modelo enterprise — preço só sob consulta comercial |
| **Vonage (grupo Ericsson)** | Marca consolidada, API robusta de voz/SMS | Preços e disponibilidade de números BR pouco documentados publicamente | Médio — exige contato comercial para entender condições reais no Brasil | Sob consulta |
| **DIDLogic / IDT Express / CommPeak / FlyNumber** | Nicho de atacado de DIDs puro, preços agressivos (alguns a partir de ~US$1-4/mês), bom para só "número + encaminhamento" | Menos recursos de plataforma (sem CRM, sem automação embutida), alguns sem suporte a SMS no Brasil, confiabilidade/compliance variável | Baixo custo, mas exige você construir a camada de produto por cima | Pay-as-you-go, créditos de entrada (ex: até US$100 em bônus em alguns) |

### 3.2 CPaaS/"Operadoras Parceiras" brasileiras (já resolvem a parte regulatória local, suporte em português)

| Empresa | Prós | Contras | Custo/benefício | Custo estimado de parceria |
|---|---|---|---|---|
| **Zenvia (ex-TotalVoice)** | Maior player nacional de CPaaS, já resolve a "Operadora Parceira" por trás (modelo de cessão não onerosa de linha), API madura de voz/SMS/WhatsApp, suporte em português, cobrança sem repasse direto de custo de telecom (cobra só a licença da plataforma) | Termos deixam claro que a Zenvia não responde pela qualidade do serviço de telecom em si (responsabilidade é da operadora parceira dela, não identificada publicamente) — ou seja, você fica com duas camadas de dependência | Bom custo-benefício para quem quer lançar rápido com cara nacional | Modelo pay-as-you-go divulgado para PMEs; para revenda/white-label em volume, negociação comercial direta (não publicada) |
| **3C Plus** | Forte em discador/URA para operações de call center, já usado por muitas revendas | Mais focado em software de atendimento do que em atacado puro de numeração | Médio — mais adequado se a FOX vai ter operação própria de atendimento | Sob consulta comercial |
| **Leucotron** | Tradição em telefonia corporativa (PABX/URA), hardware + software | Modelo mais voltado a integração on-premise que a revenda pura de numeração como produto | Baixo a médio para o modelo de "revenda de números" puro | Sob consulta comercial |

### 3.3 Operadoras licenciadas (SCM/SMP) com modelo formal de parceiro/revenda

| Empresa | Prós | Contras | Custo/benefício | Custo estimado de parceria |
|---|---|---|---|---|
| **Algar Telecom** | Lançou em set/2025 um modelo inédito de parceria para provedores regionais (>7 mil clientes): a Algar cuida de backbone, billing e suporte; o parceiro foca em vendas/expansão local. É o modelo mais próximo do que a FOX quer fazer | Pensado originalmente para ISPs/provedores regionais com base de clientes já existente, não para uma revenda pura de numeração nova | Alto, se a FOX conseguir se enquadrar no perfil de parceiro regional | Não divulgado publicamente — negociação direta com time comercial da Algar |
| **Grupo Ligga / Sercomtel** | Sercomtel foi privatizada (2020) e hoje é parte do Grupo Ligga; rede própria em ~15 municípios, fora disso atua em parceria com dados da Ligga | Estrutura mais regional/fragmentada, processo de parceria menos padronizado | Médio — bom nicho regional (Paraná), fraco para escala nacional | Sob consulta |
| **Vivo / Claro / TIM (atacado)** | Maior capilaridade e confiabilidade de rede do país, essenciais se a FOX mirar MVNO móvel no futuro | Processos de atacado burocráticos, ciclos de negociação longos, exigem volume mínimo relevante para fazer sentido comercialmente | Baixo no curto prazo (fase 1), alto se a FOX evoluir para MVNO (há ~400 MVNOs ativos no Brasil ao fim de 2025, segundo TIP Brasil) | Tipicamente contratos de atacado com volume mínimo e caução — inacessível para operação pré-revenue |
| **Brisanet (atacado/parceiros)** | Provedor regional em expansão agressiva no Nordeste, mais aberto a parcerias que os grandes 3 | Cobertura ainda concentrada regionalmente | Médio — bom se a FOX focar inicialmente em uma região | Sob consulta comercial |

## 4. Recomendação de sequenciamento

1. **Fase 1 (0–3 meses, MVP de baixo custo):** contratar uma API de CPaaS pay-as-you-go (Telnyx ou Plivo para custo mínimo; Zenvia se quiser suporte em português e cara nacional desde o dia 1) para validar demanda e fluxo de revenda sem contrato mínimo nem outorga própria.
2. **Fase 2 (3–9 meses, com tração comprovada):** negociar condições de atacado/white-label diretamente com Sinch, Vonage ou Zenvia (contrato de volume, melhores margens), e paralelamente avaliar o modelo de parceiro formal da Algar Telecom caso a FOX já tenha base de clientes relevante.
3. **Fase 3 (escala, 12+ meses):** se o modelo validar e o volume justificar, avaliar outorga SCM própria junto à ANATEL e/ou acordo de MVNO com uma SMP (Vivo/Claro/TIM/Algar) para internalizar margem e reduzir dependência de terceiros.

## 5. Limitações desta pesquisa

Preços de atacado e condições de parceria comercial (setup fee, volume mínimo, % de margem) raramente são públicos — a maioria dos valores acima é de varejo/self-service ou estimativa de mercado. Os próximos passos recomendados são: (a) abrir conversas comerciais diretas com Zenvia, Algar Telecom e Telnyx/Plivo para cotação real; (b) validar com advogado de telecom o contrato de "Operadora Parceira" antes de assinar qualquer termo de cessão de numeração.

## 6. Fontes

- [Telnyx – Brazil DID requirements](https://support.telnyx.com/en/articles/5464041-brazil-did-requirements)
- [Telnyx – Brazil virtual phone numbers](https://telnyx.com/phone-numbers/brazil)
- [Plivo – SIP trunking pricing BR](https://www.plivo.com/sip-trunking/pricing/br/)
- [DIDLogic – Brazil virtual numbers](https://didlogic.com/virtual-phone-numbers/brazil/)
- [IDT Express – Brazil](https://www.idtexpress.com/pt/countries/brazil/)
- [FlyNumber – Brazil](https://www.flynumber.com/virtual-phone-number/Brazil)
- [CommPeak – Brazil virtual numbers](https://www.commpeak.com/services/virtual-numbers-dids/coverage/brazil)
- [Sinch – cobertura de números](https://sinch.com/pt/numeros-telefonicos/recursos/cobertura-de-numeros/)
- [Zenvia – comunicado TotalVoice agora é Zenvia](https://zenvia.com/blog/perguntas-sobre-totalvoice/)
- [Zenvia – Termos de Serviço da Plataforma de Voz](https://zenvia.com/termos/plataforma-voz/)
- [Teletime – Algar apresenta modelo inédito para provedores](https://teletime.com.br/23/09/2025/algar-apresenta-modelo-inedito-para-provedores-expandirem-seu-negocio/)
- [Sercomtel – Relatório da Administração 2023](https://www.sercomtel.com.br/site/views/_data/public-files/files/relatorio-da-administracao-2023-1724261595.pdf)
- [Mattos Filho – Anatel aprova novo regulamento de numeração](https://www.mattosfilho.com.br/unico/regulamento-servicos-telecomunicacoes/)
- [Legisweb – Resolução Anatel nº 614/2013 (revogada pela 769/2024)](https://www.legisweb.com.br/legislacao/?id=451782)
- [MobileTime – TIP Brasil: 400 MVNOs e 100 mil clientes ativos](https://www.mobiletime.com.br/noticias/23/02/2026/tip-100-mil-mvnos/)
