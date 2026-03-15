# jab bhi kisi arry ke anadar kitne element he yeeh check karan ho toh print ke andar .size use karan hoga 

import numpy as np 
 
arr_1=np.array([13,31,33])

arr_2=np.array([
    [12,32,33],
    [23,21,12]
    ])

arr_3=np.array([
    [
        [11,22,21],
        [12,21,31]
    ],
    [
        [12,21,34],
        [21,21,22]
    ]
])
print(arr_1.size)
print(arr_2.size)
print(arr_3.size)
