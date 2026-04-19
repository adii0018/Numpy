# shape se haam shape check kar sakte he kisi bhi array ka yaha pe .shape use hoata he print ke andar 

import numpy as np 

arr_1=np.array([12,22,33])

arr_2=np.array([[12,22,33],
               [12,12,42]])

arr_3=np.array([
    [
        [13,13,44],
        [21,31,31]
    ],
    [
        [21,31,31],
        [13,13,44]
    ]
    ])

print(arr_1.shape)
print(arr_2.shape)
print(arr_3.shape)