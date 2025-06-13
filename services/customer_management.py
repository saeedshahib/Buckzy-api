from buckzy_client import BuckzyClient
from typing import Dict, Any

class CustomerManagement(BuckzyClient):
    """Manages customer-related operations in the Buckzy API."""

    def get_all_child_customers(self, size: int = 100, status: str = None) -> Dict[str, Any]:
        """Retrieves a list of all child customers."""
        params = {"size": size}
        if status:
            params["status"] = status
        return self._make_request("GET", "/v1/customers", params=params)
