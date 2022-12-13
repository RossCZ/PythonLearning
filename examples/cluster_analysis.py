import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


class KMeans:
    def __init__(self, k_clusters, max_iter=100):
        self.k_clusters = k_clusters
        self.max_iter = max_iter
        self.current_iter = 0
        self.centroids = np.empty(0)
        self.clusters = np.empty(0)

    @staticmethod
    def euclidean_distance(point, centroids):
        """Calculate Euclidean distance between point and centroids."""
        return np.sqrt(np.sum((point - centroids) ** 2, axis=1))

    def assign_points_to_clusters(self, points, visualize=True):
        """Assign each datapoint to the nearest centroid."""
        clusters = [[] for _ in range(self.k_clusters)]
        for point in points:
            distances = self.euclidean_distance(point, self.centroids)
            clusters[np.argmin(distances)].append(point)
        self.clusters = [np.array(cluster) for cluster in clusters]
        if visualize:
            self.visualize_clusters()

    def fit(self, X_train):
        """Fit datapoints to K clusters."""
        # initialize centroids: randomly assign to datapoints
        self.centroids = np.array([np.random.default_rng().choice(X_train, axis=0) for _ in range(self.k_clusters)])
        self.assign_points_to_clusters(X_train)

        # iterate until convergence or max_iter limit
        self.current_iter = 0
        prev_centroids = None
        while np.not_equal(self.centroids, prev_centroids).any() and self.current_iter < self.max_iter:
            self.current_iter += 1
            prev_centroids = self.centroids

            # reassign centroids as mean of the points in the cluster
            self.centroids = np.array([np.mean(cluster, axis=0) for cluster in self.clusters])
            self.assign_points_to_clusters(X_train)

    def visualize_clusters(self, keep_open=False):
        """Visualize current clusters with centroids."""
        plt.clf()
        plt.title(f"K-Means clustering (iteration: {self.current_iter})")
        for i, cluster in enumerate(self.clusters):
            plt.scatter(*cluster.T, marker=".", label=f"C{i}")
        plt.scatter(*self.centroids.T, color="k", marker="x", s=50, label="Centroids")
        plt.legend()
        plt.tight_layout()
        if keep_open:
            plt.show()
        else:
            plt.pause(0.5)


def cluster_analysis_example():
    # generate random datapoints in 2D (3 groups)
    samples_a = np.random.normal((12, 14), (3.1, 2.8), (300, 2))
    samples_b = np.random.normal((18, 20), (4.2, 2.8), (300, 2))
    samples_c = np.random.normal((14, 30), (2.3, 4.7), (300, 2))
    samples = np.stack((samples_a, samples_b, samples_c), axis=0).reshape(-1, 2)

    # visualize original data
    # plt.scatter(*samples.T)
    # plt.scatter(*samples_a.T)
    # plt.scatter(*samples_b.T)
    # plt.scatter(*samples_c.T)
    # plt.show()

    # calculate clusters using the K-Means algorithm
    kmeans = KMeans(3)
    kmeans.fit(samples)
    kmeans.visualize_clusters(True)


if __name__ == "__main__":
    # https://en.wikipedia.org/wiki/K-means_clustering
    cluster_analysis_example()
