import requests

API_ENDPOINT="https://btc.aadarshadhakal.com.np/api/bitcoin/latest/"

def get_bitcoin_price():
  try:
    response = requests.get(API_ENDPOINT)
    data = response.json()
    price = data["data"]["BTC"]["quote"]["USD"]["price"]
    return float(price)
  except requests.exceptions.RequestException as e:
    print(f"something wrong with the API!: {e}")
    return None
  except (KeyError, TypeError) as e:
    print(f"Error parsing response data: {e}")
    return None

get_bitcoin_price()