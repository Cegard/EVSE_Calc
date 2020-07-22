
import pytest


def test_json_not_null():
    """ Asserts if the .json exists after retrieval.
    """
    from evse_charging_calculator import json_retrieval, constants

    json_retrieved = json_retrieval.get_json(constants.CONSTANTS['url'])
    assert json_retrieved
