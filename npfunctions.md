# 📊 NumPy Functions Cheat Sheet (With Explanation)

## 🔹 1. Array Creation Functions

```python
np.array([1,2,3])        # Python list ko NumPy array me convert karta hai
np.zeros((2,3))          # 2x3 array jisme sab 0 honge
np.ones((2,3))           # 2x3 array jisme sab 1 honge
np.arange(1,10,2)        # Range generate karta hai (start, stop, step)
np.linspace(0,1,5)       # 0 se 1 tak 5 equally spaced numbers
np.eye(3)                # Identity matrix (diagonal = 1)
np.random.rand(2,2)      # Random values (0 to 1)
np.random.randint(1,10)  # Random integer between 1 and 10
```


---

## 🔹 2. Mathematical Functions

```python
np.sum(arr)        # Total sum
np.mean(arr)       # Average value
np.std(arr)        # Standard deviation
np.var(arr)        # Variance
np.min(arr)        # Minimum value
np.max(arr)        # Maximum value
np.sqrt(arr)       # Square root
np.exp(arr)        # e^x (exponential)
np.log(arr)        # Natural log (ln)
np.abs(arr)        # Absolute value
```

---

## 🔹 3. Statistical Functions

```python
np.median(arr)     # Middle value (after sorting)
np.percentile(arr, 50)  # 50th percentile (same as median)
np.corrcoef(arr1, arr2) # Correlation between arrays
```

---

## 🔹 4. Array Manipulation Functions

```python
np.reshape(arr, (2,5))   # Shape change karta hai
np.ravel(arr)            # 1D array me convert karta hai
np.transpose(arr)        # Rows ↔ Columns swap karta hai
np.concatenate([a,b])    # Arrays ko jodta hai
np.split(arr, 2)         # Array ko parts me todta hai
```

---

## 🔹 5. Searching & Sorting Functions

```python
np.where(arr > 10)   # Condition satisfy karne wale indices
np.sort(arr)         # Sorted array return karta hai
np.argsort(arr)      # Sorted indices return karta hai
```

---

## 🔹 6. Linear Algebra Functions

```python
np.dot(a,b)          # Dot product
np.matmul(a,b)       # Matrix multiplication
np.linalg.inv(a)     # Matrix inverse
np.linalg.det(a)     # Determinant
np.linalg.eig(a)     # Eigenvalues & eigenvectors
```

---

## 🔹 7. Random Functions

```python
np.random.rand(3,3)        # Random floats (0–1)
np.random.randn(3,3)       # Random normal distribution
np.random.randint(1,10,5)  # Random integers
np.random.seed(42)         # Same random results (reproducibility)
```

---

## 🔹 8. Useful Utility Functions

```python
np.unique(arr)      # Unique elements
np.clip(arr, 0, 10) # Values ko limit karta hai (0–10)
np.round(arr, 2)    # Round to 2 decimal places
```

---

## 🔥 Key Learning

* `np.function()` → NumPy ke global functions hote hain
* Ye arrays pe operate karte hain
* AI/ML me inka heavy use hota hai

---

## 🚀 Pro Tip

👉 Same kaam kai baar 2 tarike se hota hai:

```python
arr.mean()   # Method
np.mean(arr) # Function
```

👉 But har function ka method version nahi hota:

```python
np.median(arr)  # ✔️
arr.median()    # ❌
```
