# hsplit()
# vsplit()

import numpy as np 

arr=np.array([[10,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]])
a1=np.hsplit(arr,2)
a2=np.vsplit(arr,2)
print(a1)
print(a2)