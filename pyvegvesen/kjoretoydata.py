import os
import sys
from typing import Optional

import requests

from .model import Model


def kjoretoydata(kjennemerke: str) -> Optional[Model]:
    url = 'https://akfell-datautlevering.atlas.vegvesen.no/enkeltoppslag/kjoretoydata'
    response = requests.get(url, {'kjennemerke': kjennemerke}, headers={
        'SVV-Authorization': os.environ.get('VEGVESEN_API_KEY'),
    })
    if response.status_code == 204:
        return None
    response.raise_for_status()
    return Model(**response.json())


if __name__ == '__main__':
    data = kjoretoydata(sys.argv[1])
    print(data)
