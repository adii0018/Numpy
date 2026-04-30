'''### Q4 — NumPy: Matrix Diagonal
Ek 5x5 random integer matrix banao (0–50 range). Phir diagonal elements nikalo aur unka sum karo.

**Libraries:** `numpy`  
**Hint:** `np.random.randint()` se matrix, `np.diag()` se diagonal elements, `.sum()` se total.
'''

import numpy as np 

# 5x5 random integer matrix (0–50 range)
matrix =np.random.randint(0,51,(5,5))
print("matrix\n",matrix)

# diagonal elements
diagonal =np.diag(matrix)
print("diagonal >>\n", diagonal)

# sum of diagonal elements
diagonal_sum=np.sum(diagonal)
print('diagonal_sum>>',diagonal_sum)