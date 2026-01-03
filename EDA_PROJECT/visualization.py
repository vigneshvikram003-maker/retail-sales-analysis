import matplotlib.pyplot as plt
import seaborn as sns

def basic_plots(df):
    plt.figure(figsize=(8, 5))
    plt.hist(df['Sales'], bins=30, edgecolor='black')
    plt.xlabel("Sales")
    plt.ylabel("Frequency")
    plt.title("Sales Distribution")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 5))
    df['Category'].value_counts().plot(kind='bar', edgecolor='black')
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.title("Category-wise Count")
    plt.grid(axis='y')
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(df.index, df['Sales'], marker='o')
    plt.xlabel("Index")
    plt.ylabel("Sales")
    plt.title("Sales Trend")
    plt.grid(True)
    plt.show()


def advanced_plots(df):
    sns.pairplot(df[['Quantity', 'Sales', 'Profit']], diag_kind='kde')
    plt.show()

    plt.figure(figsize=(6, 5))
    corr = df[['Quantity', 'Sales', 'Profit']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()

    