'''
### Q3 — Matplotlib + NumPy: sin & cos Plot
Matplotlib se ek simple line chart banao jo `sin(x)` aur `cos(x)` dono ko ek hi plot pe dikhaye, alag alag colors mein, legend ke saath.

**Libraries:** `numpy`, `matplotlib`  
**Hint:** `np.linspace()` se x values banao, `plt.plot()` do baar call karo, `plt.legend()` lagao.

---
'''
import matplotlib.pyplot as plt
import numpy as np

sinx=np.linspace(0,10,100)
cosx=np.linspace(2,20,200)


plt.plot(sinx,color="blue",label="sinx")
plt.plot(cosx,color="red",label="cosx")

plt.xlabel("sinx")
plt.ylabel("cosx")
plt.legend("top left")
plt.title("sin cos table")

plt.show()