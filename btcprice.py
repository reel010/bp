import requests

def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data["bpi"]["USD"]["rate"]
        return price
    else:
        return "Failed to fetch Bitcoin price"

print(f"Current Bitcoin price: ${get_bitcoin_price()} USD")
