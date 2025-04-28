import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math
try:
    from sklearn.cluster import KMeans
except ImportError:
    print('Warning: sklearn not installed, clustering functionality will not work')

# --- Data Loading ---
x = [1.0, 2.0, 3.0, 4.0, 5.0]
y = [2.0, 3.0, 4.0, 5.0, 6.0]
# --- End Data Loading ---

# --- WizUALL Program ---
x_coords = [1.0, 2.0, 3.0, 4.0, 5.0]
y_coords = [2.0, 3.0, 4.0, 5.0, 6.0]
z_coords = np.add(x_coords, y_coords)
w_coords = np.multiply(z_coords, 2.0)
v_coords = np.subtract(w_coords, [1.0, 1.0, 1.0, 1.0, 1.0])
u_coords = np.divide(v_coords, 2.0)
# --- End WizUALL Program ---