import os
import pandas as pd
import talib as ta
import plotly.express as px

class FinancialAnalyzer:
    def __init__(self, ticker, data_folder, start_date=None, end_date=None):
        self.ticker = ticker
        self.data_folder = data_folder
        self.start_date = start_date
        self.end_date = end_date
        self.data = self.load_stock_data()
    
    def load_stock_data(self):
        
        file_path = os.path.join(self.data_folder, f"{self.ticker}.csv")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Data file for {self.ticker} not found at {file_path}")
        
        data = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
        
        if self.start_date is None:
            self.start_date = data.index.min()
        if self.end_date is None:
            self.end_date = data.index.max()
        
        data = data[(data.index >= pd.to_datetime(self.start_date)) & 
                    (data.index <= pd.to_datetime(self.end_date))]
        
        if data.empty:
            raise ValueError(f"No data found for {self.ticker} in the specified date range.")
        
        return data
            
    def columns_checker(self, data):
        data.columns = data.columns.str.strip()
        required_columns = ["Open", "High", "Low", "Close", "Volume"]
        if not all(col in data.columns for col in required_columns):
            raise ValueError("The dataset must include Open, High, Low, Close, and Volume columns.")

    def calculate_moving_average(self, data, window_size):
        return ta.SMA(data, timeperiod=window_size)

    def calculate_technical_indicators(self, data):
        data['SMA'] = self.calculate_moving_average(data['Close'], 20)
        data['RSI'] = ta.RSI(data['Close'], timeperiod=14)
        data['EMA'] = ta.EMA(data['Close'], timeperiod=20)
        macd, macd_signal, _ = ta.MACD(data['Close'])
        data['MACD'] = macd
        data['MACD_Signal'] = macd_signal
        data = data.dropna()
        return data

    def plot_stock_data(self, data):
        fig = px.line(data, x=data.index, y=['Close', 'SMA'], title='Stock Price with Moving Average')
        fig.show()

    def plot_rsi(self, data):
        fig = px.line(data, x=data.index, y='RSI', title='Relative Strength Index (RSI)')
        fig.show()

    def plot_ema(self, data):
        fig = px.line(data, x=data.index, y=['Close', 'EMA'], title='Stock Price with Exponential Moving Average')
        fig.show()

    def plot_macd(self, data):
        fig = px.line(data, x=data.index, y=['MACD', 'MACD_Signal'], title='Moving Average Convergence Divergence (MACD)')
        fig.show()
    
