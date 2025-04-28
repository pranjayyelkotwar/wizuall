import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math
try:
    from sklearn.cluster import KMeans
except ImportError:
    print('Warning: sklearn not installed, clustering functionality will not work')

OUTPUT_DIR = '/Users/pranjayyelkotwar/Desktop/3-2/CC/project_final/outputs'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Data Loading ---
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([2.0, 3.0, 5.0, 7.0, 6.0])
# --- End Data Loading ---

# --- WizUALL Program ---
x_coords = [1.0, 2.0, 3.0, 4.0, 5.0]
y_coords = [2.0, 3.0, 5.0, 7.0, 6.0]
data = x_coords if isinstance(x_coords, (list, np.ndarray)) else [x_coords]
plt.figure()
plt.hist(data, bins=int(5.0))
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig(os.path.join(OUTPUT_DIR, 'histogram.png'))
plt.close()
x_data = x_coords if isinstance(x_coords, (list, np.ndarray)) else [x_coords]
y_data = y_coords if isinstance(y_coords, (list, np.ndarray)) else [y_coords]
plt.figure()
plt.scatter(x_data, y_data)
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig(os.path.join(OUTPUT_DIR, 'scatter.png'))
plt.close()
x_data = x_coords if isinstance(x_coords, (list, np.ndarray)) else [x_coords]
y_data = y_coords if isinstance(y_coords, (list, np.ndarray)) else [y_coords]
plt.figure()
plt.plot(x_data, y_data)
plt.title('Line Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig(os.path.join(OUTPUT_DIR, 'plot.png'))
plt.close()
# --- End WizUALL Program ---