from get_bitcoin_price import get_bitcoin_price
from send_sms import send_sms
import asyncio

TARGET_PRICE = 79500
PRICE_CHECK_INTERVAL = 120

async def monitor_bitcoin_price():
  while True:
    price = get_bitcoin_price()
    if price is not None:
      print(f"current bitcoin price: {price}")

      if price >= TARGET_PRICE:
        message = f"Bitcoin price reached ${price}. Target: ${TARGET_PRICE}"
        send_sms(message)
      else:
        print("Target price is greater than current price.")
    else:
      print("couldn't fetch current price.")
    
    await asyncio.sleep(PRICE_CHECK_INTERVAL)

if __name__ == '__main__':
  asyncio.run(monitor_bitcoin_price())