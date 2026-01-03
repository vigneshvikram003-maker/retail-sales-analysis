from sklearn.preprocessing import StandardScaler
import pandas as pd

def scale_data(df):
    scaler = StandardScaler()
    cols = ['Quantity', 'Sales', 'Profit']
    scaled_array = scaler.fit_transform(df[cols])
    scaled_df = pd.DataFrame(scaled_array, columns=cols)
    
    print("Scaled Data (first 5 rows):")
    print(scaled_df.head())
    
    return scaled_df

