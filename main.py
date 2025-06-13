from buckzy_client import BuckzyClient
from customer_management import CustomerManagement
from entity_documents_management import EntityDocumentsManagement
from spot_rates import SpotRates
from buckzy_account_management import BuckzyAccountManagement
from payout_transaction import PayoutTransaction


def main():
    """
    Main function to demonstrate the usage of the Buckzy API wrapper.
    """
    # Replace with your actual credentials
    auth_host = "YOUR_AUTH_HOST"
    api_host = "YOUR_API_HOST"
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"
    username = "YOUR_USERNAME"
    password = "YOUR_PASSWORD"
    apikey = "YOUR_API_KEY"

    # Initialize the clients
    buckzy_client = BuckzyClient(auth_host, api_host, client_id, client_secret, username, password, apikey)
    customer_manager = CustomerManagement(auth_host, api_host, client_id, client_secret, username, password, apikey)
    entity_documents_manager = EntityDocumentsManagement(auth_host, api_host, client_id, client_secret, username, password, apikey)
    spot_rates_manager = SpotRates(auth_host, api_host, client_id, client_secret, username, password, apikey)
    account_manager = BuckzyAccountManagement(auth_host, api_host, client_id, client_secret, username, password, apikey)
    payout_manager = PayoutTransaction(auth_host, api_host, client_id, client_secret, username, password, apikey)

    # Example usage:
    # try:
    #     # Get all child customers
    #     all_customers = customer_manager.get_all_child_customers()
    #     print("All Customers:", all_customers)

    #     # Get a specific child customer
    #     customer_id = "CUSTOMER_ID"
    #     customer = customer_manager.get_child_customer_by_filter(customer_id)
    #     print("Customer:", customer)

    #     # Get spot rate
    #     spot_rate = spot_rates_manager.get_spot_rate("USD", "EUR", 100)
    #     print("Spot Rate:", spot_rate)

    #     # Get all accounts
    #     all_accounts = account_manager.get_all_accounts()
    #     print("All Accounts:", all_accounts)

    # except Exception as e:
    #     print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()