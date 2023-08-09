import ccxt
import tkinter as tk

# Initialize the exchange API
exchange = ccxt.binance({
    'apiKey': 'jdMHj1ZcU8g1eodVx6F5Jd',
    'secret': 'V6wPpswWDrRMLDE29bLd7n',
})

# Define the trading parameters
symbol = 'BTC/USDT'
amount = 0.01
buy_threshold = 10000
sell_threshold = 11000

# Place a buy order
def place_buy_order():
    print('Placing buy order...')
    try:
        order = exchange.create_market_buy_order(symbol, amount)
        print('Buy order placed:', order)
    except Exception as e:
        print('Failed to place buy order:', str(e))

# Place a sell order
def place_sell_order():
    print('Placing sell order...')
    try:
        order = exchange.create_market_sell_order(symbol, amount)
        print('Sell order placed:', order)
    except Exception as e:
        print('Failed to place sell order:', str(e))

# Check the current price
def get_current_price():
    ticker = exchange.fetch_ticker(symbol)
    return ticker['close']

# Main trading loop
def trade():
    price = get_current_price()
    print('Current price:', price)

    if price < buy_threshold:
        place_buy_order()
    elif price > sell_threshold:
        place_sell_order()

    # Add additional conditions or trading strategies here

    root.after(60000, trade)  # Adjust the interval as per your needs

# GUI Setup
root = tk.Tk()
root.title("Crypto Trading Bot")

# Current price label
price_label = tk.Label(root, text="Current Price: ")
price_label.pack()

# Start trading button
start_button = tk.Button(root, text="Start Trading", command=trade)
start_button.pack()

root.mainloop()
