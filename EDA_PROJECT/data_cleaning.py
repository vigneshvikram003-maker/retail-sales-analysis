def clean_data(df):
    print("----- NULL VALUES (Before Cleaning) -----")
    print(df.isnull().sum())

    print("\n----- DUPLICATE ROWS (Before Cleaning) -----")
    print(df.duplicated().sum())

    # Fill missing numeric values with mean
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    print("\n----- DUPLICATE ROWS (After Cleaning) -----")
    print(df.duplicated().sum())

    return df

