# Fase 0 — Execução (Estrutura para autoconsumo/validação)

> Runbook operacional da Fase 0 do `docs/roteiro-lancamento.md`. Pressupõe que o CNPJ já está aberto — portanto o foco aqui é só: escolher fornecedor(es), abrir cadastro, comprar números de teste e validar o fluxo fim a fim.

## 1. Fornecedores para abrir cadastro agora

Recomendação: abrir cadastro em **2 fornecedores em paralelo** (não custa nada além de tempo, já que são self-service sem contrato mínimo) para comparar preço, qualidade de voz e facilidade de KYC antes de escolher o principal.

| Prioridade | Fornecedor | Por que | Link oficial | Verificação exigida |
|---|---|---|---|---|
| 1 ✅ **confirmado** | **Telnyx** | Mais barato (DID BR **confirmado em US$1,00/mês**), portal self-service maduro (Mission Control), boa documentação de API — use este como fornecedor principal da Fase 0 | Cadastro: [telnyx.com/sign-up](https://telnyx.com/sign-up) · Portal após cadastro: [portal.telnyx.com](https://portal.telnyx.com) | E-mail corporativo (ou login via Google/Microsoft), confirmação de e-mail, celular válido; alguns cadastros passam por KYC adicional pedindo CNPJ/documento societário |
| 2 ⚠️ **sem self-service claro** | **Zenvia** (ex-TotalVoice) | Empresa brasileira, suporte em português — mas o fluxo de cadastro/compra de número **não é um self-service óbvio**: historicamente é vendido via time comercial ("fale com consultor"), e a documentação técnica ainda vive no domínio legado `totalvoice.com.br/doc`. Não foi possível localizar uma página de cadastro direta nem confirmar se hoje existe compra de número 100% self-service | [zenvia.com](https://zenvia.com) → menu "Voz"; se não encontrar fluxo de autocadastro, usar a opção "Fale com um consultor" | Aceite dos Termos de Serviço da Plataforma de Voz no cadastro |
| 3 (opcional, comparação) | **Plivo** | Preço competitivo (DID ~US$5/mês), bom para comparar custo com Telnyx | [plivo.com](https://plivo.com) → "Sign Up" | E-mail corporativo obrigatório (domínios pessoais como Gmail/Hotmail são recusados), verificação por celular, **não usar VPN** durante o cadastro |

> **Decisão prática:** como a Telnyx já está confirmada e funcionando (self-service, preço validado), siga a Fase 0 com ela como fornecedor principal agora. Trate a Zenvia como item de comparação futura — abra contato comercial em paralelo, sem bloquear o andamento da Fase 0 esperando resposta deles.
>
> Não guardei um link profundo de cadastro para Plivo porque não encontrei a URL exata documentada publicamente — use o link do domínio principal e navegue pelo menu ("Sign Up"), em vez de um link adivinhado.

## 2. Documentos para ter em mãos (você já tem o CNPJ — falta reunir o resto)

- [ ] Cartão CNPJ / comprovante de inscrição (já emitido junto com o CNPJ)
- [ ] Contrato social ou documento de constituição da empresa
- [ ] RG/CPF do responsável legal (sócio-administrador)
- [ ] Comprovante de endereço da empresa (conta de luz/água/telefone em nome do CNPJ, ou contrato de locação)
- [ ] E-mail corporativo (evitar @gmail/@hotmail pessoal nos cadastros que pedem domínio corporativo — se ainda não tiver, criar um e-mail no domínio da FOX Telecom antes de cadastrar)
- [ ] Telefone celular válido para verificação por SMS/chamada
- [ ] Cartão de crédito corporativo ou meio de pagamento internacional (Telnyx/Plivo cobram em USD via cartão; Zenvia tende a aceitar faturamento nacional)

## 3. Plano de execução otimizado (caminho crítico)

O item que mais demora é a aprovação de KYC da Telnyx (até 3 dias úteis) — por isso ele deve ser **disparado primeiro**, e tudo que não depende dele roda em paralelo enquanto se aguarda. Essa é a otimização principal do plano: nenhuma etapa fica esperando à toa.

| Quando | Bloco | Tarefas | Depende de |
|---|---|---|---|
| **Dia 0 (hoje, ~1h)** | Disparar o item de maior lead time | 1) Criar e-mail corporativo, se não tiver. 2) Iniciar cadastro na Telnyx (`telnyx.com/sign-up`) e enviar documentos de KYC (CNPJ, contrato social, RG/CPF) assim que solicitado. | Documentos da seção 2 prontos |
| **Dia 0 (em paralelo, ~30min)** | Preparar o ambiente técnico | 1) Clonar/baixar os scripts de `scripts/fase0/` (seção 5). 2) Conferir que o Python 3 está instalado. 3) Deixar o `.env` pronto para colar a API key assim que ela existir. | Nada — não depende da aprovação |
| **Dia 0 (em paralelo, ~15min)** | Abrir contato com fornecedores de comparação | 1) Mandar mensagem comercial para a Zenvia ("Fale com um consultor"). 2) Criar cadastro na Plivo só para cotação. | Nada |
| **Dia 1–3 (enquanto aguarda aprovação)** | Sem ação bloqueante | Acompanhar e-mail da Telnyx; se pedirem documento adicional, responder no mesmo dia para não perder posição na fila. | — |
| **Dia da aprovação (~1h)** | Validação técnica via script | 1) Gerar API key no Mission Control Portal. 2) Rodar `check_balance.py`. 3) Adicionar crédito/cartão se saldo zerado. 4) Rodar `search_numbers.py` e escolher 1–3 números. 5) Rodar `buy_number.py --confirm`. | Cadastro aprovado + API key gerada |
| **Mesmo dia (~30min)** | Validação de uso real | 1) No portal (UI), configurar encaminhamento simples do número comprado para seu celular. 2) Fazer uma ligação de teste real e avaliar áudio. 3) Rodar `check_balance.py` antes/depois da ligação para calcular o custo real por minuto. | Número comprado |
| **+1 dia** | Fechamento da fase | 1) Comparar custo real vs. estimado (seção 6.3.1 do doc de parcerias). 2) Guardar evidências (prints, comprovantes). 3) Decidir fornecedor principal definitivo. | Teste concluído |

## 4. Passo a passo detalhado

1. **Criar e-mail corporativo** (se ainda não existir) — evita recusa por domínio pessoal (caso do Plivo).
2. **Cadastrar na Telnyx** (`telnyx.com/sign-up`): confirmar e-mail, completar KYC assim que solicitado (não deixar parado esperando — é o item do caminho crítico).
3. **Em paralelo, abrir contato com Zenvia** (comparação futura, não bloqueante) e, opcionalmente, criar conta na Plivo só para cotar.
4. **Assim que aprovado**, gerar a API key no Mission Control Portal e usar os scripts da seção 5 para: checar saldo → buscar números → comprar 1–3 números de teste.
5. **Configurar encaminhamento de voz** no portal (UI) apontando o número para um celular/softphone.
6. **Fazer uma ligação de teste real** e validar qualidade de áudio, chamada recebida e discagem.
7. **Testar billing**: usar `check_balance.py` antes/depois da ligação de teste para calcular o custo real por minuto, e comparar com a estimativa da seção 6.3.1 do `docs/parcerias-revenda-numeros.md`.
8. **Guardar evidências** (prints de configuração, comprovante de compra do número, registro da ligação de teste) — vira lastro para o atestado técnico da Fase 2.
9. **Decidir o fornecedor principal** com base no teste real (preço, qualidade, suporte) antes de avançar para a Fase 1 (vender para clientes externos).

## 5. Scripts de validação técnica

Para não depender só de cliques manuais no portal (mais lento e mais sujeito a erro), os passos de checar saldo, buscar números e comprar número de teste estão automatizados em `scripts/fase0/` (Python puro, sem dependências externas). Ver `scripts/fase0/README.md` para instruções de uso. Resumo do fluxo:

```
python3 scripts/fase0/check_balance.py
python3 scripts/fase0/search_numbers.py 11 10
python3 scripts/fase0/buy_number.py +5511XXXXXXXXX --confirm
python3 scripts/fase0/list_my_numbers.py
```

`buy_number.py` gasta dinheiro de verdade — por isso exige a flag explícita `--confirm`.

## 6. Checklist resumido

- [ ] E-mail corporativo criado
- [ ] Cadastro Telnyx enviado (documentos de KYC submetidos)
- [ ] Cadastro Telnyx aprovado
- [ ] Contato comercial aberto com Zenvia (comparação futura)
- [ ] (Opcional) Cadastro Plivo feito para cotação
- [ ] API key gerada e validada (`check_balance.py`)
- [ ] 1–3 números comprados (`buy_number.py`) e testados
- [ ] Encaminhamento de voz configurado no portal
- [ ] Chamada de teste validada (qualidade de áudio OK)
- [ ] Custo real confirmado contra a estimativa da seção 6.3.1
- [ ] Fornecedor principal escolhido

## 7. Fontes

- [Telnyx – How to sign up for a Telnyx account](https://support.telnyx.com/en/articles/5295540-how-to-sign-up-for-a-telnyx-account)
- [Telnyx Developers – Create account](https://developers.telnyx.com/docs/account-setup/create-account.md)
- [Plivo Support – How can I create a Plivo account?](https://support.plivo.com/hc/en-us/articles/360041203772)
- [Zenvia – Dúvidas frequentes sobre integração de canais](https://zenvia.com/blog/duvidas-integrar-canais/)
- [Zenvia – Termos de Serviço da Plataforma de Voz](https://zenvia.com/termos/plataforma-voz/)
