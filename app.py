import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

# Import service classes
from services.customer_management import CustomerManagement
from services.spot_rates import SpotRates
from services.buckzy_account_management import BuckzyAccountManagement
from services.payout_transaction import PayoutTransaction
from services.entity_documents_management import EntityDocumentsManagement

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# --- Configuration ---
CONFIG = {
    "auth_host": os.getenv("AUTH_HOST"),
    "api_host": os.getenv("API_HOST"),
    "client_id": os.getenv("CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET"),
    "username": os.getenv("BUCKZY_USERNAME"),
    "password": os.getenv("BUCKZY_PASSWORD"),
    "apikey": os.getenv("API_KEY"),
}


# --- API Error Handling ---
@app.errorhandler(Exception)
def handle_exception(e):
    """Generic error handler to return JSON response."""
    # Pass through HTTP errors
    if hasattr(e, 'code'):
        return jsonify(error=str(e)), e.code
    # Handle other exceptions
    return jsonify(error=f"An internal error occurred: {e}"), 500


# --- Helper to initialize services ---
def get_service(service_class):
    """Initializes a service class with credentials."""
    try:
        return service_class(**CONFIG)
    except Exception as e:
        # This will be caught by the generic error handler
        raise Exception(f"Failed to initialize API client: {e}")


# --- API Routes ---
@app.route('/')
def index():
    """Welcome endpoint."""
    return jsonify({"message": "Welcome to the Buckzy API Wrapper"})


@app.route('/customers', methods=['GET'])
def get_customers():
    """Retrieves all child customers."""
    customer_service = get_service(CustomerManagement)
    customers_data = customer_service.get_all_child_customers()
    return jsonify(customers_data)


@app.route('/accounts', methods=['GET'])
def get_accounts():
    """Retrieves all accounts."""
    account_service = get_service(BuckzyAccountManagement)
    accounts_data = account_service.get_all_accounts()
    return jsonify(accounts_data)


@app.route('/spot-rates', methods=['POST'])
def get_spot_rates():
    """Gets the current spot rate for a currency pair."""
    data = request.get_json()
    if not data or not all(k in data for k in ['from_currency', 'to_currency', 'amount']):
        return jsonify({"error": "Missing required fields: from_currency, to_currency, amount"}), 400

    spot_rates_service = get_service(SpotRates)
    rate_info = spot_rates_service.get_spot_rate(
        data['from_currency'],
        data['to_currency'],
        float(data['amount'])
    )
    return jsonify(rate_info)


@app.route('/payouts', methods=['POST'])
def create_payout():
    """Initiates a single payment transaction."""
    payout_data = request.get_json()
    if not payout_data:
        return jsonify({"error": "Request body cannot be empty"}), 400

    payout_service = get_service(PayoutTransaction)
    result = payout_service.initiate_single_payment(payout_data)
    return jsonify(result)


@app.route('/customers/<string:customer_id>/entities/<string:entity_id>/documents', methods=['POST'])
def upload_document(customer_id, entity_id):
    """Uploads a document for a specific customer entity."""
    if 'document' not in request.files:
        return jsonify({"error": "No document file provided in the 'document' field"}), 400

    document_file = request.files['document']

    # Extract other form fields required by the Buckzy API
    form_data = {
        'fileTp': request.form.get('fileTp'),
        'docType': request.form.get('docType')
    }

    if not all(form_data.values()):
        return jsonify({"error": "Missing required form fields: fileTp, docType"}), 400

    doc_service = get_service(EntityDocumentsManagement)
    result = doc_service.attach_document_file(customer_id, entity_id, document_file, form_data)

    return jsonify(result)


if __name__ == '__main__':
    # Check for missing configuration on startup
    for key, value in CONFIG.items():
        if not value:
            print(f"FATAL ERROR: Environment variable '{key.upper()}' is not set.")
            exit(1)
    app.run(debug=True)