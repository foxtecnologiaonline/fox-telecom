#!/usr/bin/env python3
"""Lista numeros brasileiros disponiveis para compra na Telnyx.

Uso:
    python3 search_numbers.py [DDD] [limite]

Exemplo:
    python3 search_numbers.py 11 10
"""
import sys

from telnyx_client import get


def main():
    ddd = sys.argv[1] if len(sys.argv) > 1 else None
    limit = sys.argv[2] if len(sys.argv) > 2 else "10"

    params = {
        "filter[country_code]": "BR",
        "filter[limit]": limit,
    }
    if ddd:
        params["filter[national_destination_code]"] = ddd

    status, body = get("/available_phone_numbers", params=params)
    if status != 200:
        print(f"Erro ({status}):", body)
        raise SystemExit(1)

    numbers = body.get("data", [])
    if not numbers:
        print("Nenhum numero encontrado para esse filtro.")
        return

    for n in numbers:
        phone = n.get("phone_number")
        extra = {k: v for k, v in n.items() if k not in ("phone_number", "record_type")}
        print(f"{phone}  |  {extra}")


if __name__ == "__main__":
    main()
