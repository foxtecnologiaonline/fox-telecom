# Parcerias para Revenda de Números de Operadoras Especializadas — FOX Telecom

> Pesquisa de mercado para a fase 1 de lançamento da FOX Telecom: revenda de números (DID/numeração virtual) de operadoras especializadas, antes de buscar outorga própria. Ver `docs/estrutura-sva.md` para o enquadramento jurídico formal (SVA) que sustenta esse modelo de revenda sem outorga.

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

| Empresa | Prós | Contras | Custo/benefício | Custo estimado de parceria | Posso revender? |
|---|---|---|---|---|---|
| **Twilio** | Maior ecossistema de APIs (voz, SMS, WhatsApp), documentação excelente, confiabilidade alta, usado por grandes CPaaS brasileiros como lastro | Preço acima da média, suporte em português limitado, exige CNPJ + comprovação para números BR (até 3 dias úteis de aprovação) | Alto para MVP técnico, mas margem de revenda fica apertada se o concorrente também usa Twilio por trás | Pay-as-you-go, sem fidelidade; números BR a partir de poucos dólares/mês + minutagem; não há "taxa de parceria" pública — modelo self-service | **Modelo ISV sim** (embarcar a API no seu produto e servir seus clientes finais — é o uso esperado); **revenda formal/sublicenciamento bruto, não** sem contrato — o ToS geral veda resale/sublicense a terceiros fora do modelo de "End Users" do seu próprio produto, e o programa formal de reseller é só por convite. WhatsApp é mais restrito ainda: proibido redistribuir sem entrar no Tech Provider Program |
| **Telnyx** | Números BR a partir de US$ 1/mês, portal self-service (Mission Control), preços agressivos, boa reputação em qualidade de voz | Marca pouco conhecida no Brasil, suporte em inglês, exige CNPJ/documentos para compliance BR | Ótimo custo-benefício para operação enxuta | Sem setup fee relevante; pay-as-you-go | **Sim, explicitamente.** A própria Telnyx tem um FAQ público "Can I resell your services?" confirmando que sim, com plataforma multi-tenant pensada para isso. Além do self-service, há um **Channel Reseller Program** formal (comissionado, mínimo de US$500/mês de contrato, prazo mínimo de 12 meses) |
| **Plivo** | Preço competitivo (DID ~US$5/mês, chamadas a partir de US$0,018-0,02/min), calculadora de comparação direta com Twilio | Ecossistema menor, menos integrações prontas no Brasil | Bom para quem já sabe o volume esperado | Pay-as-you-go, sem contrato mínimo divulgado | **Provavelmente sim para voz/SMS** (tem guia próprio de boas práticas para ISVs/revendas em messaging A2P, sem veto geral encontrado na AUP) — **mas WhatsApp é expressamente proibido**: o termo suplementar da Plivo veda em caixa alta reseller/redistribuir/sublicenciar os serviços de WhatsApp Business a terceiros |
| **Sinch** | Forte presença global, atua também como back-end de vários players brasileiros (ex-Movile/Wavy), 145 países de cobertura de numeração | Pouca transparência de preço BR específico, atendimento mais voltado a contas enterprise | Bom para quem já quer negociar volume desde o início | Modelo enterprise — preço só sob consulta comercial | **Tem programas de parceiro formais** (Sinch Converse Partner com comissão, sem taxa de adesão; Operator Connect para Partners voltado a CSP/MSP/VAR), mas não encontrei confirmação pública específica para revenda de API de voz/número pura — **confirmar direto com o time comercial** |
| **Vonage (grupo Ericsson)** | Marca consolidada, API robusta de voz/SMS | Preços e disponibilidade de números BR pouco documentados publicamente | Médio — exige contato comercial para entender condições reais no Brasil | Sob consulta | **Tem Reseller Program formal** (parceiro é dono do contrato comercial com o cliente final), mas o foco declarado do programa é UK/EMEA/APAC — **cobertura para Brasil/LatAm não confirmada**, perguntar antes de assumir que vale aqui |
| **DIDLogic / IDT Express / CommPeak / FlyNumber** | Nicho de atacado de DIDs puro, preços agressivos (alguns a partir de ~US$1-4/mês), bom para só "número + encaminhamento" | Menos recursos de plataforma (sem CRM, sem automação embutida), alguns sem suporte a SMS no Brasil, confiabilidade/compliance variável | Baixo custo, mas exige você construir a camada de produto por cima | Pay-as-you-go, créditos de entrada (ex: até US$100 em bônus em alguns) | **Geralmente sim** — são provedores de atacado por natureza (o próprio modelo de negócio deles é vender para quem revende), mas isso não foi verificado caso a caso nos termos de cada um — confirmar antes de operar em volume |

### 3.2 CPaaS/"Operadoras Parceiras" brasileiras (já resolvem a parte regulatória local, suporte em português)

| Empresa | Prós | Contras | Custo/benefício | Custo estimado de parceria | Posso revender? |
|---|---|---|---|---|---|
| **Zenvia (ex-TotalVoice)** | Maior player nacional de CPaaS, já resolve a "Operadora Parceira" por trás (modelo de cessão não onerosa de linha), API madura de voz/SMS/WhatsApp, suporte em português, cobrança sem repasse direto de custo de telecom (cobra só a licença da plataforma) | Termos deixam claro que a Zenvia não responde pela qualidade do serviço de telecom em si (responsabilidade é da operadora parceira dela, não identificada publicamente) — ou seja, você fica com duas camadas de dependência | Bom custo-benefício para quem quer lançar rápido com cara nacional | Modelo pay-as-you-go divulgado para PMEs; para revenda/white-label em volume, negociação comercial direta (não publicada) | **Sim, de forma explícita e formal.** Existe o programa **Zenvia Partners**, com uma modalidade específica **"Partner VAR"** descrita como gestão de "clientes compartilhados desde a revenda até o suporte" — é literalmente o modelo que a FOX quer. Entrada via formulário de interesse no site; condições comerciais detalhadas não são públicas |
| **3C Plus** | Forte em discador/URA para operações de call center, já usado por muitas revendas | Mais focado em software de atendimento do que em atacado puro de numeração | Médio — mais adequado se a FOX vai ter operação própria de atendimento | Sob consulta comercial | **Não confirmado** — não encontrei programa de revenda de numeração específico; perguntar direto se há modelo de parceria/revenda |
| **Leucotron** | Tradição em telefonia corporativa (PABX/URA), hardware + software | Modelo mais voltado a integração on-premise que a revenda pura de numeração como produto | Baixo a médio para o modelo de "revenda de números" puro | Sob consulta comercial | **Não confirmado** — modelo mais B2B tradicional/on-premise, sem programa de revenda de numeração encontrado publicamente |

### 3.3 Operadoras licenciadas (SCM/SMP) com modelo formal de parceiro/revenda

| Empresa | Prós | Contras | Custo/benefício | Custo estimado de parceria | Posso revender? |
|---|---|---|---|---|---|
| **Algar Telecom** | Lançou em set/2025 um modelo inédito de parceria para provedores regionais (>7 mil clientes): a Algar cuida de backbone, billing e suporte; o parceiro foca em vendas/expansão local. É o modelo mais próximo do que a FOX quer fazer | Pensado originalmente para ISPs/provedores regionais com base de clientes já existente, não para uma revenda pura de numeração nova | Alto, se a FOX conseguir se enquadrar no perfil de parceiro regional | Não divulgado publicamente — negociação direta com time comercial da Algar | **Sim, via modelo formal de parceria** lançado em 2025 — mas pensado para quem já tem base de clientes (ISP regional), não para revenda pura de numeração do zero |
| **Grupo Ligga / Sercomtel** | Sercomtel foi privatizada (2020) e hoje é parte do Grupo Ligga; rede própria em ~15 municípios, fora disso atua em parceria com dados da Ligga | Estrutura mais regional/fragmentada, processo de parceria menos padronizado | Médio — bom nicho regional (Paraná), fraco para escala nacional | Sob consulta | **Não documentado publicamente** — possível via parceria comercial direta, mas sem programa formal conhecido |
| **Vivo / Claro / TIM (atacado)** | Maior capilaridade e confiabilidade de rede do país, essenciais se a FOX mirar MVNO móvel no futuro | Processos de atacado burocráticos, ciclos de negociação longos, exigem volume mínimo relevante para fazer sentido comercialmente | Baixo no curto prazo (fase 1), alto se a FOX evoluir para MVNO (há ~400 MVNOs ativos no Brasil ao fim de 2025, segundo TIP Brasil) | Tipicamente contratos de atacado com volume mínimo e caução — inacessível para operação pré-revenue | **Sim, mas só via contrato formal de atacado/MVNO** — não é um "programa de revenda" simples de aderir, é negociação de grande porte com caução/volume mínimo |
| **Brisanet (atacado/parceiros)** | Provedor regional em expansão agressiva no Nordeste, mais aberto a parcerias que os grandes 3 | Cobertura ainda concentrada regionalmente | Médio — bom se a FOX focar inicialmente em uma região | Sob consulta comercial | **Não confirmado** — sob consulta comercial direta |

> **Nuance importante sobre "posso revender":** para APIs internacionais (Twilio, Plivo), existe uma diferença entre **modelo ISV** (embarcar a API dentro do seu produto/software e servir seus próprios clientes finais — isso é o uso esperado e normalmente permitido) e **revenda bruta/sublicenciamento** (repassar a capacidade da API como está, sem camada de produto própria — isso costuma exigir um contrato de parceria formal, às vezes só por convite). O modelo de negócio da FOX (revenda de números com um produto/plataforma por cima) se encaixa melhor como ISV na maioria dos fornecedores internacionais — mas **sempre confirmar por escrito com o time comercial** antes de operar em volume, especialmente para canais com regra própria mais restrita como WhatsApp Business.

## 4. Recomendação de sequenciamento

1. **Fase 1 (0–3 meses, MVP de baixo custo):** contratar uma API de CPaaS pay-as-you-go (Telnyx ou Plivo para custo mínimo; Zenvia se quiser suporte em português e cara nacional desde o dia 1) para validar demanda e fluxo de revenda sem contrato mínimo nem outorga própria.
2. **Fase 2 (3–9 meses, com tração comprovada):** negociar condições de atacado/white-label diretamente com Sinch, Vonage ou Zenvia (contrato de volume, melhores margens), e paralelamente avaliar o modelo de parceiro formal da Algar Telecom caso a FOX já tenha base de clientes relevante.
3. **Fase 3 (escala, 12+ meses):** se o modelo validar e o volume justificar, avaliar outorga SCM própria junto à ANATEL e/ou acordo de MVNO com uma SMP (Vivo/Claro/TIM/Algar) para internalizar margem e reduzir dependência de terceiros.

## 5. Limitações desta pesquisa

Preços de atacado e condições de parceria comercial (setup fee, volume mínimo, % de margem) raramente são públicos — a maioria dos valores acima é de varejo/self-service ou estimativa de mercado. Os próximos passos recomendados são: (a) abrir conversas comerciais diretas com Zenvia, Algar Telecom e Telnyx/Plivo para cotação real; (b) validar com advogado de telecom o contrato de "Operadora Parceira" antes de assinar qualquer termo de cessão de numeração.

## 6. Precificação, estrutura mínima e ponto de equilíbrio

> **Aviso de premissas:** não existe tabela pública de preço de atacado por operadora/CPaaS (ver seção 5). Os valores abaixo combinam (a) preços de varejo/self-service já levantados (Telnyx, Plivo, DIDLogic) convertidos para R$, e (b) benchmarks de mercado de serviços de numeração virtual/PABX em nuvem no Brasil. Servem para dimensionar a ordem de grandeza e testar a estrutura do modelo — **precisam ser substituídos por cotações reais** antes de qualquer decisão de capital.

### 6.1 CAPEX inicial (investimento pré-operacional, único)

| Item | Estimativa (R$) |
|---|---|
| Abertura de empresa (CNPJ, contrato social se LTDA) | 500 – 2.000 |
| Identidade visual básica (logo, manual de marca) | 0 – 3.000 |
| Site institucional + landing page de vendas (no-code) | 0 – 3.000 |
| Integração técnica inicial com a API do fornecedor (dev/freelancer) | 0 – 6.000 |
| Setup de cobrança recorrente (Pix/boleto/cartão via gateway) | 0 – 500 |
| Assessoria jurídica (revisão do contrato de "Operadora Parceira"/cessão de numeração) | 1.500 – 3.000 |
| Capital de giro (2–3 meses de operação até gerar caixa) | 10.000 – 20.000 |
| **Total CAPEX inicial** | **≈ R$ 15.000 – 35.000** |

### 6.2 OPEX mensal — estrutura mínima para operar

**Cenário enxuto** (fundador(a) full-time cuidando de vendas/operação, sem CLT):

| Item | R$/mês |
|---|---|
| Contabilidade terceirizada | 300 – 600 |
| Ferramentas (CRM, billing SaaS, WhatsApp Business API, helpdesk) | 300 – 600 |
| Hospedagem, domínio, e-mail profissional | 100 – 200 |
| Marketing/tráfego pago inicial | 1.000 – 2.500 |
| Suporte ao cliente (freelancer/part-time, se não for o fundador) | 0 – 1.500 |
| Taxa mínima de plataforma CPaaS (quando houver, pay-as-you-go geralmente é R$0) | 0 – 500 |
| **Total OPEX fixo (enxuto)** | **≈ R$ 2.000 – 5.500/mês** |

**Cenário estruturado** (+1 pessoa full-time em vendas/suporte, CLT ou PJ): soma **+ R$ 3.000 – 6.000/mês** → **≈ R$ 6.000 – 12.000/mês**.

Pró-labore do(s) fundador(es) não está incluso acima — entra como variável de decisão (reinvestir vs. remunerar).

### 6.3 Precificação (custo variável x preço de venda por número ativo)

Custo variável estimado por número/cliente ativo (pago ao fornecedor):

| Componente | R$/mês |
|---|---|
| Aluguel do número/DID | 10 – 25 |
| Minutos inclusos (pacote médio ~100–300 min, custo ~R$0,05–0,12/min) | 10 – 25 |
| **Custo variável total por número** | **≈ R$ 25 – 45** |

#### 6.3.1 Confirmado na prática: Telnyx a US$ 1/mês por número

Ao abrir o cadastro na Telnyx (fase 0), o valor real do aluguel do DID Brasil é **US$ 1,00/mês confirmado** — na faixa inferior da estimativa acima. Câmbio de referência usado aqui: **R$ 5,50/US$** (ajuste pela cotação do dia). Isso confirma e reduz a ponta inferior do custo variável, mas o custo por minuto de chamada (que não vem incluso no US$1 — é cobrado à parte, por uso) **ainda precisa ser confirmado no rate card de voz da própria Telnyx** (Mission Control Portal → Pricing, ou `telnyx.com/pricing/voice`) antes de fechar qualquer preço final. Como referência de mercado (mesma classe de produto, mesmo país, fornecedor comparável — Plivo), os valores praticados são: fixo em grandes centros ~US$0,021/min, fixo demais localidades ~US$0,033/min, móvel ~US$0,098/min.

**Cenário 1 — Para uso próprio (Fase 0, validação, sem revenda):**

| Item | Custo mensal |
|---|---|
| Aluguel do número (confirmado) | US$ 1,00 (≈ R$ 5,50) |
| Minutos de teste (baixo volume, ~20–50 min/mês, tarifa blended ~US$0,04/min) | US$ 1 – 2 (≈ R$ 5,50 – 11) |
| **Total estimado — uso próprio** | **≈ US$ 2 – 3/mês (≈ R$ 11 – 17/mês)** |

Ou seja: validar a Fase 0 tecnicamente custa na prática **menos de R$ 20/mês** por número de teste — bem abaixo do CAPEX já reservado para isso.

**Cenário 2 — Para revenda (repassando a um cliente final):**

| Item | Custo mensal (pago à Telnyx) |
|---|---|
| Aluguel do número (confirmado) | US$ 1,00 (≈ R$ 5,50) |
| Minutos inclusos no plano revendido (ex.: 100 min/mês, tarifa blended ~US$0,04/min) | US$ 4,00 (≈ R$ 22) |
| **Custo variável total por número revendido** | **≈ US$ 5,00/mês (≈ R$ 27,50/mês)** |

Isso confirma a ponta inferior da faixa já estimada (R$ 25–45) — com o dado real do aluguel, o custo variável tende para **~R$ 27–35/mês** em planos com até ~100–150 min inclusos, deixando a margem de contribuição da seção 6.3 (ARPU R$75 − custo R$33 ≈ R$42) como estimativa ainda válida, possivelmente conservadora.

> **Ação pendente:** confirmar a tarifa de voz exata da Telnyx para o Brasil (fixo/móvel, local/DDD) no Mission Control Portal antes de fechar a tabela de preços definitiva — os valores de Plivo acima são só benchmark de mercado, não o rate card da Telnyx.

Preço de venda sugerido (benchmark de mercado BR para número virtual/ramal em nuvem, R$49–149/mês):

| Plano | Preço sugerido | Inclui |
|---|---|---|
| Básico | R$ 49/mês | 1 número + ~100 min |
| Profissional | R$ 89/mês | 1 número + ~300 min + URA simples |
| Avançado/0800 | R$ 149/mês | número especial + minutagem maior + recursos extras |

Com um mix ponderado de planos, ARPU médio estimado ≈ **R$ 75/mês**, custo variável médio ≈ **R$ 33/mês** → **margem de contribuição ≈ R$ 42/mês por cliente (≈ 56%)**.

### 6.4 Ponto de equilíbrio (break-even)

Fórmula: **nº de clientes ativos para break-even = custos fixos mensais ÷ margem de contribuição por cliente**

| Cenário de custo fixo | Margem de contribuição | Clientes ativos p/ break-even | Receita mensal no break-even |
|---|---|---|---|
| Enxuto (~R$ 3.750/mês) | Conservadora (R$ 24/mês) | ≈ 156 clientes | ≈ R$ 9.200/mês |
| Enxuto (~R$ 3.750/mês) | Base (R$ 42/mês) | ≈ 89 clientes | ≈ R$ 6.700/mês |
| Enxuto (~R$ 3.750/mês) | Otimista (R$ 67/mês) | ≈ 56 clientes | ≈ R$ 5.300/mês |
| Estruturado (~R$ 9.000/mês) | Conservadora (R$ 24/mês) | ≈ 375 clientes | ≈ R$ 22.100/mês |
| Estruturado (~R$ 9.000/mês) | Base (R$ 42/mês) | ≈ 214 clientes | ≈ R$ 16.000/mês |
| Estruturado (~R$ 9.000/mês) | Otimista (R$ 67/mês) | ≈ 134 clientes | ≈ R$ 12.700/mês |

**Leitura prática:**
- No cenário mais enxuto possível (fundador solo, operação bem negociada), a FOX Telecom precisaria de **~90 a 160 clientes ativos** pagando um número/ramal para cobrir o custo fixo mensal.
- Isso é um volume plausível para 6–12 meses de operação com aquisição de 10–20 clientes/mês — mas essa velocidade de vendas não foi modelada aqui (depende de canal de aquisição e CAC reais).
- A alavanca mais forte para antecipar o break-even não é reduzir custo fixo, e sim **melhorar a margem de contribuição** (negociar atacado de verdade com o fornecedor, em vez de preço de varejo/self-service) — sair de R$24 para R$42 de margem por cliente já reduz o break-even em ~45%.

### 6.5 Próximo passo recomendado

Antes de comprometer capital: validar com 2–3 fornecedores (ex.: Zenvia, Telnyx/Plivo em volume, Algar Telecom) o preço real de atacado por número e por minuto nesse volume-alvo (ex.: 100–300 números), e refazer esta tabela com os números de cotação em vez das estimativas de varejo.

## 7. Fontes

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
- [Telnyx – Can I resell your services?](https://support.telnyx.com/en/articles/1130655-can-i-resell-your-services)
- [Telnyx – Channel Reseller Program](https://support.telnyx.com/en/articles/8288757-channel-partner-reseller-program)
- [Plivo – Supplemental Terms (WhatsApp)](https://www.plivo.com/legal/supplemental/)
- [Plivo – Acceptable Use Policy](https://plivo.com/aup)
- [Plivo – A2P guidelines to work with ISVs](https://support.plivo.com/hc/en-us/articles/45508322658073-A2P-guidelines-by-Plivo-to-work-with-ISVs)
- [Vonage – Reseller Program](https://www.vonage.com/about-us/vonage-stories/vonage-reseller-program/)
- [Vonage – Become a Partner](https://www.vonage.com/partners/become-a-partner/)
- [Sinch – Partners](https://sinch.com/pt/partners/)
- [Zenvia – Partners](https://zenvia.com/partners/)
- [Zenvia – Partner VAR (LatAm)](https://zenvia.com/es-mx/partners/partner-var/)
- [Zenvia Blog – Zenvia Partners: o que é e por que fazer parte](https://zenvia.com/blog/zenvia-partners/)
