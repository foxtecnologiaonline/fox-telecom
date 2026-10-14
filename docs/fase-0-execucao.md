# Fase 0 — Execução (Estrutura para autoconsumo/validação)

> Runbook operacional da Fase 0 do `docs/roteiro-lancamento.md`. Pressupõe que o CNPJ já está aberto — portanto o foco aqui é só: escolher fornecedor(es), abrir cadastro, comprar números de teste e validar o fluxo fim a fim.

## 1. Fornecedores para abrir cadastro agora

Recomendação: abrir cadastro em **2 fornecedores em paralelo** (não custa nada além de tempo, já que são self-service sem contrato mínimo) para comparar preço, qualidade de voz e facilidade de KYC antes de escolher o principal.

| Prioridade | Fornecedor | Por que | Link oficial | Verificação exigida |
|---|---|---|---|---|
| 1 | **Telnyx** | Mais barato (DID BR a partir de US$1/mês), portal self-service maduro (Mission Control), boa documentação de API | Cadastro: [telnyx.com/sign-up](https://telnyx.com/sign-up) · Portal após cadastro: [portal.telnyx.com](https://portal.telnyx.com) | E-mail corporativo (ou login via Google/Microsoft), confirmação de e-mail, celular válido; alguns cadastros passam por KYC adicional pedindo CNPJ/documento societário |
| 2 | **Zenvia** (ex-TotalVoice) | Empresa brasileira, suporte em português, já resolve a "Operadora Parceira" por trás — mais simples de validar o KYC usando CNPJ nacional | [zenvia.com](https://zenvia.com) → menu "Voz" / "Plataforma de Voz" (a própria Zenvia instrui criar conta nessa área antes de gerar o Access Token em "Minha Conta") | Aceite dos Termos de Serviço da Plataforma de Voz no cadastro |
| 3 (opcional, comparação) | **Plivo** | Preço competitivo (DID ~US$5/mês), bom para comparar custo com Telnyx | [plivo.com](https://plivo.com) → "Sign Up" | E-mail corporativo obrigatório (domínios pessoais como Gmail/Hotmail são recusados), verificação por celular, **não usar VPN** durante o cadastro |

> Não guardei um link profundo de cadastro para Zenvia e Plivo porque não encontrei a URL exata documentada publicamente — use o link do domínio principal e navegue pelo menu ("Voz"/"Sign Up"), em vez de um link adivinhado.

## 2. Documentos para ter em mãos (você já tem o CNPJ — falta reunir o resto)

- [ ] Cartão CNPJ / comprovante de inscrição (já emitido junto com o CNPJ)
- [ ] Contrato social ou documento de constituição da empresa
- [ ] RG/CPF do responsável legal (sócio-administrador)
- [ ] Comprovante de endereço da empresa (conta de luz/água/telefone em nome do CNPJ, ou contrato de locação)
- [ ] E-mail corporativo (evitar @gmail/@hotmail pessoal nos cadastros que pedem domínio corporativo — se ainda não tiver, criar um e-mail no domínio da FOX Telecom antes de cadastrar)
- [ ] Telefone celular válido para verificação por SMS/chamada
- [ ] Cartão de crédito corporativo ou meio de pagamento internacional (Telnyx/Plivo cobram em USD via cartão; Zenvia tende a aceitar faturamento nacional)

## 3. Passo a passo de execução

1. **Criar e-mail corporativo** (se ainda não existir) para usar nos cadastros — evita recusa por domínio pessoal (caso do Plivo).
2. **Cadastrar na Telnyx** (`telnyx.com/sign-up`): confirmar e-mail, completar KYC se solicitado, aguardar liberação (pode levar até 3 dias úteis para numeração BR).
3. **Cadastrar na Zenvia** (`zenvia.com` → Voz): criar conta, aceitar os Termos da Plataforma de Voz, gerar o Access Token em "Minha Conta".
4. **(Opcional) Cadastrar na Plivo** só para cotar/comparar preço, sem necessariamente operacionalizar nela ainda.
5. **Comprar 1 a 3 números de teste** (DID local ou 0800) no fornecedor escolhido como principal.
6. **Configurar encaminhamento/teste de chamada**: direcionar o número para um celular ou softphone e validar qualidade de áudio, ligação recebida e discagem.
7. **Testar billing**: confirmar que a fatura/cobrança do fornecedor bate com o que foi estimado na seção 6.3 do `docs/parcerias-revenda-numeros.md` (custo variável por número).
8. **Guardar evidências** (prints de configuração, comprovante de compra do número, teste de chamada gravado) — isso já começa a virar lastro para o atestado técnico da Fase 2.
9. **Decidir o fornecedor principal** com base no teste real (preço, qualidade, suporte) antes de avançar para a Fase 1 (vender para clientes externos).

## 4. Checklist resumido

- [ ] E-mail corporativo criado
- [ ] Cadastro Telnyx aprovado
- [ ] Cadastro Zenvia aprovado
- [ ] (Opcional) Cadastro Plivo feito para cotação
- [ ] 1–3 números comprados e testados
- [ ] Chamada de teste validada (qualidade de áudio OK)
- [ ] Custo real confirmado contra a estimativa da seção 6.3
- [ ] Fornecedor principal escolhido

## 5. Fontes

- [Telnyx – How to sign up for a Telnyx account](https://support.telnyx.com/en/articles/5295540-how-to-sign-up-for-a-telnyx-account)
- [Telnyx Developers – Create account](https://developers.telnyx.com/docs/account-setup/create-account.md)
- [Plivo Support – How can I create a Plivo account?](https://support.plivo.com/hc/en-us/articles/360041203772)
- [Zenvia – Dúvidas frequentes sobre integração de canais](https://zenvia.com/blog/duvidas-integrar-canais/)
- [Zenvia – Termos de Serviço da Plataforma de Voz](https://zenvia.com/termos/plataforma-voz/)
