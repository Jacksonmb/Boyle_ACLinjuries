import kagglehub

# Download latest version
path = kagglehub.dataset_download("ziya07/athlete-injury-and-performance-dataset")
print(path)

df = pd.read("ziya07/athlete-injury-and-performance-dataset")
print(df.head())