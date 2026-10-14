#!/usr/bin/env python3
"""Confirma que a TELNYX_API_KEY funciona e mostra o saldo da conta.

Uso:
    python3 check_balance.py
"""
from telnyx_client import get


def main():
    status, body = get("/balance")
    if status != 200:
        print(f"Erro ({status}):", body)
        raise SystemExit(1)

    data = body.get("data", {})
    print(f"Saldo: {data.get('balance')} {data.get('currency')}")
    print(f"Credito disponivel: {data.get('available_credit')}")
    print(f"Limite de credito: {data.get('credit_limit')}")


if __name__ == "__main__":
    main()
