from quadriga import QuadrigaClient

from API_setup import APISetup


def main():

    API_setup = APISetup()

    # Initialize the QuadrigaCX client
    client = QuadrigaClient(
        api_key=API_setup.client['api_key'],
        api_secret=API_setup.client['api_secret'],
        client_id=API_setup.client['client_id'],
        default_book=API_setup.client['default_book']
    )

    summary = client.get_summary()

    balance = client.get_balance()
    pass

if __name__ == "__main__":
    main()