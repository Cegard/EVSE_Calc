
import pytest
from . import dummy_data


def test_transaction_creation():
    """ Asserts that a new transaction is created
    """
    from evse_charging_calculator import transaction

    dummy_t = transaction.Transaction(**dummy_data.DUMMY_TRANSACTION)

    assert isinstance(dummy_t, transaction.Transaction)
