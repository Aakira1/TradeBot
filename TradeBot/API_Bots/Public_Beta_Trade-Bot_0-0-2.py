import json
import hmac
import hashlib
import requests
import time

class InstrumentFetcher:
    def __init__(self, api_url, public_endpoints):
        self = InstrumentFetcher
        self.api_url = API_URL
        self.public_endpoints = public_endpoints
        self.instrument_names = []
        self.trades = []

#region Obtain Instrument Names
    def fetch_instrument_names(self):
        filtered_endpoints = [endpoint for endpoint in self.public_endpoints if endpoint["method"] == "public/get-instruments"]

        for endpoint in filtered_endpoints:
            endpoint_url = self.api_url + endpoint["method"]
            headers = {
                "Content-Type": "application/json",
                "API-KEY": endpoint.get("api_key"),
                "SIG": endpoint.get("sig"),
                "Nonce": str(endpoint.get("nonce"))
            }

        response = requests.get(endpoint_url, headers=headers)
        
        #partial success
        if response.status_code == 200:
            print("Successfully connected: " + str(response.status_code))
            data = response.json()
            instruments = data["result"]["instruments"]
            for instrument in instruments:
                instrument_name = instrument["instrument_name"]
                self.instrument_names.append(instrument_name)
        else:
            print("Request failed with status code:", response.status_code)
    def Display_InstrumentNames(self):
        for i in self.instrument_names:
            if(i == 'SHIB_USDT'):
                print(True)
#endregion
    
    #def getTicker(self)

    def getTrades(self):
        return

if __name__ == "__main__":
    with open('keys.json') as file:
        calls = json.load(file)

    API_URL = calls['API_URL']
    public_endpoints = calls["public"]

    # Create an instance of InstrumentFetcher
    crypto_names = InstrumentFetcher(API_URL, public_endpoints)

    # Fetch instrument names
    crypto_names.fetch_instrument_names()

    # Print instrument names
    crypto_names.Display_InstrumentNames()

#add an if auth... statement to access user details