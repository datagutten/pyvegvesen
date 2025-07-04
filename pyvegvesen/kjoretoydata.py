import os
import sys

import requests

from .model import Model


def kjoretoydata(kjennemerke: str) -> Model:
    url = 'https://akfell-datautlevering.atlas.vegvesen.no/enkeltoppslag/kjoretoydata'
    response = requests.get(url, {'kjennemerke': kjennemerke}, headers={
        'SVV-Authorization': os.environ.get('VEGVESEN_API_KEY'),
    })
    response.raise_for_status()
    return Model(**response.json())


if __name__ == '__main__':
    data = kjoretoydata(sys.argv[1])
    print(data)
