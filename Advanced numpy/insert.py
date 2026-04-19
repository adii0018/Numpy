#yah pe np.insert (array ,index,value,asix=None)
#array= orignal array
# agar asix =0 toh yeeh row waise kaam kargea else column wise 
 
import numpy as np 

arr=np.array([1,2,3,4,5])
arr2=np.insert(arr, 5 , 6 , axis=None)
print(arr2)
