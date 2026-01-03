import matplotlib.pyplot as plt
import seaborn as sns

def basic_plots(df):
    plt.hist(df['Sales'], bins=30)
    plt.title("Sales Distribution")
    plt.show()

    df['Category'].value_counts().plot(kind='bar')
    plt.title("Category Count")
    plt.show()

def advanced_plots(df):
    sns.pairplot(df[['Quantity', 'Sales', 'Profit']])
    plt.show()

    sns.heatmap(df[['Quantity', 'Sales', 'Profit']].corr(), annot=True)
    plt.show()