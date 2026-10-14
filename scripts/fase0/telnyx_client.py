"""Cliente HTTP minimo para a API da Telnyx (so biblioteca padrao, sem dependencias).

Confirme sempre nomes de campos/endpoints contra developers.telnyx.com/docs:
a API pode ter mudado desde que este script foi escrito.
"""
import json
import os
import urllib.error
import urllib.parse
import urllib.request

API_BASE = "https://api.telnyx.com/v2"


def _request(method, path, params=None, body=None):
    api_key = os.environ.get("TELNYX_API_KEY")
    if not api_key:
        raise SystemExit(
            "Defina TELNYX_API_KEY no ambiente antes de rodar "
            "(veja scripts/fase0/.env.example)."
        )

    url = API_BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params, doseq=True)

    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {api_key}")
    req.add_header("Accept", "application/json")
    if data is not None:
        req.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8")
        try:
            return e.code, json.loads(raw)
        except json.JSONDecodeError:
            return e.code, {"raw_error": raw}
    except urllib.error.URLError as e:
        raise SystemExit(f"Falha de conexao com a API da Telnyx: {e.reason}")


def get(path, params=None):
    return _request("GET", path, params=params)


def post(path, body=None):
    return _request("POST", path, body=body)
