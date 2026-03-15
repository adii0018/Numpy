# jab bhi kisi arry ke anadar ka dimention check karan ho toh .ndim use karan hoga print ke andar n dim ka matalb hota e number of dimentions 

# arry ka dimention pata karan ho tab yeeh use karte he  

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
print(arr_1.ndim)
print(arr_2.ndim)
print(arr_3.ndim)
