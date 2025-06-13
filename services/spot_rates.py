from buckzy_client import BuckzyClient
from typing import Dict, Any

class SpotRates(BuckzyClient):
    """Manages spot rate-related operations in the Buckzy API."""

    def get_spot_rate(self, from_currency: str, to_currency: str, amount: float, transfer_type: str = "BANK_TRANSFER") -> Dict[str, Any]:
        """Gets the current spot rate for a currency pair."""
        data = {
            "fromCurrencyCode": from_currency,
            "toCurrencyCode": to_currency,
            "sendingAmount": amount,
            "transferType": transfer_type
        }
        return self._make_request("POST", "/v2/fx", data=data)
