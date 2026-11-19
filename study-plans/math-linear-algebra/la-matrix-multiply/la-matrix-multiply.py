import numpy as np

def matrix_multiply(A: list, B: list) -> np.ndarray:
    """
    Returns the matrix product as a float64 array.
    """
    A_array = np.asarray(A, dtype=np.float64)
    B_array = np.asarray(B, dtype=np.float64)
    return A_array @ B_array