# Import modules
import yfinance as yf
import pandas as pd


class ESFuturesCollector:
    def __init__(self):
        self.symbol = "ES=F"

    """Fetch S&P 500 futures OHLCV data"""
    def fetch_data(self, period, interval):
        try:
            # Gets the data
            ticker = yf.Ticker(self.symbol)
            data = ticker.history(period, interval)

            # Prints statistics about data
            print(f"Fetched {len(data)} rows of data")
            print(f"Date range: {data.index[0]} to {data.index[-1]}")
            
            return data
            
        except Exception as e:
            # Return possible errors
            print(f"Error fetching data: {e}")
            return None
        
    """Validate that data was extracted"""
    def validate_data(self, data):
        # Check if data exists
        if data is None or data.empty:
            return False
        # Check if trading occured
        if data["Volume"].sum() == 0:
            return False
        return True
    
    """Clean data for trading days"""
    def clean(self, data):
        return data[data["Volume"] != 0]
    

# Test the collector with specified timeframe
if __name__ == "__main__":
    collector = ESFuturesCollector()
    data = collector.fetch_data("1y", "1d")  # 1 year timeframe, daily candles
    
    if collector.validate_data(data):
        print(data.head())  # Show first 5 rows
        print(f"Current ES price: ${data["Close"].iloc[-1]:.2f}")  # Print the last closing price 2dp
