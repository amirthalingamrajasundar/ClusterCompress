import numpy as np

class KMeans:
    def __init__(self, k: int, epsilon: float = 1e-6) -> None:
        self.num_clusters = k
        self.cluster_centers = None
        self.epsilon = epsilon
    
    def _assign_labels(self, X: np.ndarray) -> np.ndarray:
        # Computes distance of each point to each cluster center and assigns the nearest one
        distances = np.linalg.norm(X[:, np.newaxis] - self.cluster_centers, axis=2)
        return np.argmin(distances, axis=1)

    def fit(self, X: np.ndarray, max_iter: int = 100) -> None:
        # Initialize cluster centers 
        # Using K-Means++ to avoid the case where none of the pixels are assigned to some
        # of the clusters, which in turn will result in a division by zero error
        self.cluster_centers = self.kmeans_plus_plus_init(X)

        for _ in range(max_iter):
            # Assign each sample to the closest prototype
            labels = self._assign_labels(X)
            
            # Store the current cluser centers to check for convergence later
            old_centers = np.copy(self.cluster_centers)

            # Update the cluster centers by taking the mean of all points assigned to each cluster
            for i in range(self.num_clusters):
                cluster_points = X[labels == i]
                if len(cluster_points) > 0:
                    self.cluster_centers[i] = np.mean(cluster_points, axis=0)
            
            # Check for convergence
            if np.linalg.norm(self.cluster_centers - old_centers) < self.epsilon:
                break

    
    def predict(self, X: np.ndarray) -> np.ndarray:
        return self._assign_labels(X)
    
    def fit_predict(self, X: np.ndarray, max_iter: int = 100) -> np.ndarray:
        self.fit(X, max_iter)
        return self.predict(X)
    
    def replace_with_cluster_centers(self, X: np.ndarray) -> np.ndarray:
        # Replace each point in X with it's closest cluster center
        labels = self.predict(X)
        return self.cluster_centers[labels]
    
    def kmeans_plus_plus_init(self, X: np.ndarray) -> np.ndarray:
        # Initialize cluster centers using K-Means++
        n_samples, _ = X.shape
        centers = np.zeros((self.num_clusters, X.shape[1]))

        # Choose the first center randomly
        centers[0] = X[np.random.randint(n_samples)]

        # For each remaining center, pick the point with the highest probability of being far away from the existing centers
        for i in range(1, self.num_clusters):
            distances = np.min(np.linalg.norm(X[:, np.newaxis] - centers[:i], axis=2), axis=1)
            # Pick the next center based on the probability distribution proportional to the squared distances
            probabilities = distances**2
            probabilities /= np.sum(probabilities)
            next_center_idx = np.random.choice(n_samples, p=probabilities)
            centers[i] = X[next_center_idx]

        return centers