# jab bhi hame type change karna ho  tab ham .astype()  use karte he jisme () bracket ke andar new wala data type pass karan hota he 

import numpy as np
arr=np.array([12,22,22.5])
print(arr.dtype)
# aab type change hoga 
arr_1=arr.astype(int)
print(arr_1.dtype)
