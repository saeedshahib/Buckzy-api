import requests
from typing import Dict, Any


class BuckzyClient:
    """
    A base client for the Buckzy API that handles authentication and common API requests.
    """

    def __init__(self, auth_host: str, api_host: str, client_id: str, client_secret: str, username: str, password: str, apikey: str):
        """
        Initializes the Buckzy API client.

        Args:
            auth_host (str): The authentication host URL.
            api_host (str): The API host URL.
            client_id (str): The client ID for authentication.
            client_secret (str): The client secret for authentication.
            username (str): The username for authentication.
            password (str): The password for authentication.
            apikey (str): The API key for authentication.
        """
        self.auth_host = auth_host
        self.api_host = api_host
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.apikey = apikey
        self.access_token = self._get_access_token()

    def _get_access_token(self) -> str:
        """
        Retrieves an access token from the Buckzy authentication server.

        Returns:
            str: The access token.
        """
        url = f"{self.auth_host}/token"
        params = {"apikey": self.apikey}
        data = {
            "grant_type": "password",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "username": self.username,
            "password": self.password,
        }
        response = requests.post(url, params=params, data=data)
        response.raise_for_status()
        return response.json()["access_token"]

    def _make_request(self, method: str, endpoint: str, params: Dict[str, Any] = None, data: Dict[str, Any] = None, files: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Makes a request to the Buckzy API.

        Args:
            method (str): The HTTP method to use (e.g., 'GET', 'POST', 'PUT', 'DELETE').
            endpoint (str): The API endpoint to call.
            params (Dict[str, Any], optional): The query parameters for the request. Defaults to None.
            data (Dict[str, Any], optional): The JSON data to send with the request. Defaults to None.
            files (Dict[str, Any], optional): The files to send with the request. Defaults to None.

        Returns:
            Dict[str, Any]: The JSON response from the API.
        """
        url = f"{self.api_host}{endpoint}"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        if params is None:
            params = {}
        params["apikey"] = self.apikey
        response = requests.request(method, url, headers=headers, params=params, json=data, files=files)
        response.raise_for_status()
        return response.json()
