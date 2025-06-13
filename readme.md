# Buckzy REST API Project

This project is a Flask-based REST API that acts as a wrapper for the official Buckzy API. It simplifies interaction with key Buckzy services by exposing them through a clean, local API.

## Quick Start

### 1. Prerequisites
* Python 3.8+
* An active Buckzy developer account with API credentials.

### 2. Setup
Clone this repository, create a virtual environment, and install the required dependencies.

```bash
# It is recommended to use a virtual environment
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the project root (you can rename `.env.example`). Fill it with your Buckzy API credentials:

```ini
FLASK_APP=app.py
AUTH_HOST="YOUR_BUCKZY_AUTH_HOST"
API_HOST="YOUR_BUCKZY_API_HOST"
CLIENT_ID="YOUR_BUCKZY_CLIENT_ID"
CLIENT_SECRET="YOUR_BUCKZY_CLIENT_SECRET"
BUCKZY_USERNAME="YOUR_BUCKZY_USERNAME"
BUCKZY_PASSWORD="YOUR_BUCKZY_PASSWORD"
API_KEY="YOUR_BUCKZY_API_KEY"
```

### 4. Run the API Server
Launch the Flask development server.

```bash
flask run
```
The API is now available at `http://127.0.0.1:5000`.

---

## API Endpoints

* `GET /`: Welcome message to check if the service is running.
* `GET /customers`: Get a list of all child customers.
* `GET /accounts`: Get a list of all client accounts.
* `POST /spot-rates`: Get a currency exchange rate.
* `POST /payouts`: Initiate a new payment transaction.
* `POST /customers/<cust_id>/entities/<entity_id>/documents`: Upload a document for an entity.

### `curl` Examples

**Get a Spot Rate (`POST` with JSON):**
```bash
curl -X POST [http://127.0.0.1:5000/spot-rates](http://127.0.0.1:5000/spot-rates) \
-H "Content-Type: application/json" \
-d '{
    "from_currency": "USD",
    "to_currency": "CAD",
    "amount": 100
}'
```

**Upload a Document (`POST` with multipart/form-data):**
```bash
curl -X POST [http://127.0.0.1:5000/customers/YOUR_CUSTOMER_ID/entities/YOUR_ENTITY_ID/documents](http://127.0.0.1:5000/customers/YOUR_CUSTOMER_ID/entities/YOUR_ENTITY_ID/documents) \
-F "fileTp=PASSPORT" \
-F "docType=PROOF_OF_IDENTITY" \
-F "document=@/path/to/your/document.pdf"