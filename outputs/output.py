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
input = np.array([5.0, 10.0, 15.0, 20.0, 25.0])
# --- End Data Loading ---

# --- WizUALL Program ---
input_coords = [5.0, 10.0, 15.0, 20.0, 25.0]
shifted_coords = np.subtract(input_coords, [2.0, 2.0, 2.0, 2.0, 2.0])
doubled_coords = np.multiply(shifted_coords, 2.0)
x_data = input_coords if isinstance(input_coords, (list, np.ndarray)) else [input_coords]
y_data = doubled_coords if isinstance(doubled_coords, (list, np.ndarray)) else [doubled_coords]
plt.figure()
plt.scatter(x_data, y_data)
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig(os.path.join(OUTPUT_DIR, 'scatter.png'))
plt.close()
# --- End WizUALL Program ---