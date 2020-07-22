
import pytest
from . import dummy_data


def test_json_not_null():
    """ Asserts if the .json exists after retrieval.
    """
    from evse_charging_calculator import json_retrieval

    json_retrieved = json_retrieval.get_json(dummy_data.URL)
    assert json_retrieved
