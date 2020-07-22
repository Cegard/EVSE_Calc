
import json
import requests


def get_json(url: str) -> dict:
    """ Retrieves the json data from the given URL
    """

    return json.loads(requests.get(url).text)
