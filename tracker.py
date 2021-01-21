import os
import time
import requests
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#Global variables 
api_key = os.getenv('api_key')
bot_token = os.getenv('bot_token')
chat_id = os.getenv('chat_id')
limit = 30000
time_interval = 1800

def get_btc_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }
    
    #Send request to the coinmarketcap api
    response = requests.get(url, headers=headers)
    response_json = response.json()

    #Extract the bitcoin price from the json data
    btc_price = response_json['data'][0]

    #Create dict to hold timestamp and price.
    time_and_price = {}
    time_and_price['timestamp'] = response_json['status']['timestamp']
    time_and_price['price'] = btc_price['quote']['USD']['price']

    return time_and_price

#Send_message through telegram.
def send_message(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"

    #Send the msg
    requests.get(url)

#Main function where the magic happens.
def main():

    while True:
        price = get_btc_price()
        price["price"] = round(price["price"], 3)

        #If the price tanks below given limit
        if price['price'] < limit:
            send_message(chat_id=chat_id, msg=f'BTC Price Drop Alert: {price["price"]}')

        #Send message and format to make it look better
        send_message(chat_id=chat_id, msg=f'{price["timestamp"][11:-5]} \n {price["price"]}')
        price = {}

        #Wait before sending new request
        time.sleep(time_interval)

if __name__ == '__main__':
    main()