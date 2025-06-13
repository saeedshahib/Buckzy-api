from buckzy_client import BuckzyClient
from typing import Dict, Any
from werkzeug.datastructures import FileStorage


class EntityDocumentsManagement(BuckzyClient):
    """Manages entity document-related operations in the Buckzy API."""

    def attach_document_file(self, customer_id: str, entity_id: str, document_file: FileStorage,
                             form_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Attaches a document file to an entity using multipart/form-data.
        """
        endpoint = f"/v1/customers/{customer_id}/entities/{entity_id}/documents:multi-file"
        files = {'document': (document_file.filename, document_file.stream, document_file.mimetype)}

        # 'data' will be passed as form fields and 'files' as the file part
        return self._make_request("POST", endpoint, data=form_data, files=files)
