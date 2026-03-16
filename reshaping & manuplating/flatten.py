# .revel() -> view banata he yeeh main dat ako iffect karat he 
# .flatten() -> copy karat he main dat ame se 
# yeeh sab tab use hite he jab hamko multidimention arry  ko 1d array me convert karna hoat he 

import numpy as np

arr_1=np.array([[11,21,12],[13,12,11]])

print(arr_1.ravel())
print(arr_1.flatten())