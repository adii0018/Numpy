import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Column-wise mean
print(np.mean(arr, axis=0))

# Row-wise mean
print(np.mean(arr, axis=1))