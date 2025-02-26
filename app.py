import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from utils.stock_data import get_stock_data
from utils.feature_engineering import create_features
from utils.model_comparison import compare_models

# Set up Streamlit page config
st.set_page_config(page_title="Stock Price Prediction", layout="wide")

# Title of the app
st.title("Stock Price Prediction Web App")

# Sidebar for user input
st.sidebar.header("User Input Parameters")

# User selects stock symbol from a dropdown
stock_symbol = st.sidebar.selectbox("Select Stock Symbol", ("AAPL", "GOOG", "MSFT", "AMZN", "TSLA"))

# User selects the time range for training the model
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2015-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2021-01-01"))

# Training model period
st.sidebar.header("Model Training Parameters")
train_period = st.sidebar.slider("Training Period (Days)", 30, 365, 180)

# Fetch the stock data
@st.cache
def load_data(symbol, start, end):
    return get_stock_data(symbol, start, end)

# Show a message while loading data
st.sidebar.text("Loading stock data...")

# Load data
stock_data = load_data(stock_symbol, start_date, end_date)

# Show stock data
st.subheader(f"Stock Data for {stock_symbol}")
st.write(stock_data.tail())

# Feature engineering
st.sidebar.text("Generating features...")
features = create_features(stock_data)

# Model comparison
st.sidebar.text("Training models...")

# Compare machine learning models
models_comparison = compare_models(features, train_period)

# Display model comparison results
st.subheader("Model Performance Comparison")
st.write(models_comparison)

# Plot the results
st.subheader(f"Stock Price Prediction for {stock_symbol}")
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(stock_data.index, stock_data['Close'], label="Actual", color="blue", linewidth=2)
for model_name, prediction in models_comparison.items():
    ax.plot(stock_data.index[train_period:], prediction, label=model_name)
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title(f"Stock Price Prediction for {stock_symbol}")
ax.legend()

# Show plot
st.pyplot(fig)

