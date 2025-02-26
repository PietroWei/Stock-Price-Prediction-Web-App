import yfinance as yf
import pandas as pd

def get_stock_data(symbol, start, end):
    """
    Fetch historical stock data from Yahoo Finance.
    
    Args:
        symbol (str): Stock ticker symbol.
        start (str): Start date (YYYY-MM-DD).
        end (str): End date (YYYY-MM-DD).
    
    Returns:
        pd.DataFrame: Stock data with OHLC and returns.
    """
    stock_data = yf.download(symbol, start=start, end=end)
    stock_data["Return"] = stock_data["Close"].pct_change()
    stock_data.dropna(inplace=True)
    return stock_data
