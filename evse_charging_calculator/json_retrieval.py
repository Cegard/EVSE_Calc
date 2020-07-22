
from datetime import datetime
import json
import requests



def get_json(url: str) -> dict:
    """ Retrieves the json data from the given URL
    """

    return json.loads(requests.get(url).text)


def format_transaction_data(transaction_data: dict) -> dict:
    """ Transforms a raw transaction data to its proper data types
    """
    formated_data = {}
    formated_data['charging_end'] = datetime.fromisoformat(transaction_data['Charging end'])
    formated_data['charging_start'] = datetime.fromisoformat(transaction_data['Charging start'])
    formated_data['meter_value_end'] = float(transaction_data['Meter value end'])
    formated_data['meter_value_start'] = float(transaction_data['Meter value start'])
    formated_data["partner_product_id"] = transaction_data["Partner product ID"] \
            if transaction_data["Partner product ID"] else ""
    formated_data['session_end'] = datetime.fromisoformat(transaction_data['Session end'])
    formated_data['session_start'] = datetime.fromisoformat(transaction_data['Session start'])
    formated_data['country_code'] = transaction_data['CountryCode']
    formated_data['evseid'] = transaction_data['EVSEID']
    formated_data['metering_signature'] = transaction_data['Metering signature']
    formated_data['provider_id'] = transaction_data['Proveider ID']
    formated_data['session_id'] = transaction_data['Session ID']
    formated_data['uid'] = transaction_data['UID']

    return formated_data


def get_transactions(transactions: list) -> list:
    """ Makes Transaction type objects from a list with raw data
    """

    return map(format_transaction_data, transactions)


def format_raw_price(raw_price: dict) -> dict:
    """ Formats a raw supplier to its proper datatypes
    """
    formated_price = {}
    formated_price['charge_based_id'] = raw_price['EVSE ID'] \
            if raw_price['EVSE ID'] else raw_price['Product ID']
    formated_price['identifier'] = raw_price['EVSE ID']
    formated_price['company_name'] = raw_price['Company name']
    formated_price['currency'] = raw_price['Currency']

    return formated_price
