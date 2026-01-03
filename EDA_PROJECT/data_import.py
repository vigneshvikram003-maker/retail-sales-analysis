import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

df = load_data("data.csv")
print("first five rows")
print(df.head())
print("information of data")
print(df.info())
