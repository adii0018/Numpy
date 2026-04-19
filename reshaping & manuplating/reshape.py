'''
kisi bhi dimention ko rehsape karna matlb ... agar 1d arry he toh usko 2d yaah 3d arry bana sakte he ...
isme main data pe effect padta he 
isme row or columns batana hota he requiremnts ke liye 
'''

import numpy as np 

arr_1=np.array([1,2,3,4,5,6])
arr_2=arr_1.reshape(3,2)
arr_3=arr_1.reshape(3,2,1)
print(arr_2)
print("...........................")
print(arr_3)