


class SupplierPrice:
    """ An EVSE supplier price
    """


    def __init__(
            self,
            charge_based_id: str,
            identifier: str,
            company_name: str,
            currency: list,
    ):
        self.charge_based_id = charge_based_id
        self.identifier = identifier
        self.company_name = company_name
        self.currency = {
            'name': currency[0],
            'symbol': currency[1]
        }
