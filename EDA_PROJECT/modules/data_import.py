import pandas as pd

def load_data():
    df = pd.read_csv("retail_sales5.csv", encoding="latin1")
    print(df.head())
    print(df.info())
    return df