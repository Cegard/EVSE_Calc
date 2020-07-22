
import json
import requests


def get_json(url):
    """ Retrieves the json data from the given URL
    """

    return json.loads(requests.get(url).text)
