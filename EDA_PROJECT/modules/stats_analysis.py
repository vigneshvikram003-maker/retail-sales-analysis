def descriptive_stats(df):
    print(df[['Quantity', 'Sales', 'Profit']].describe())