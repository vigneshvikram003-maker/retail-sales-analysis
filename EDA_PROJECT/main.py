from modules.data_import import load_data
from modules.data_cleaning import clean_data
from modules.transformation import scale_data
from modules.stats_analysis import descriptive_stats
from modules.visualization import basic_plots, advanced_plots
from modules.modeling import kmeans_cluster

# Load data
print("First Five Rows of Dataset")
df = load_data()

# Clean data
print("Dataset Structure")
df = clean_data(df)

# Export backup
print("Cleaned Dataset Saved as retail_sales_backup.csv")
df.to_csv("outputs/retail_sales_backup.csv", index=False)

# Statistics
print("Descriptive Statistics")
descriptive_stats(df)

#scaled data
print("Stardardized Data")
print(scale_data(df))


# Visualizations
basic_plots(df)
advanced_plots(df)

# Scaling & Clustering
scaled_data = scale_data(df)
df = kmeans_cluster(df, scaled_data)

print("EDA Project Completed Successfully")
