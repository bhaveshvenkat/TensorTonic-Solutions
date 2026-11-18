import numpy as np

def euclidean_distance(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    difference = x - y
    return float(np.sqrt(np.sum(difference ** 2)))