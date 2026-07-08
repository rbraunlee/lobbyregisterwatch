import requests
from urllib.parse import urljoin

def call_lr(base_url, endpoint, params, header):
    while True:
        response = requests.get(urljoin(base_url, endpoint), params=params, headers = header)
        response.raise_for_status()
        tmp = response.json()["results"]

        yield tmp["results"]

        if tmp["results"] ==[]:
            break
        cursor = tmp["cursor"]
        if params.get("cursor") == cursor:
            break
        params["cursor"] = cursor
