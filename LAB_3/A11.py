import pandas as pd
import numpy as np
df = pd.read_excel("test.xlsx", sheet_name="marketing_campaign")
num = df.select_dtypes(include=np.number).fillna(0)
X = num.values
def distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))
def kmeans(data, k=3, max_iter=100):
    centroids = data[:k].copy()
    for _ in range(max_iter):
        clusters = []
        for point in data:
            d = [distance(point, c) for c in centroids]
            clusters.append(np.argmin(d))
        clusters = np.array(clusters)
        new_centroids = []
        for i in range(k):
            pts = data[clusters == i]
            if len(pts) > 0:
                new_centroids.append(np.mean(pts, axis=0))
            else:
                new_centroids.append(centroids[i])
        new_centroids = np.array(new_centroids)
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    return clusters, centroids
labels, centroids = kmeans(X, 3)
print("Cluster Labels")
print(labels)
print("\nCentroids")
print(centroids)