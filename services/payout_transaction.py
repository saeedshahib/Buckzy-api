from buckzy_client import BuckzyClient
from typing import Dict, Any

class PayoutTransaction(BuckzyClient):
    """Manages payout transaction-related operations in the Buckzy API."""

    def initiate_single_payment(self, payment_data: Dict[str, Any]) -> Dict[str, Any]:
        """Initiates a single payment transaction."""
        return self._make_request("POST", "/v1/transactions", data=payment_data)
    