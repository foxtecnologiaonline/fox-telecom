# Estruturação da Parceria com a Algar Telecom — FOX Telecom

> Aprofunda a seção 3.3 de `docs/parcerias-revenda-numeros.md` (candidatos a parceiro) especificamente para a Algar. Objetivo: responder "o que fazer, onde entrar, o que podemos oferecer" com o que existe de público sobre o programa da Algar, e cruzar isso com o estágio real da FOX Telecom (Fase 0, por `docs/roteiro-lancamento.md`).

## 1. A Algar tem dois programas de parceria distintos — não um só

A pesquisa encontrou dois modelos com públicos-alvo e portas de entrada completamente diferentes. Confundir os dois é o erro mais fácil de cometer aqui.

### 1.1 Franquia para provedores regionais (ISPs) — o modelo "inédito" de set/2025

- Lançado em setembro de 2025, formalizado e expandido ao longo do ano: já são **34 franqueados em mais de 100 cidades** (incluindo Brasília, Goiânia, São Paulo/Itaquera), e a Algar afirma que o modelo já responde por **~12% da receita total da companhia** (dado de uma única fonte, não confirmado em outra).
- **Perfil de alvo explícito:** provedor regional (ISP) de médio porte, com **mais de 7 mil clientes** e ticket médio de ~R$100 — ou seja, **faturamento mínimo de referência ≈ R$700 mil/mês**. Isso é operação de banda larga fixa com base instalada, não revenda de numeração.
- **Divisão de papéis:** a Algar assume backbone, data centers, monitoramento de rede 24/7, faturamento, segurança e ampliação de portfólio. O franqueado local foca em expansão de rede, vendas e atendimento ao cliente — mantendo o fundador na frente da operação local.
- A própria Algar descreve o modelo como **gestão compartilhada**, explicitamente diferente de uma aquisição ou de um acordo comercial simples.

**Conclusão:** este é o modelo mais "forte" e mais citado, mas o perfil de entrada (7k+ clientes, R$700k+/mês, rede de banda larga própria) está muito acima do estágio atual da FOX (Fase 0 — autoconsumo, revenda de numeração via CPaaS). Não é a porta de entrada de agora; é um horizonte de **Fase 4** (outorga própria/escala), e mesmo assim só se a FOX decidir migrar de "revenda de números" para "operador de banda larga regional" — são negócios diferentes.

### 1.2 Canal de afiliados / revenda de Cloud Phone Pro (URA, PABX em nuvem) — modelo de 2020

- Em 2020 a Algar lançou um **programa de marketing de afiliados** aberto a autônomos e empresas para vender soluções de TI/telecom ao mercado empresarial, com **comissão recorrente de 25%** e capacitação para os afiliados.
- O produto citado especificamente é o **Cloud Phone / Cloud Phone Pro**: ramais físicos e virtuais, PABX em nuvem, URA, discador automático, gravação — ou seja, exatamente a categoria de produto que a FOX já está validando na Fase 0/1 (número virtual + URA + ramal em nuvem).
- **Lacuna importante:** não há confirmação pública de que esse programa ainda está ativo em 2026 nem de como ele está estruturado hoje (requisitos, comissão atual, contrato). A fonte é de 2020; o foco de comunicação recente da Algar está todo no modelo de franquia de ISPs (seção 1.1). É preciso validar diretamente com a Algar se o canal de afiliados ainda existe e em que condições.

**Conclusão:** se ainda ativo, este é o encaixe mais realista para o estágio atual da FOX — ela entraria como **revendedor/afiliado de um produto de PABX/URA/ramal em nuvem já outorgado e com suporte nacional da Algar**, em vez de (ou além de) montar a própria pilha sobre Telnyx/Zenvia. Precisa ser confirmado antes de qualquer planejamento em cima dele.

## 2. Diagnóstico de encaixe: onde a FOX está x onde a Algar quer parceiros

| Dimensão | Franquia ISP (1.1) | Afiliado Cloud Phone (1.2) | Estágio atual da FOX |
|---|---|---|---|
| Base de clientes exigida | 7.000+ | Não divulgada (modelo de comissão, não de porte mínimo) | 0–poucas dezenas (Fase 0/1) |
| Faturamento mínimo implícito | ~R$700 mil/mês | Nenhum conhecido | Pré-receita a ~R$5–20 mil/mês |
| Tipo de ativo exigido | Rede de banda larga própria, CNPJ formalizado, operação local madura | CNPJ, capacidade de vendas/distribuição | CNPJ simples (MEI/ME), em formalização |
| Relação com a Algar | Gestão compartilhada / franquia | Comissionamento sobre revenda | — |
| Compatível com o modelo "revenda de numeração" da FOX? | Não — é outro negócio (ISP de banda larga) | Sim — é o mesmo tipo de produto (URA/PABX/ramal) | — |

**Leitura honesta:** hoje, a FOX não se qualifica para o programa mais visível e mais forte da Algar (1.1). O caminho de entrada realista é testar se o canal de afiliados (1.2) ainda existe — e, se não existir mais nesse formato, tratar a Algar por ora como **parceiro de atacado/CPaaS a cotar** (como já está na seção 3.3 do doc de parcerias) em vez de como "programa de parceria formal" já aberto para o porte da FOX.

## 3. Onde entrar — plano de ação concreto

1. **Identificar o canal de contato comercial certo.** Não há, nas fontes públicas levantadas, um formulário ou e-mail de "parceria/revenda" documentado. Os dois caminhos mais diretos:
   - Site institucional da Algar Telecom (`algartelecom.com.br`) → seção Empresas/Parceiros → formulário de contato comercial, mencionando explicitamente interesse no "programa de afiliados Cloud Phone" e, separadamente, perguntando sobre o "modelo de parcerias com provedores" (para mapear o caminho futuro, mesmo sem se qualificar agora).
   - LinkedIn: a área de franquias é liderada por **Ana Flávia Martins** (diretora executiva de franquias, citada na cobertura de set/2025); a área comercial de SP teve troca de diretoria recente (jun/2026). Contato via LinkedIn para a área de franquias/parcerias tende a ser mais rápido que formulário genérico — mas use para abrir conversa, não para assinar nada.
2. **Perguntas a fazer no primeiro contato** (roteiro sugerido):
   - O programa de afiliados/revenda do Cloud Phone Pro (URA, PABX em nuvem, ramal virtual) ainda está ativo? Se sim: requisitos de entrada, comissão atual, modelo de contrato, SLA de suporte, exclusividade territorial/setorial.
   - Existe algum modelo de parceria comercial para numeração/CPaaS (voz/SMS) para empresas que ainda não atingem o perfil de franquia de ISP (7k+ clientes)?
   - Qual o canal correto para revisitar o tema quando a FOX atingir escala compatível com o modelo de franquia?
3. **Due diligence antes de assinar qualquer coisa** (reaproveitando a seção 2 de `docs/parcerias-revenda-numeros.md`):
   - Validar com advogado especializado em telecom a cláusula de responsabilidade pela prestação do serviço (quem responde pela qualidade/outorga: Algar, sempre).
   - Checar exclusividade (a Algar pode exigir que o afiliado não revenda produto concorrente na mesma categoria).
   - Checar se a comissão é sobre receita bruta ou líquida, e se há metas mínimas de venda para manter o status de afiliado.
4. **Não bloquear a Fase 0/1 esperando resposta da Algar.** Como já registrado em `docs/fase-0-execucao.md`, a Telnyx já está confirmada como fornecedor funcional e barato. Trate o contato com a Algar como uma frente paralela de **pesquisa de parceiro de atacado** (igual Zenvia), não como pré-requisito para validar o MVP.

## 4. O que a FOX pode oferecer à Algar

Como a FOX ainda não tem base de clientes relevante, a proposta de valor não pode ser "volume" — precisa ser outra coisa. Candidatas realistas, do mais forte ao mais fraco:

1. **Canal de vendas digital-first para um nicho ainda não coberto.** A Algar já tem 34 franqueados regionais (banda larga) e um canal de afiliados generalista (se ainda ativo). A FOX pode se posicionar como um canal 100% digital/self-service para numeração virtual e PABX em nuvem voltado a um nicho específico (ex.: PMEs de serviços, profissionais liberais, e-commerce) que hoje é atendido por "fale com um consultor" (como a própria Zenvia) — ou seja, oferecer **velocidade e experiência de compra online** que os canais tradicionais da Algar não têm hoje.
2. **Validação e geração de leads de baixo custo de aquisição.** Ofereça à Algar dados de tração real (mesmo pequenos): CAC, conversão, churn, ARPU validados na Fase 1 — isso é o que falta para a Algar avaliar expandir o canal de afiliados/parceiros para operações menores que 7k clientes.
3. **Atestados técnicos e histórico para o funil de licitações.** Se a FOX formalizar uma carta de respaldo técnico ou atestado conjunto com a Algar (como já previsto na Fase 2 do roteiro de lançamento), isso é valor mútuo: a Algar expande presença em licitações municipais/estaduais via um parceiro mais ágil para processos pequenos, e a FOX ganha lastro regulatório.
4. **Opcional/futuro:** se a FOX decidir migrar para o modelo de ISP de banda larga (fora do escopo atual de "revenda de numeração"), o próprio crescimento até 7k+ clientes é o que destrava o programa de franquia — mas isso é uma mudança de modelo de negócio, não um ajuste de parceria.

## 5. Estrutura de parceria recomendada, por fase

| Fase (ver `docs/roteiro-lancamento.md`) | Relação com a Algar |
|---|---|
| 0–1 (atual: autoconsumo → primeiros clientes) | Contato exploratório: confirmar se o canal de afiliados Cloud Phone ainda existe; se sim, avaliar rodar em paralelo à Telnyx como segunda opção de fornecedor "cara nacional" (como já cogitado para a Zenvia). Não depender disso para lançar. |
| 2 (formalização) | Se o canal de afiliados for viável, formalizar contrato de revenda + buscar carta de respaldo técnico da Algar para fortalecer atestado de capacidade técnica. |
| 3 (licitações pequenas/médias) | Usar a carta de respaldo/consórcio com a Algar (se obtida) para disputar editais que exigem outorga STFC/SMP — ver o ponto crítico já mapeado na seção 3 de `docs/roteiro-lancamento.md` sobre subcontratação limitada. |
| 4 (escala/outorga própria ou MVNO) | Só aqui o modelo de franquia de ISP (seção 1.1) entra como opção real — e apenas se a FOX tiver pivotado para operação de banda larga com base de clientes própria compatível com o perfil exigido (7k+ clientes). |

## 6. Riscos e pontos de atenção

- **Risco de mal-entendido de programa:** se o primeiro contato comercial for direcionado automaticamente para a área de franquias de ISP, a resposta provável é "não se qualifica" — por isso vale nomear explicitamente o interesse no canal de afiliados/Cloud Phone no primeiro contato, para não ser descartado antes de chegar à área certa.
- **Dependência de informação não confirmada:** tudo na seção 1.2 é de 2020 e pode estar descontinuado. Trate como hipótese a validar, não como programa garantido.
- **Duas camadas de dependência:** como já alertado no doc de parcerias, qualquer revenda sobre outorga de terceiro (Algar incluída) deixa a FOX sem controle direto sobre a qualidade do serviço de telecom em si — isso deve estar claro no contrato e na comunicação com o cliente final.

## 7. Próximos passos imediatos

1. Abrir contato comercial com a Algar (site institucional + LinkedIn da área de franquias) perguntando especificamente sobre o canal de afiliados do Cloud Phone Pro.
2. Em paralelo, continuar a Fase 0 com a Telnyx sem esperar resposta (já confirmada e funcionando).
3. Registrar a resposta da Algar (ativo/descontinuado, condições) e atualizar este documento e a seção 3.3 de `docs/parcerias-revenda-numeros.md` com o dado real.
4. Guardar o modelo de franquia de ISP (seção 1.1) como marco de Fase 4 — revisitar quando a base de clientes se aproximar de uma escala relevante.

## 8. Fontes

- [Teletime – Algar apresenta modelo inédito para provedores expandirem seu negócio (23/09/2025)](https://teletime.com.br/23/09/2025/algar-apresenta-modelo-inedito-para-provedores-expandirem-seu-negocio/)
- [Teletime – Algar, modelo de parcerias com provedores (08/12/2025)](https://teletime.com.br/08/12/2025/algar-modelo-parcerias-provedores/)
- [Teletime – Algar Telecom Franquias: modelo pioneiro no país oferece operação de ponta a ponta para provedores (01/04/2025)](https://teletime.com.br/01/04/2025/algar-telecom-franquias-modelo-pioneiro-no-pais-oferece-operacao-de-ponta-a-ponta-para-provedores/)
- [Minha Operadora – Algar adquire 645 mil clientes através do sistema de franquias](https://www.minhaoperadora.com.br/?p=118823)
- [Teletime – Algar cria programa de marketing de afiliados para atendimento de PMEs (08/07/2020)](https://teletime.com.br/08/07/2020/algar-cria-programa-de-marketing-de-afiliados-para-atendimento-de-pmes/)
- [Baguete – Algar Telecom aposta em marketing de afiliados](https://www.baguete.com.br/noticias/algar-telecom-aposta-em-marketing-de-afiliados)
- [Baguete – Algar aposta em franquias](https://baguete.com.br/public/noticias/algar-aposta-em-franquias)
- Ver também `docs/parcerias-revenda-numeros.md` (seção 3.3) e `docs/roteiro-lancamento.md` (seção de licitações, sobre limites de subcontratação em telefonia).
