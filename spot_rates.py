from buckzy_client import BuckzyClient
from typing import Dict, Any


class SpotRates(BuckzyClient):
    """
    A class to manage spot rate-related operations in the Buckzy API.
    """

    def get_spot_rate(self, from_currency: str, to_currency: str, amount: float) -> Dict[str, Any]:
        """
        Gets the current spot rate for a currency pair.

        Args:
            from_currency (str): The currency to convert from.
            to_currency (str): The currency to convert to.
            amount (float): The amount to convert.

        Returns:
            Dict[str, Any]: The response from the API.
        """
        data = {
            "fromCurrencyCode": from_currency,
            "toCurrencyCode": to_currency,
            "sendingAmount": amount,
        }
        return self._make_request("POST", "/v2/fx", data=data)
