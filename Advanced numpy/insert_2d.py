import numpy as np
arr2d=np.array([[1,2],[3,4]])
print(arr2d)
arr=np.insert(arr2d,1,[12,33] ,axis=0)
print(arr)