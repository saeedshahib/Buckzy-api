from buckzy_client import BuckzyClient
from typing import Dict, Any


class EntityDocumentsManagement(BuckzyClient):
    """
    A class to manage entity document-related operations in the Buckzy API.
    """

    def attach_document_base64(self, customer_id: str, entity_id: str, document_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Attaches a document to an entity in base64 format.

        Args:
            customer_id (str): The ID of the customer.
            entity_id (str): The ID of the entity.
            document_data (Dict[str, Any]): The document data to attach.

        Returns:
            Dict[str, Any]: The response from the API.
        """
        return self._make_request("POST", f"/v1/customers/{customer_id}/entities/{entity_id}/documents", data=document_data)

    def attach_document_file(self, customer_id: str, entity_id: str, document_files: Dict[str, Any], file_type: str) -> Dict[str, Any]:
        """
        Attaches a document file to an entity.

        Args:
            customer_id (str): The ID of the customer.
            entity_id (str): The ID of the entity.
            document_files (Dict[str, Any]): The document files to attach.
            file_type (str): The type of the file.

        Returns:
            Dict[str, Any]: The response from the API.
        """
        data = {"fileTp": file_type}
        return self._make_request("POST", f"/v1/customers/{customer_id}/entities/{entity_id}/documents:multi-file", data=data, files=document_files)