from buckzy_client import BuckzyClient
from typing import Dict, Any


class PayoutTransaction(BuckzyClient):
    """
    A class to manage payout transaction-related operations in the Buckzy API.
    """

    def initiate_single_payment(self, payment_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Initiates a single payment transaction.

        Args:
            payment_data (Dict[str, Any]): The data for the payment.

        Returns:
            Dict[str, Any]: The response from the API.
        """
        return self._make_request("POST", "/v1/transactions", data=payment_data)
