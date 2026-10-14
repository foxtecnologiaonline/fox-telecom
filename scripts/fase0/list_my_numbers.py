#!/usr/bin/env python3
"""Lista os numeros ja comprados na conta Telnyx.

Uso:
    python3 list_my_numbers.py
"""
from telnyx_client import get


def main():
    status, body = get("/phone_numbers", params={"page[size]": "50"})
    if status != 200:
        print(f"Erro ({status}):", body)
        raise SystemExit(1)

    numbers = body.get("data", [])
    if not numbers:
        print("Nenhum numero na conta ainda.")
        return

    for n in numbers:
        phone = n.get("phone_number")
        extra = {k: v for k, v in n.items() if k not in ("phone_number", "record_type")}
        print(f"{phone}  |  {extra}")


if __name__ == "__main__":
    main()
