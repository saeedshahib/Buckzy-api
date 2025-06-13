from buckzy_client import BuckzyClient
from typing import Dict, Any


class BuckzyAccountManagement(BuckzyClient):
    """
    A class to manage Buckzy account-related operations in the Buckzy API.
    """

    def create_main_account(self, currency_code: str, client_id: str) -> Dict[str, Any]:
        """
        Creates a new main account.

        Args:
            currency_code (str): The currency code for the account.
            client_id (str): The client ID for the account.

        Returns:
            Dict[str, Any]: The response from the API.
        """
        data = {"currencyCode": currency_code, "clientId": client_id}
        return self._make_request("POST", "/v1/accounts", data=data)

    def get_all_accounts(self, underlying: bool = True) -> Dict[str, Any]:
        """
        Retrieves all accounts for the client.

        Args:
            underlying (bool, optional): Whether to include underlying accounts. Defaults to True.

        Returns:
            Dict[str, Any]: The response from the API.
        """
        params = {"underlying": underlying}
        return self._make_request("GET", "/v1/accounts", params=params)
