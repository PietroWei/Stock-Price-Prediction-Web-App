import pandas as pd

def create_features(data):
    """
    Generate technical indicators as features.
    
    Args:
        data (pd.DataFrame): Stock data with OHLC columns.
    
    Returns:
        pd.DataFrame: Data with additional feature columns.
    """
    data["SMA_10"] = data["Close"].rolling(window=10).mean()
    data["SMA_50"] = data["Close"].rolling(window=50).mean()
    data["Volatility"] = data["Close"].pct_change().rolling(window=10).std()
    
    data.dropna(inplace=True)
    return data
