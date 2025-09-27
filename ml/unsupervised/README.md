# Unsupervised Learning

## Definition
Unsupervised learning deals with **unlabeled datasets**, where the goal is to **find hidden patterns or structures** in the data.

## Applications
1. **Clustering** – Group similar data points together
2. **Association** – Find rules and relationships among variables (e.g., Market Basket Analysis, Apriori Algorithm)
3. **Dimensionality Reduction** – Reduce the number of features while preserving information (e.g., PCA)

---

## 1️⃣ Clustering

Clustering is the task of **grouping similar data points** into clusters.

### Types of Clustering Algorithms

#### A. K-Means and K-Means++

- Used for solving clustering problems where **k = number of clusters** is predefined
- Each cluster has a **centroid** (center position)
  - Example:
    - 1 cluster → 1 centroid  
    - 3 clusters → 3 centroids

**Example:** On a 2D plane (x-y)
- Red cluster (A)
- Blue cluster (B) 
- Brown cluster (C)

**Distance calculation:** Euclidean distance is commonly used:

```
d = √[(x₂ - x₁)² + (y₂ - y₁)²]
```

**Other distance metrics:** Manhattan, Minkowski, Cosine, Hamming. Google Maps uses **Haversine formula** for geospatial distances.

##### Drawbacks of K-Means:
- Sensitive to **outliers** (points far from cluster)
- Requires predefining **k**

##### How to define k?
Using **WCSS (Within Cluster Sum of Squares)** or **Elbow Method**

### WCSS (Within Cluster Sum of Squares)

- **Intra-cluster distance:** Distance from centroid to points in the cluster
- **Inter-cluster distance:** Distance from centroid of one cluster to points of another cluster
- **Inertia (WCSS):**

```
WCSS = Σ(clusters) Σ(points) [distance(point, centroid)]²
```

### Elbow Method

- Plot **WCSS vs k**
- WCSS decreases as k increases (inversely proportional)
- **Elbow point:** The value of k after which WCSS decreases very slowly → optimal number of clusters

### Cluster Validation Metrics

#### 1. Dunn Index:
- Measures **cluster separation / intra-cluster distance**
- Higher Dunn index → better clustering

#### 2. Silhouette Score:
- Measures how similar a point is to its own cluster vs other clusters

```
SS = (b - a) / max(a, b)
```

Where:
- **a** = intra-cluster distance (mean distance to points in the same cluster)
- **b** = inter-cluster distance (mean distance to points in the nearest cluster)

**Interpretation:**
- SS = 1 → Perfect clustering
- SS = 0 → OK clustering  
- SS = -1 → Wrong clustering

### K-Means++
- Improvement over K-Means
- Better initialization of centroids → faster convergence & better results

---

#### B. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

- Clusters based on **density of points**
- Can detect **noise/outliers**
- Does **not require k**
- Good for **arbitrary-shaped clusters**

---

#### C. Hierarchical Clustering

- Builds a **tree-like structure (dendrogram)** of clusters

**Types:**

1. **Agglomerative (Bottom-Up):**
   - Each point starts as a single cluster → merged iteratively
   - Linkage types:
     - **Single link (minimum distance)**
     - **Complete link (maximum distance)**
     - **Group average**
     - **Ward's method** (minimizes variance)

2. **Divisive (Top-Down):**
   - Start with all points in one cluster → divide iteratively

---

## 2️⃣ Dimensionality Reduction

- Reduces **number of features** while preserving most information
- Example: **PCA (Principal Component Analysis)**

---

## 3️⃣ Association

- Finds **relationships between variables**
- Common algorithms:
  - **MBA (Market Basket Analysis)**
  - **Apriori Algorithm**

---

## ✅ Summary Table

| Problem Type | Example Techniques | Notes |
|--------------|-------------------|-------|
| **Clustering** | K-Means, K-Means++, DBSCAN, Hierarchical | Group similar data points |
| **Dimensionality Reduction** | PCA | Reduce features, keep important info |
| **Association** | MBA, Apriori | Find relationships among items |

---

## Key Takeaways

- **Clustering** groups similar data points without labels
- **K-Means** requires predefined k, sensitive to outliers
- **DBSCAN** handles noise and arbitrary shapes
- **Hierarchical clustering** creates tree-like structures
- **Validation metrics** help evaluate clustering quality
- **Dimensionality reduction** preserves information with fewer features
- **Association** discovers hidden relationships in data