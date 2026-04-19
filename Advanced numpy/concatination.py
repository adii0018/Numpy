#np.concatination((arr1,arr2),asix=0)
import numpy as np

arr1=np.array([1,3,4])
arr2=np.array([8,5,9])

arr3=np.concatenate((arr1,arr2),axis=0)

print(arr3) 