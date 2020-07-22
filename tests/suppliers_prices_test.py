
import pytest
from . import dummy_data
from evse_charging_calculator.models.supplier_price import SupplierPrice


def test_create_supplier_price():
    """ Tests that a supplier price can be made from raw data
    """

    dummy_price = SupplierPrice(**dummy_data.SIMPLE_SUPPLIER_PRICE)
    assert isinstance(dummy_price, SupplierPrice)


def test_format_supplier_from_raw_data():
    """ Tests that a supplier price can be made from raw data
    """
    from evse_charging_calculator.json_retrieval import format_raw_price

    dummy_price = format_raw_price(dummy_data.SIMPLE_RAW_PRICE)
    assert isinstance(SupplierPrice(**dummy_price), SupplierPrice)
