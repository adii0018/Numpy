
#Ek NumPy array banao jisme 1 se 100 tak ke sirf even numbers hon. Phir unka mean, median aur std nikalo.

import numpy as np

arr=np.arange(2,101,2)

print("mean >",arr.mean())

print("median >",np.median(arr))

print("std >",arr.std())

