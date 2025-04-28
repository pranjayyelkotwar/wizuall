import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define output directory relative to project root
OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'outputs'))
os.makedirs(OUTPUT_DIR, exist_ok=True)

try:
    from sklearn.cluster import KMeans
except ImportError:
    print('Warning: sklearn not installed, clustering functionality will not work')


def ensure_numpy_array(data):
    """Ensure the input data is a numpy array."""
    return np.array(data) if not isinstance(data, np.ndarray) else data


def save_plot(filename):
    """Save the current matplotlib plot to the output directory."""
    plt.savefig(os.path.join(OUTPUT_DIR, filename))
    plt.close()


def histogram(data, bins=10):
    """Generate and save a histogram plot."""
    data = ensure_numpy_array(data)
    plt.figure()
    plt.hist(data, bins=int(bins))
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    save_plot('histogram.png')


def scatter(x_data, y_data):
    """Generate and save a scatter plot."""
    x_data = ensure_numpy_array(x_data)
    y_data = ensure_numpy_array(y_data)
    plt.figure()
    plt.scatter(x_data, y_data)
    plt.title('Scatter Plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    save_plot('scatter.png')


def plot(x_data, y_data):
    """Generate and save a line plot."""
    x_data = ensure_numpy_array(x_data)
    y_data = ensure_numpy_array(y_data)
    plt.figure()
    plt.plot(x_data, y_data)
    plt.title('Line Plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    save_plot('plot.png')


def reverse(data):
    """Reverse the input data."""
    data = ensure_numpy_array(data)
    reversed_data = data[::-1]
    print('Reversed:', reversed_data)
    return reversed_data


def slice(data, start=0, end=None):
    """Slice the input data."""
    data = ensure_numpy_array(data)
    end = len(data) if end is None else end
    sliced_data = data[int(start):int(end)]
    print('Sliced:', sliced_data)
    return sliced_data


def cluster(data, n_clusters=2):
    """Perform KMeans clustering on the input data."""
    data = ensure_numpy_array(data)
    try:
        data_reshaped = data.reshape(-1, 1)
        kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data_reshaped)
        labels = kmeans.labels_
        print('Cluster Labels:', labels)
        return labels
    except ImportError:
        print('Warning: sklearn not available, clustering skipped')
        return np.zeros(len(data), dtype=int)