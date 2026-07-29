import numpy as np
def minkowski_distance(a, b, p):
    a = np.array(a)
    b = np.array(b)
    return np.sum(np.abs(a - b) ** p) ** (1 / p)
A = [2, 4, 6]
B = [1, 3, 5]
print("Manhattan:", minkowski_distance(A, B, 1))
print("Euclidean:", minkowski_distance(A, B, 2))