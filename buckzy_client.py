import requests
from typing import Dict, Any


class BuckzyClient:
    """
    A base client for the Buckzy API that handles authentication and common API requests.
    """

    def __init__(self, auth_host: str, api_host: str, client_id: str, client_secret: str, username: str, password: str,
                 apikey: str):
        """Initializes the Buckzy API client."""
        self.auth_host = auth_host
        self.api_host = api_host
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.apikey = apikey
        self.access_token = self._get_access_token()

    def _get_access_token(self) -> str:
        """Retrieves an access token from the Buckzy authentication server."""
        url = f"{self.auth_host}/token"
        params = {"apikey": self.apikey}
        data = {
            "grant_type": "password",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "username": self.username,
            "password": self.password,
        }
        try:
            response = requests.post(url, params=params, data=data)
            response.raise_for_status()
            return response.json()["access_token"]
        except requests.exceptions.RequestException as e:
            print(f"Error getting access token: {e}")
            raise

    def _make_request(self, method: str, endpoint: str, params: Dict[str, Any] = None, data: Dict[str, Any] = None,
                      files: Dict[str, Any] = None) -> Dict[str, Any]:
        """Makes a request to the Buckzy API."""
        url = f"{self.api_host}{endpoint}"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        if params is None:
            params = {}
        params["apikey"] = self.apikey

        try:
            response = requests.request(method, url, headers=headers, params=params, json=data, files=files)
            response.raise_for_status()
            if response.status_code == 204 or not response.content:
                return {}
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making request to {url}: {e}")
            if e.response is not None:
                print(f"Response status: {e.response.status_code}")
                print(f"Response body: {e.response.text}")
            raise