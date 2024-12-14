import pandas as pd

def caluculate_moving_average(data,window):
    return data.rolling(window=window).mean()