import requests

class CurrencyConverter:
    def __init__(self):
        self.api_key = 'b7b74489826c416dec46cfcb420f9b47'  # Your actual API key
        self.api_url = f"https://api.exchangeratesapi.io/latest?access_key={self.api_key}"

    def get_rates(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json().get("rates")
        else:
            print(f"Error: {response.status_code}")  # Print error status
            return None

    def convert(self, amount, from_currency, to_currency):
        rates = self.get_rates()
        if rates and from_currency in rates and to_currency in rates:
            amount_in_base = amount / rates[from_currency]
            return amount_in_base * rates[to_currency]
        return None

