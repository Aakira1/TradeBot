import json
import hmac
import hashlib
import requests
import time


class APIKeys:
    API_URL = "https://api.crypto.com/v2/"

with open('keys.json') as keys:
    informations = json.load(keys)
    API_KEY = informations['api_key']
    SECRET_KEY = informations['secret_key']

#public function
def get_candlestick(instrument_name, timeframe):
    informations = requests.get(APIKeys.API_URL + "public/get-candlestick?instrument_name="
                                + instrument_name + "&timeframe=" + timeframe)
    informations = json.loads(informations.text)
    return informations['result']['data'][-1]

latest_candlestick_eth_usdt = get_candlestick("BTCUSD-PERP","1m")
print(latest_candlestick_eth_usdt)

#region Function To Read Json Files
# with open("get_instruments.json", "r") as BTCfile:
#     instrument = json.load(BTCfile)
# print("Data: ", type(BTCfile))
# for i in instrument:
#     print(i, instrument[i])
#endregion

#region Get Instruments
""" This is a note header for specific calls
______________________________________________________________________
Name   | Type   | Description of API call
______________________________________________________________________
symbol      | string | e.g specific block coin name type (i.e. BTCUSD-PERP)
inst_type   |
"""
def get_instruments(instrument_name, depth):
    instrument = requests.get(APIKeys.APICalls.API_URL + "public/get-book?instrument_name="+ instrument_name + "&depth=" + depth)
    instrument = json.loads(instrument.text)
    return instrument['result']['data'][-1]

#region Get Trades
"""Get Trades Note
"""
def get_trades(instrument_name, count):
    instrument = requests.get(APIKeys.API_URL + "public/get-trades?instrument_name=" + instrument_name + "&count=" + count)
    instrument = json.loads(instrument.text)
    return instrument['result']['data'][-1]
#endregion

#region Get Ticks
"""Get Ticker Notes"""
def get_ticks(instrument_name):
    informations = requests.get(APIKeys.API_URL + "public/get-tickers?instrument_name=" + instrument_name)
    informations = json.loads(informations.text)
    return informations['result']['data'][-1]

getTick = get_ticks("BTCUSD-PERP")
print(getTick)
#endregion

def UI_get_specifiedInstrument(n):
    return {
        '':1,
    }.get(n, 9)
#print(gtBTC)
#endregion



