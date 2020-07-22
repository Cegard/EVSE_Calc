
import pytest
from . import dummy_data
from evse_charging_calculator.transaction import Transaction
from evse_charging_calculator import json_retrieval


def test_transaction_creation():
    """ Asserts that a new transaction is created
    """

    dummy_t = Transaction(**dummy_data.DUMMY_TRANSACTION)
    assert isinstance(dummy_t, Transaction)


def test_format_transaction_from_json_data():
    """ Asserts that a transaction is made from the json data
    """

    dummy_transaction = json_retrieval.format_transaction_data(dummy_data.RAW_TRANSACTION)
    dummy_transaction = Transaction(**dummy_transaction)
    assert isinstance(dummy_transaction, Transaction)


def test_get_all_transactions():
    """ Asserts that a transaction is made from the json data
    """

    dummy_transactions = json_retrieval.get_transactions(dummy_data.RAW_TRANSACTIONS)
    assert all([isinstance(Transaction(**dummy_transaction), Transaction) \
                for dummy_transaction in dummy_transactions])
