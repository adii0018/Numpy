# 📊 NumPy Array Methods Cheat Sheet (With Explanation)

## 🔹 1. Basic Info

```python
arr.shape      # Array ka shape batata hai (rows, columns)
arr.ndim       # Array kitne dimensions ka hai (1D, 2D, 3D...)
arr.size       # Total number of elements
arr.dtype      # Data type (int, float, etc.)
```

---

## 🔹 2. Mathematical / Statistical Methods

```python
arr.sum()        # Sab elements ka total sum
arr.mean()       # Average value (mean)
arr.std()        # Standard deviation (data kitna spread hai)
arr.var()        # Variance (std ka square)
arr.min()        # Smallest value
arr.max()        # Largest value
arr.argmin()     # Minimum value ka index
arr.argmax()     # Maximum value ka index
arr.cumsum()     # Cumulative sum (running total)
arr.cumprod()    # Cumulative product (running multiplication)
```

❗ **Note:**

```python
np.median(arr)   # Median (middle value after sorting) — arr ka method nahi hai
```

---

## 🔹 3. Reshaping Methods

```python
arr.reshape(2,5)   # Array ko new shape me convert karta hai (2 rows, 5 cols)
arr.flatten()      # Array ko 1D me convert karta hai (copy banata hai)
arr.ravel()        # Array ko 1D me convert karta hai (view deta hai, fast)
arr.transpose()    # Rows ko columns me convert karta hai
arr.T              # transpose ka shortcut
```

---

## 🔹 4. Sorting & Searching

```python
arr.sort()         # Array ko ascending order me sort karta hai (in-place)
arr.argsort()      # Sorted order ke indices return karta hai
```

🔍 **Search:**

```python
np.where(arr > 10)   # Condition satisfy karne wale elements ke indices deta hai
```

---

## 🔹 5. Indexing / Selection

```python
arr[0]             # First element access
arr[1:5]           # Slicing (index 1 se 4 tak)
arr[arr > 10]      # Boolean indexing (sirf >10 wale elements)
```

---

## 🔹 6. Add / Remove Elements

```python
np.append(arr, 101)     # End me element add karta hai
np.insert(arr, 0, 99)   # Specific index pe element insert karta hai
np.delete(arr, 2)       # Given index ka element delete karta hai
```

---

## 🔹 7. Copy & View

```python
arr.copy()    # Deep copy (original array change nahi hota)
arr.view()    # Shallow copy (original change ho sakta hai)
```

---

## 🔹 8. Type Conversion

```python
arr.astype(float)   # Data type change karta hai (int → float)
```

---

## 🔥 Pro Tip

```python
dir(arr)
```

👉 Array ke saare available methods dikha deta hai

---

## 🚀 Key Learning

* `arr.method()` → Direct array ke methods
* `np.function()` → NumPy ke functions
* Sirf yaad mat karo → **use cases samjho (AI/ML me wahi kaam aata hai)**
