
from datetime import datetime

DUMMY_TRANSACTION = {
    'charging_end': datetime.fromisoformat("2018-05-26T17:07:07"),
    'charging_start': datetime.fromisoformat("2018-05-26T00:05:04"),
    'country_code': "US",
    'evseid': "GI*BRA*H732*06",
    'meter_value_end': 4374.142,
    'meter_value_start': 4132.568,
    'metering_signature': "",
    'partner_product_id': "",
    'provider_id': "HF-MXK",
    'session_id': "d7ef6cb2-e4a8-4159-862e-73a7fc2f3a92",
    'session_end': datetime.fromisoformat("2018-05-26T17:07:07"),
    'session_start': datetime.fromisoformat("2018-05-25T05:52:49"),
    'uid': "e881a4da78f95356e786d90b8da68787",
}

RAW_TRANSACTION = {
    'Charging end': "2018-05-26T17:07:07",
    'Charging start':	"2018-05-26T00:05:04",
    'CountryCode': "US",
    'EVSEID': "GI*BRA*H732*06",
    'Meter value end': "4374.142",
    'Meter value start': "4132.568",
    'Metering signature':	"",
    "Partner product ID": "false",
    "Proveider ID": "HF-MXK",
    "Session ID": "d7ef6cb2-e4a8-4159-862e-73a7fc2f3a92",
    'Session end': "2018-05-26T17:07:07",
    'Session start': "2018-05-25T05:52:49",
    'UID': "e881a4da78f95356e786d90b8da68787",
}
