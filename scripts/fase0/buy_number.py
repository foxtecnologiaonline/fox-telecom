#!/usr/bin/env python3
"""Compra um ou mais numeros Telnyx. ISSO GASTA DINHEIRO DE VERDADE.

So executa se a flag --confirm estiver presente, de proposito, para
nao disparar uma compra sem querer.

Uso:
    python3 buy_number.py +5511999999999 --confirm
    python3 buy_number.py +5511999999999 +5511888888888 --confirm
"""
import sys

from telnyx_client import post


def main():
    args = sys.argv[1:]
    if "--confirm" not in args:
        print("Isso vai gastar dinheiro de verdade. Rode de novo com --confirm no final.")
        print("Uso: python3 buy_number.py <numero-E164> [<numero-E164> ...] --confirm")
        raise SystemExit(1)

    numbers = [a for a in args if a != "--confirm"]
    if not numbers:
        print("Informe pelo menos um numero em formato E.164, ex: +5511999999999")
        raise SystemExit(1)

    body = {"phone_numbers": [{"phone_number": n} for n in numbers]}
    status, resp = post("/number_orders", body=body)

    if status not in (200, 201):
        print(f"Erro ({status}):", resp)
        print(
            "\nSe o erro mencionar 'requirement' ou documento pendente, "
            "numeros do Brasil normalmente exigem envio de CNPJ/comprovante "
            "via Mission Control Portal antes da primeira compra."
        )
        raise SystemExit(1)

    print("Pedido criado:")
    print(resp)


if __name__ == "__main__":
    main()
