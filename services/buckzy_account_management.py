from buckzy_client import BuckzyClient
from typing import Dict, Any

class BuckzyAccountManagement(BuckzyClient):
    """Manages Buckzy account-related operations in the Buckzy API."""

    def get_all_accounts(self, underlying: bool = True) -> Dict[str, Any]:
        """Retrieves all accounts for the client."""
        params = {"underlying": str(underlying).lower()}
        return self._make_request("GET", "/v1/accounts", params=params)
