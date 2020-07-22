from datetime import datetime


class Transaction:
    """ A charge transaction from a EVSE
    """


    def __init__(
        self,
        charging_end: datetime,
        charging_start: datetime,
        country_code: str,
        evseid: str,
        meter_value_end: float,
        meter_value_start: float,
        metering_signature: str,
        partner_product_id: str,
        proveider_id: str,
        session_id: str,
        session_end: str,
        session_start: str,
        uid: str,
    ):
        self.charging_end = charging_end
        self.charging_start = charging_start
        self.country_code = country_code
        self.evseid = evseid
        self.meter_value_end = meter_value_end
        self.meter_value_start = meter_value_start
        self.metering_signature = metering_signature
        self.partner_product_id = partner_product_id
        self.proveider_id = proveider_id
        self.session_id = session_id
        self.session_end = session_end
        self.session_start = session_start
        self.uid = uid
    