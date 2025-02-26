# Stock Price Prediction Web App

![Stock Price Prediction Logo](logo.webp)

A web app to predict stock prices using machine learning algorithms such as Random Forest and Linear Regression.
The app compares the performance of different models and visualizes predicted vs actual stock prices.

## Features
- **Stock Data Retrieval**: Fetches historical stock prices from Yahoo Finance.
- **Feature Engineering**: Transforms raw stock data into meaningful features for prediction.
- **Model Training & Comparison**: Implements and compares multiple machine learning models.
- **Interactive UI**: Allows users to select stocks, adjust parameters, and visualize predictions.
- **Performance Metrics**: Evaluates models using RMSE and other relevant metrics.

## Technologies Used
- **Python**: Core programming language for backend logic.
- **Streamlit**: For building an interactive web interface.
- **yfinance**: To retrieve stock market data.
- **scikit-learn**: For machine learning model implementation.
- **pandas**: Data manipulation and preprocessing.
- **matplotlib**: Visualization of stock trends and predictions.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/stock-price-prediction.git
   cd stock-price-prediction
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the web app in your browser.
2. Select a stock symbol from the dropdown menu.
3. Choose a time range for data analysis.
4. Adjust model training parameters as needed.
5. View the predictions and compare model performance.

## Example Output
![Stock Prediction Example](example_output.png)

## Future Improvements
- Add support for deep learning models (LSTMs, RNNs).
- Implement more advanced feature engineering techniques.
- Enhance the UI with additional visualizations and insights.
- Deploy the app on a cloud platform for public access.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

