from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

def kmeans_cluster(df, scaled_data):
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(scaled_data)

    sns.scatterplot(x=df['Sales'], y=df['Profit'], hue=df['Cluster'])
    plt.title("K-Means Clustering")
    plt.show()

    return df