from buckzy_client import BuckzyClient
from typing import Dict, Any, List


class CustomerManagement(BuckzyClient):
    """
    A class to manage customer-related operations in the Buckzy API.
    """

    def create_child_customer(self, customer_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new child customer.

        Args:
            customer_data (Dict[str, Any]): The data for the new customer.

        Returns:
            Dict[str, Any]: The response from the API.
        """
        return self._make_request("POST", "/v1/customers", data=customer_data)

    def update_child_customer(self, customer_id: str, customer_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an existing child customer.

        Args:
            customer_id (str): The ID of the customer to update.
            customer_data (Dict[str, Any]): The new data for the customer.

        Returns:
            Dict[str, Any]: The response from the API.
        """
        return self._make_request("PUT", f"/v1/customers/{customer_id}", data=customer_data)

    def get_all_child_customers(self, size: int = 999, status: str = None) -> Dict[str, Any]:
        """
        Retrieves a list of all child customers.

        Args:
            size (int, optional): The number of customers to retrieve. Defaults to 999.
            status (str, optional): The status of the customers to retrieve. Defaults to None.

        Returns:
            Dict[str, Any]: The response from the API.
        """
        params = {"size": size}
        if status:
            params["status"] = status
        return self._make_request("GET", "/v1/customers", params=params)

    def get_child_customer_by_filter(self, customer_id: str) -> Dict[str, Any]:
        """
        Retrieves a child customer by their ID.

        Args:
            customer_id (str): The ID of the customer to retrieve.

        Returns:
            Dict[str, Any]: The response from the API.
        """
        return self._make_request("GET", f"/v1/customers/{customer_id}")