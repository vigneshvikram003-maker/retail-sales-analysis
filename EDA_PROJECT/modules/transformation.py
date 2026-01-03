from sklearn.preprocessing import StandardScaler

def scale_data(df):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[['Quantity', 'Sales', 'Profit']])
    return scaled