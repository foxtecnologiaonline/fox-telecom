# Escopo de Produto e Tecnologia — FOX Telecom (benchmark Telnyx)

> Pesquisa extraída diretamente de `telnyx.com`, `developers.telnyx.com`, `support.telnyx.com` e dos índices `llms.txt`/`pricing.md` publicados pela própria Telnyx, com o objetivo de mapear **todo o catálogo de produtos, tecnologia, modelo de precificação e portal self-service** da Telnyx, e traduzir isso em um **escopo de produto para a FOX Telecom** — uma operadora/CPaaS brasileira com a mesma lógica de negócio (infraestrutura de comunicação programável, self-service, pay-as-you-go). Complementa `docs/roteiro-lancamento.md` (fases), `docs/parcerias-revenda-numeros.md` (parceiros/custos) e `docs/fase-0-execucao.md` (execução).

## 0. Metodologia e limitações

- Fontes primárias: `telnyx.com/llms.txt`, `telnyx.com/products/llms.txt`, `telnyx.com/pricing.md`, `telnyx.com/numbers/llms.txt`, `telnyx.com/sip-trunking/llms.txt`, `telnyx.com/solutions/llms.txt`, `telnyx.com/ai/compliance.json`, `developers.telnyx.com/llms.txt`, páginas de suporte e páginas de produto individuais.
- A Telnyx publica índices otimizados para agentes de IA (`llms.txt`), o que deu acesso a uma visão estruturada do catálogo completo, mas esses índices são resumidos — detalhes de implementação (codecs exatos, PoPs, SLA numérico completo) vivem na documentação de API completa (`developers.telnyx.com`) e não foram extraídos em 100% de profundidade.
- O site institucional da Telnyx hoje (out/2026) está fortemente reposicionado para **"infraestrutura para agentes de IA em tempo real"** — a camada de telecom "clássica" (voz, SMS, números, SIP) continua sendo a base do negócio, mas a comunicação de marketing dá destaque a Voice AI Agents, Inference (LLMs) e Edge Compute. Este escopo separa claramente o que é **núcleo de telecom** (o que a FOX precisa agora) do que é **camada de IA/edge compute** (expansão futura, não bloqueante).
- Preços citados são os rate cards públicos de autosserviço (USD); não refletem necessariamente condições de atacado/parceria (ver `docs/parcerias-revenda-numeros.md`, seção 5, sobre a lacuna de preços de atacado não públicos).

---

## 1. Posicionamento e modelo de negócio da Telnyx

- **Tese central:** Telnyx é uma operadora licenciada (CLEC — *Competitive Local Exchange Carrier* — nos EUA) que é dona da própria rede, pontos de presença (PoPs), núcleo móvel (mobile core) e, mais recentemente, GPUs de inferência de IA. O discurso institucional é "nenhum hop entre o seu agente e a pessoa na linha, porque cada hop é nosso" — ou seja, a vantagem competitiva alegada é **verticalização total** (rede + compute + software em uma única plataforma), ao contrário de CPaaS que compram capacidade de terceiros e revendem com camada de software por cima.
- **Modelo de entrega:** 100% self-service via portal (Mission Control Portal) + API REST completa (tudo que existe na UI existe também via API, com os mesmos objetos, rate card e fatura) + SDKs + MCP server (Model Context Protocol) para agentes de IA operarem a conta programaticamente.
- **Modelo comercial:** pay-as-you-go sem contrato mínimo como porta de entrada (igual ao que a FOX já validou na Fase 0), com camadas superiores de volume/enterprise (seção 6).
- **Multi-tenant/revenda:** feature de "Managed Accounts" — contas-filhas com API key, saldo, forma de pagamento e fatura próprios, pensada explicitamente **"para plataformas que revendem ou separam tenants"**. É o mecanismo que uma revenda (como a FOX, em estágio avançado) usaria para dar a cada cliente/sub-revendedor uma conta isolada dentro da própria conta mestre.

---

## 2. Catálogo completo de produtos Telnyx

### 2.1 Comunicação — Voz

| Produto | O que é | Observações para a FOX |
|---|---|---|
| **Voice API / Call Control** | API programável para originar, receber, transferir, gravar e orquestrar chamadas (webhooks por evento: `call.initiated`, `call.answered`, etc.) | Núcleo do produto "central telefônica em nuvem/URA" que a FOX quer vender (ver `roteiro-lancamento.md`, Fase 3) |
| **SIP Trunking** | Tronco SIP clássico para conectar PBX/URA do cliente à rede pública, outbound/inbound | Produto mais próximo do "revenda de linha" tradicional — baixa fricção de adoção para PME que já tem PBX |
| **Elastic SIP Trunking** | Tronco SIP com escala automática (sem necessidade de dimensionar canais fixos) | Vantagem comercial clara para vender "sem limite de canais simultâneos" |
| **TeXML** | Linguagem de marcação (compatível com TwiML da Twilio) para construir fluxos de chamada/IVR sem precisar operar servidor próprio de webhook | Equivalente a um "no-code call flow" — a Telnyx tem até um `TeXML Bin` no portal para quem não é dev |
| **WebRTC** | SDK para chamadas de voz/vídeo direto no navegador/app, sem número de telefone | Relevante para um futuro "app FOX" de atendimento |
| **Trusted Calling / Branded Calling** | Exibe nome/logo da empresa que está chamando no celular do destinatário (anti-spam, selo de confiança) | Diferencial comercial relevante no Brasil, onde "golpe do número desconhecido" é problema grande |
| **Fax API** | Envio/recebimento de fax programável | Nicho (jurídico, saúde, órgão público) — baixa prioridade inicial |
| **Call Recording / Media Streaming** | Gravação de chamada e streaming de áudio em tempo real (WebSocket) para IA/transcrição | Pré-requisito técnico se a FOX quiser oferecer "atendente com IA" depois |

### 2.2 Comunicação — Mensageria

| Produto | O que é | Observações |
|---|---|---|
| **SMS / MMS API** | Envio/recebimento programável de SMS e MMS | Precisa de registro 10DLC nos EUA; no Brasil o equivalente regulatório é via operadora móvel parceira |
| **RCS Business Messaging** | Mensageria rica (rich cards, botões) via Google/Android | Baixa prioridade — adoção ainda incipiente no Brasil |
| **WhatsApp Business API** | Integração oficial com a Meta para WhatsApp Business | **Alta prioridade no Brasil** — é o canal de atendimento dominante; a FOX deveria priorizar isso antes de RCS |
| **Email API** | Envio de e-mail transacional (não é marketing/blast — a própria Telnyx declara isso como limitação em `llms.txt`) | Complementar, baixo esforço de integração |
| **Short code / Alphanumeric Sender ID / 10DLC** | Infraestrutura regulatória de mensageria em massa (EUA) | Não se aplica direto ao Brasil — aqui o equivalente é cadastro de remetente junto às operadoras móveis |

### 2.3 Números

| Produto | O que é | Observações Brasil (confirmado via `support.telnyx.com`) |
|---|---|---|
| **Global Phone Numbers** | Números locais, móveis, toll-free, short code em 40+ países | Brasil: números locais/móveis e nacionais (3003/4004) disponíveis |
| **Number Porting (port-in/port-out)** | Portabilidade numérica | Processo e prazos variam por país; não detalhado para Brasil nas páginas públicas |
| **Regulatory Bundles / Documents** | Gestão de documentação regulatória por número/país | **Brasil local/móvel exige:** nome completo + CPF + cópia de identidade/passaporte (pessoa física) **ou** nome do representante + CNPJ + Cartão CNPJ (pessoa jurídica); comprovante de endereço brasileiro emitido nos últimos 3 meses. **Brasil toll-free/nacional (3003/4004) exige adicionalmente:** procuração (Power of Attorney, modelo fornecido pela própria Telnyx), certificado de registro da empresa, documento do representante. **Prazo de aprovação: até 3 dias úteis.** |
| **Number Lookup API** | Consulta de titularidade/tipo de linha (CNAM, line type, portabilidade) | Útil para antifraude e qualificação de leads |
| **Number Reputation** | Monitoramento de reputação do número (evitar marcação como spam) | Relevante dado o problema de "spam calls" no Brasil |

### 2.4 Identidade e confiança

| Produto | O que é |
|---|---|
| **Verify API** | Envio e validação de OTP (código de verificação) por SMS/voz/e-mail — base de qualquer login/2FA |
| **Branded Calling** | Ver seção 2.1 |
| **Deepfake Detection** | Detecção de voz sintética/deepfake em chamadas — produto novo 2025/2026, ligado à onda de fraude por IA generativa |
| **Number Reputation** | Ver seção 2.3 |

### 2.5 Wireless / IoT

| Produto | O que é | Observações |
|---|---|---|
| **IoT SIM Cards / eSIM** | Chips e eSIMs para conectividade celular de dispositivos (M2M/IoT) | Verticais: frotas, rastreadores, medidores — mercado relevante e pouco explorado no Brasil fora dos grandes M2M players |
| **Private Wireless Gateways** | Gateways para rede celular privada (ex.: dentro de uma fábrica) | Nicho avançado, não prioritário no curto prazo |
| **Mobile Voice / VoLTE / Wireless Data** | Voz e dados móveis sobre a infraestrutura wireless própria da Telnyx | Pressupõe acordo com operadora móvel (MVNO) — alinhado à Fase 4 do roteiro da FOX, não à Fase 1 |

### 2.6 Rede (Network)

| Produto | O que é |
|---|---|
| **Virtual Cross Connect** | Conexão privada direta para nuvens públicas (AWS/GCP/Azure) sem passar pela internet pública |
| **Cloud VPN / WireGuard Interfaces** | VPN gerenciada ponto a ponto |
| **Global IP / Global Edge Router** | Roteamento IP global próprio |

> Esta camada é infraestrutura de backbone — fora do escopo de produto da FOX nas Fases 0–3 (depende de ser operadora com rede própria). Relevante só na Fase 4 (outorga própria/MVNO).

### 2.7 Edge Compute & Storage

| Produto | O que é |
|---|---|
| **Functions** | Execução de código (containers) nos pontos de presença da rede (edge computing) |
| **StatefulActor** | Instância persistente por entidade (ex.: 1 "ator" por chamada/sessão/usuário) — padrão de arquitetura para orquestrar IA em tempo real |
| **Object Storage, KV, SQLDB, CloudFS** | Primitivas de armazenamento (S3-like, key-value, banco SQL, filesystem em nuvem) |

> Esta é a camada mais "cloud provider" e menos "telecom clássica" da Telnyx — reflete o pivô para infraestrutura de agentes de IA. **Não é prioridade para o MVP da FOX**, mas é relevante entender porque mostra para onde o mercado está indo (ver seção 7).

### 2.8 IA (camada de maior investimento atual da Telnyx)

| Produto | O que é |
|---|---|
| **Inference API** | Serving de LLMs open-weight e customizados (catálogo: GLM, DeepSeek, Kimi, MiniMax, Qwen, Gemma, modelos próprios), com interface compatível com a API da OpenAI |
| **Dedicated Inference / GPU capacity** | GPU reservada para modelos próprios/fine-tuned |
| **Voice AI Agents** | Agente de voz com IA de ponta a ponta (SIP + STT + LLM + TTS) cobrado como pacote único — **US$ 0,05/min all-in** |
| **Text-to-Speech / Speech-to-Text** | APIs de voz sintética e transcrição, com múltiplos provedores plugáveis (própria Telnyx, Amazon Polly, Azure, ElevenLabs via BYO key, Deepgram, etc.) |
| **Agent SDK / Assistants / Agent Tools (Web Search, AI Search, Meeting Bot, Agent Memory)** | Framework para construir agentes com memória persistente, tarefas agendadas e integrações de comunicação |
| **Embeddings API / AI Gateway** | Geração de embeddings e um gateway unificado para múltiplos provedores de IA |

> **Leitura estratégica:** a Telnyx está claramente apostando que o próximo ciclo de CPaaS é "infraestrutura para atendimento automatizado por IA" (voicebots, chatbots com voz, agentes autônomos), não só "canal de comunicação". Isso é um sinal de **para onde a FOX deveria evoluir o roadmap de produto depois da Fase 1–2** (atendimento automatizado por IA sobre a própria base de números/voz, não só revenda de canal).

### 2.9 Plataforma de desenvolvedor

- **API REST completa** (OpenAPI 3 spec pública no GitHub `team-telnyx/openapi`), com webhooks assinados, rate limiting documentado, retries de comando.
- **Mission Control Portal**: dashboard self-service — compra/portabilidade de número, configuração de SIP trunk (autenticação por IP/FQDN/credenciais, múltiplos IPs de failover, escolha de transporte UDP/TCP/TLS e codec, "AnchorSite" para fixar mídia em um PoP), construtor de fluxo de chamada sem código (TeXML Bin), relatórios de uso, assistente de IA de suporte embutido no próprio portal, pagamentos agendados.
- **Managed Accounts (sub-contas)**: contas-filhas com API key/saldo/forma de pagamento/fatura próprios — mecanismo de revenda/multi-tenant.
- **Ferramentas de IA para devs**: servidor MCP remoto, CLI oficial, "agent skills" publicados em repositório próprio no GitHub, permitindo que agentes de IA configurem a conta Telnyx de ponta a ponta sem humano no portal.
- **Controles de segurança**: escopo de permissão por API key, allowlist de IP por conexão, limites de gasto e bloqueio de destino (antifraude), log de auditoria de toda ação (portal ou API).

---

## 3. Modelo de precificação (referência de autosserviço, USD)

| Categoria | Faixa de preço (varejo/self-service) |
|---|---|
| SIP Trunking outbound / inbound | a partir de US$ 0,005/min / US$ 0,0032/min |
| Voice API (taxa de plataforma, soma-se ao SIP) | US$ 0,002/min |
| Gravação de chamada | US$ 0,002/min |
| Streaming de mídia (WebSocket) | US$ 0,0035/min |
| SMS/MMS outbound | a partir de US$ 0,004/mensagem (+ taxas de carrier/registro nos EUA) |
| Fax | US$ 0,007/página |
| Número local (EUA, referência) | US$ 1,00/mês (desconto de volume a partir de US$ 0,79/mês) |
| Número toll-free | a partir de US$ 1,00/mês (+ taxa única de US$ 500 e US$ 40/mês após 12 meses em alguns planos) |
| Consulta Number Lookup | a partir de US$ 0,0015/consulta |
| IoT SIM (dados) | a partir de US$ 0,01/MB |
| Voice AI Agent (pacote completo) | US$ 0,05/min |
| Text-to-Speech | US$ 0,000006 a US$ 0,00005/caractere, conforme provedor/qualidade |
| Speech-to-Text | US$ 0,0015 a US$ 0,027/min, conforme provedor |
| Inference (LLM, por 1M tokens) | ~US$ 0,10–US$ 4,40, conforme modelo (input/output) |

**Planos:**

| Plano | Mínimo mensal | Benefícios |
|---|---|---|
| Pay-as-you-go | Nenhum | Todos os produtos, suporte via comunidade, rate limit padrão (SMS 50/s, voz 500 chamadas simultâneas, API 100 req/s) |
| Committed | US$ 500/mês | Desconto por volume, gerente de conta dedicado, suporte prioritário, rate limit maior, SLA customizado |
| Enterprise | US$ 5.000/mês | Preço customizado, infraestrutura dedicada, suporte 24/7 premium, rate limit ilimitado, SLA com créditos, IP dedicado, interconexão de rede privada |

> Este é exatamente o modelo de "escada de maturidade" que a FOX já está seguindo organicamente no `roteiro-lancamento.md` (Fase 0 pay-as-you-go → Fase 2/3 negociação de atacado/volume → Fase 4 infraestrutura própria). Vale adotar a mesma estrutura de 3 camadas comercialmente (varejo self-service / contrato com volume mínimo / enterprise) desde já, mesmo operando como revenda.

---

## 4. Certificações e compliance declarados pela Telnyx

| Certificação/padrão | Status | Cobertura |
|---|---|---|
| SOC 2 Type I e II | Ativo | Voz programável, mensageria, vídeo, wireless |
| HIPAA | Ativo (BAA disponível) | Voz, mensageria, fax, inferência de IA |
| GDPR | Ativo (DPA + residência de dados UE) | Dados de clientes da UE |
| ISO/IEC 27001:2022 | Ativo | Sistema de gestão de segurança da informação |
| ISO/IEC 27701:2019 | Ativo | Gestão de privacidade |
| PCI DSS | Ativo | Processamento de cartão para billing |
| STIR/SHAKEN | Ativo, atestação nível A | Toda chamada de voz originada |
| A2P 10DLC | Ativo | Mensageria EUA, registro direto como carrier |
| FedRAMP | Em andamento (previsão 2026) | Setor público EUA |

**Leitura para o Brasil:** nenhuma dessas certificações substitui exigência regulatória brasileira (ANATEL, LGPD). A FOX deve tratar isso como benchmark de **maturidade de segurança/compliance a perseguir** (ISO 27001 é um objetivo de médio prazo realista e usado como diferencial em licitações — ver `roteiro-lancamento.md`, Fase 2/3), não como suficiente para operar no Brasil.

---

## 5. Soluções/verticais de uso divulgadas

- Saúde: confirmação automática de consultas (remarcar/cancelar em tempo real).
- Finanças: agentes de voz com IA para atendimento, verificação de identidade e alertas, com foco em compliance.
- Varejo/e-commerce: agentes de IA para devolução, rastreio de pedido e reembolso 24/7.
- Viagens/hospitalidade: suporte de reserva 24/7.
- Casos de uso transversais citados: agente de voz com IA, atendimento omnichannel, contact center, "frota conectada" (SIMs + núcleo móvel + inferência na borda), notificações globais, inferência de IA como produto autônomo (ex.: "pay-per-call" via protocolo x402/crypto — nicho experimental, não relevante para o Brasil agora).

---

## 6. Escopo de produto recomendado para a FOX Telecom, por fase

Mapeado contra as fases já definidas em `docs/roteiro-lancamento.md`.

### Fase 0–1 (agora): núcleo de telecom via revenda
Replicar como **produto vendável**, operando sobre a camada CPaaS de um fornecedor (Telnyx/Plivo/Zenvia):
- [x] Número virtual (DID) local — já validado.
- [ ] Encaminhamento de chamada / central telefônica simples (Voice API/Call Control).
- [ ] URA básica sem código (equivalente ao TeXML Bin — construir um "montador de fluxo" próprio ou usar o do fornecedor via white-label, se existir).
- [ ] WhatsApp Business API — priorizar sobre RCS/SMS dado o perfil do mercado brasileiro.
- [ ] Verify API (OTP) — módulo de baixo custo e alta demanda (qualquer empresa que tenha login/cadastro).
- [ ] Gravação de chamada básica (compliance/qualidade).
- [ ] Portal do cliente FOX (mínimo): visualizar número, saldo, extrato de uso, configurar encaminhamento — ainda que simplificado, é o equivalente ao Mission Control em escala pequena.

### Fase 2–3: camada de produto própria sobre o fornecedor
- [ ] Portal self-service mais completo: compra/portabilidade de número pelo próprio cliente, configuração de SIP trunk, relatórios de uso — isso é o que gera retenção e diferencia a FOX de "só repassar a Telnyx com margem".
- [ ] Billing e faturamento Pix/boleto nativo (a Telnyx não resolve isso para o Brasil — é onde a FOX agrega valor real).
- [ ] Number Lookup / antifraude básico — útil para qualificar leads e evitar número "sujo".
- [ ] Branded Calling (CNAM/identificação de chamada) — forte diferencial comercial no combate a "chamada desconhecida" tão comum no Brasil.
- [ ] Multi-tenant/sub-contas — se a FOX quiser, nesta fase, começar a sub-revender para terceiros (parceiros regionais), replicar o conceito de "Managed Accounts".

### Fase 4 (outorga própria/MVNO): paridade de infraestrutura
- [ ] SIP Trunking/Elastic SIP Trunking com rede própria (hoje depende 100% do parceiro).
- [ ] Wireless/IoT SIM (M2M) — mercado adjacente de alto potencial, pouco explorado por provedores regionais brasileiros.
- [ ] Rede própria (PoPs, interconexão) — fora de alcance até ter outorga SCM/STFC ou acordo MVNO.

### Camada de diferenciação futura (não bloqueante, mas estratégica): IA
- [ ] Atendente com IA (voicebot) sobre a própria base de voz — réplica de "Voice AI Agents" da Telnyx, porém focado em PME brasileira (ex.: recepcionista virtual, triagem de atendimento, cobrança automatizada).
- [ ] TTS/STT em português-BR como add-on de produto (há provedores com suporte a PT-BR; validar qualidade antes de vender).

> Esta camada de IA é onde a Telnyx está investindo mais agora (seção 2.8) — é um sinal de mercado real, mas **não deve ser priorizada antes da Fase 1–2 estarem consolidadas**: a FOX ainda não tem base de clientes nem caixa para competir em infraestrutura de IA: o caminho razoável é **revender/embutir um fornecedor de voicebot (inclusive a própria Telnyx Voice AI Agents) como feature**, não construir isso do zero.

---

## 7. Lacunas e pontos para validar antes de fechar o escopo definitivo

1. **Preço de atacado real** — os valores da seção 3 são varejo/self-service; já identificado como lacuna em `docs/parcerias-revenda-numeros.md`, seção 5. Sem cotação real de volume, a margem projetada permanece estimativa.
2. **Regulatório Brasil específico por produto** — os requisitos de KYC descritos (seção 2.3) são os da Telnyx como revendedora; não substituem o enquadramento ANATEL que a própria FOX precisa seguir como "revenda sobre operadora parceira" (ver `docs/parcerias-revenda-numeros.md`, seção 2).
3. **Detalhes técnicos de SIP Trunking** (codecs suportados, PoPs, SLA numérico) não vieram completos dos índices `llms.txt` — exigem leitura da documentação de API completa (`developers.telnyx.com/docs/...`) antes de qualquer decisão de arquitetura.
4. **Termos reais do programa de revenda/white-label** — a Telnyx não publica termos de "reseller program" nem política de markup/white-label nas páginas públicas acessadas; é preciso contato comercial direto (consistente com a limitação já registrada em `docs/parcerias-revenda-numeros.md`).
5. **Precificação de Wireless/IoT, Vídeo/WebRTC e Verify** não apareceu completa na extração (arquivo de pricing foi truncado por tamanho) — revisar `telnyx.com/pricing.md` página completa ou `telnyx.com/pricing/llms.txt` se for preciso o rate card 100% completo.

---

## 8. Fontes

- [Telnyx — Homepage](https://telnyx.com)
- [Telnyx — Full LLM index](https://telnyx.com/llms.txt)
- [Telnyx — Products index](https://telnyx.com/products/llms.txt)
- [Telnyx — Numbers index](https://telnyx.com/numbers/llms.txt)
- [Telnyx — SIP Trunking index](https://telnyx.com/sip-trunking/llms.txt)
- [Telnyx — Solutions index](https://telnyx.com/solutions/llms.txt)
- [Telnyx — Pricing (markdown)](https://telnyx.com/pricing.md)
- [Telnyx — Compliance (JSON)](https://telnyx.com/ai/compliance.json)
- [Telnyx — Getting started runbook](https://telnyx.com/getting-started.md)
- [Telnyx Developers — Full LLM index](https://developers.telnyx.com/llms.txt)
- [Telnyx Support — Brazil DID requirements](https://support.telnyx.com/en/articles/5464041-brazil-did-requirements)
- [Telnyx — Demo: how resellers leverage Mission Control](https://telnyx.com/resources/demo-how-resellers-leverage-mission-control)
- [Telnyx — Use case: embedded number search & provisioning](https://telnyx.com/use-cases/embedded-number-search-provisioning)
- [Telnyx OpenAPI Specification (GitHub)](https://github.com/team-telnyx/openapi)
- Ver também fontes já listadas em `docs/parcerias-revenda-numeros.md` e `docs/roteiro-lancamento.md`.
