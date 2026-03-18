# np.isinf(array) 10^19999
# 1/0

import numpy as np 

arr=np.array([1,2,np.inf,4,5,np.inf,6])

print(np.isinf(arr))
