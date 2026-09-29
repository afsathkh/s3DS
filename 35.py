import pandas as pd
from scipy.cluster.hierarchy import centroid
from sklearn.cluster import KMeans

data = pd.read_csv("Iris.csv")
print(data.head())
x  = data.iloc[:, 0:4]
print(x.head())
km = KMeans(n_clusters=3, n_init=10, random_state=42)
print(km.fit(x))
y = km.predict(x)
print(y)
centroid = km.cluster_centers_
[print(centroid)]