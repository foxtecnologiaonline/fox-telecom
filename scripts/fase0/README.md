# Scripts de validação técnica — Fase 0 (Telnyx)

Scripts em Python 3 (só biblioteca padrão, sem dependências externas) para
rodar a validação técnica da Fase 0 de forma rápida e repetível, em vez de
só clicar manualmente no Mission Control Portal.

Contexto completo em `docs/fase-0-execucao.md`.

## Pré-requisito

Cadastro na Telnyx aprovado (KYC concluído) e uma API key gerada no Mission
Control Portal (`portal.telnyx.com`).

## Configuração

```bash
cd scripts/fase0
cp .env.example .env
# edite .env e cole sua API key
export $(grep -v '^#' .env | xargs)
```

## Scripts

| Script | O que faz | Gasta dinheiro? |
|---|---|---|
| `check_balance.py` | Confirma que a API key funciona e mostra o saldo da conta | Não |
| `search_numbers.py [DDD] [limite]` | Lista números brasileiros disponíveis para compra | Não |
| `buy_number.py <numero-E164> --confirm [--requirement-group-id <id>]` | Compra número(s) — exige a flag `--confirm` de propósito. Use `--requirement-group-id` se uma tentativa anterior retornar erro pedindo um grupo de requisitos regulatórios | **Sim** |
| `list_my_numbers.py` | Lista números já comprados na conta | Não |

## Fluxo recomendado (depois do cadastro aprovado)

```bash
python3 check_balance.py
# se o saldo estiver zerado, adicionar cartão/crédito no portal antes de continuar

python3 search_numbers.py 11 10
# escolha um numero da lista

python3 buy_number.py +5511XXXXXXXXX --confirm

python3 list_my_numbers.py
```

Depois da compra, configure o encaminhamento de voz simples (número →
celular) direto na interface do Mission Control Portal — é mais rápido
fazer isso na UI do que via API nesta fase. Faça uma ligação de teste real
e rode `check_balance.py` antes/depois para calcular o custo real por
minuto (compare com a seção 6.3.1 de `docs/parcerias-revenda-numeros.md`).

## Observação sobre números do Brasil

A Telnyx normalmente exige envio de documentos (CNPJ, comprovante) antes de
liberar a primeira compra de numeração brasileira. Se `buy_number.py`
retornar erro mencionando `requirement` ou documento pendente, resolva isso
primeiro no Mission Control Portal e rode o script de novo.

## Aviso

Os nomes exatos de alguns campos de resposta da API podem mudar — confirme
contra a documentação oficial (`developers.telnyx.com/docs`) se algo não
bater com o esperado. Nunca commite o arquivo `.env` com a chave real.

Falhas de conexão (sem internet, DNS, timeout) aparecem como uma mensagem
clara de erro — não como um traceback cru — e cada chamada tem timeout de
20s para não travar indefinidamente.

## Testes

Todos os scripts foram validados contra um servidor HTTP local simulando as
respostas da API da Telnyx (saldo, busca de números, criação de pedido,
listagem) antes de serem commitados, cobrindo o caminho feliz, erro HTTP,
falha de conexão e os dois modos de `buy_number.py` (com e sem
`--requirement-group-id`). Isso não substitui testar contra a API real
assim que houver uma chave válida.
