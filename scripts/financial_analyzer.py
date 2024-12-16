import yfinance as yf
import pandas as pd
import talib as ta
import numpy as np
import plotly.express as px
from pynance.data import Indicators

class FinancialAnalyzer:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date 
        self.end_date = end_date
    
    def calculate_moving_average(self, data, window_size):
        return ta.SMA(data,timeperiod= window_size)
    
    def calculate_technical_indicators(self, data):
        data['SMA'] = self.calculate_moving_average(data['Close'],20)
        data['RSI'] = ta.RSI(data['Close'], timeperiod = 14)
        data['EMA'] = ta.EMA(data['Close'], timeperiod = 20)
        macd, macd_signal, _ = ta.MACD(data['Close'])
        data['MACD'] = macd
        data['MACD_Signal'] = macd_signal
        return data
    def plot_stock_data(self, data):
        fig = px.line(data, x=data.index, y=['Close','SMA'], title='Stock Price with Moving Average')
        fig.show()
    def plot_rsi(self, data):
        fig = px.line(data, x=data.index, y='RSI', title='Relative Strength Index (RSI)')
        fig.show()
    def plot_ema(self, data):
        fig = px.line(data, x=data.index, y=['Close','EMA'], title='Stock Price with Exponencial Moving Average')
        fig.show()
    def plot_macd(self, data):
        fig = px.line(data, x=data.index, y=['MACD','MACD_Signal'], title='Moving Average Convergence Divergence with Moving Average Convergence Divergence Signal')
        fig.show()
   