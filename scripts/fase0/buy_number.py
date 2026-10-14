#!/usr/bin/env python3
"""Compra um ou mais numeros Telnyx. ISSO GASTA DINHEIRO DE VERDADE.

So executa se a flag --confirm estiver presente, de proposito, para
nao disparar uma compra sem querer.

Uso:
    python3 buy_number.py +5511999999999 --confirm
    python3 buy_number.py +5511999999999 +5511888888888 --confirm
    python3 buy_number.py +5511999999999 --confirm --requirement-group-id <id>

A flag --requirement-group-id so e necessaria se uma tentativa anterior
tiver retornado erro pedindo um "requirement group" (comum em numeros BR
que ainda nao passaram pelo envio de documentos no Mission Control Portal).
"""
import sys

from telnyx_client import post


def main():
    args = sys.argv[1:]
    if "--confirm" not in args:
        print("Isso vai gastar dinheiro de verdade. Rode de novo com --confirm no final.")
        print("Uso: python3 buy_number.py <numero-E164> [<numero-E164> ...] --confirm")
        raise SystemExit(1)
    args.remove("--confirm")

    requirement_group_id = None
    if "--requirement-group-id" in args:
        idx = args.index("--requirement-group-id")
        try:
            requirement_group_id = args[idx + 1]
        except IndexError:
            print("--requirement-group-id precisa de um valor logo em seguida.")
            raise SystemExit(1)
        del args[idx:idx + 2]

    numbers = args
    if not numbers:
        print("Informe pelo menos um numero em formato E.164, ex: +5511999999999")
        raise SystemExit(1)

    phone_numbers = [{"phone_number": n} for n in numbers]
    if requirement_group_id:
        for item in phone_numbers:
            item["requirement_group_id"] = requirement_group_id

    body = {"phone_numbers": phone_numbers}
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
