import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
# Function to get stock data and display graph
def show_stock_graph(symbol):
    # Get stock data
    stock_data = yf.Ticker(symbol)
    # Get company name
    company_name = stock_data.info['longName']
    print(f"Company: {company_name}")
    # Get historical stock prices
    stock_df = stock_data.history(period='1y')  # Adjust the period as needed
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(stock_df['Close'], label='Stock Prices')
    plt.title(f'Stock Prices for {company_name} ({symbol})')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()
# Example usage
stock_symbol = input("Enter the stock symbol: ")
show_stock_graph(stock_symbol)
