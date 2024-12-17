import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def load_data_with_parse(file_path, parse_dates=None):
    return pd.read_csv(file_path, parse_dates=None)

def load_csv_files(file_paths, stock_names):
    dataframes = []
    for file_path, stock in zip(file_paths, stock_names):
        df = pd.read_csv(file_path)
        df["Stock"] = stock  
        dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True)
