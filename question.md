# 🐍 NumPy + Pandas + Matplotlib — Practice Questions

> Teeno libraries ko milake banaye gaye 20 practice questions.  
> Difficulty levels: Easy ✅ | Medium ⚠️ | Hard 🔥

---

## 📋 Table of Contents

- [Easy Questions (1–6, 11, 20)](#-easy-questions)
- [Medium Questions (7–10, 12, 15, 17)](#-medium-questions)
- [Hard Questions (13, 14, 16, 18, 19)](#-hard-questions)
- [Libraries Quick Reference](#-libraries-quick-reference)

---

## ✅ Easy Questions

### Q1 — NumPy: Even Numbers Statistics
Ek NumPy array banao jisme 1 se 100 tak ke sirf even numbers hon. Phir unka mean, median aur std nikalo.

**Libraries:** `numpy`  
**Hint:** `np.arange()` use karo range ke liye, phir fancy indexing ya filter lagao. `np.mean()`, `np.median()`, `np.std()` use karo.

---

### Q2 — Pandas: DataFrame Exploration
Pandas mein ek CSV load karo (ya dictionary se DataFrame banao) aur dekho: kitni rows/columns hain, koi null values hain kya, aur har column ka data type kya hai.

**Libraries:** `pandas`  
**Hint:** `df.shape`, `df.isnull().sum()`, `df.dtypes` — yeh teeno use karo.

---

### Q3 — Matplotlib + NumPy: sin & cos Plot
Matplotlib se ek simple line chart banao jo `sin(x)` aur `cos(x)` dono ko ek hi plot pe dikhaye, alag alag colors mein, legend ke saath.

**Libraries:** `numpy`, `matplotlib`  
**Hint:** `np.linspace()` se x values banao, `plt.plot()` do baar call karo, `plt.legend()` lagao.

---

### Q4 — NumPy: Matrix Diagonal
Ek 5x5 random integer matrix banao (0–50 range). Phir diagonal elements nikalo aur unka sum karo.

**Libraries:** `numpy`  
**Hint:** `np.random.randint()` se matrix, `np.diag()` se diagonal elements, `.sum()` se total.

---

### Q5 — Pandas + Matplotlib: Sort & Bar Chart
Pandas DataFrame mein ek column ke basis pe sort karo, top 5 rows lo, aur result ko ek bar chart mein dikhao.

**Libraries:** `pandas`, `matplotlib`  
**Hint:** `df.sort_values()` → `df.head(5)` → `df.plot.bar()` ya `plt.bar()`

---

### Q6 — Pandas + NumPy: Student Report Card
Students ka marks data banao (naam + 3 subjects). Har student ka average nikalo, pass/fail column add karo (average >= 40 = Pass), aur pass percentage calculate karo.

**Libraries:** `pandas`, `numpy`  
**Hint:** `df.mean(axis=1)` se row-wise average, `np.where()` se pass/fail column.

---

### Q11 — NumPy: Matrix Multiplication & Transpose
Matrix multiplication ke baare mein: 2 random matrices banao (3x4 aur 4x5), multiply karo, result ka transpose lo, aur verify karo ki shapes sahi hain.

**Libraries:** `numpy`  
**Hint:** `np.dot()` ya `@` operator, `.T` se transpose, `.shape` se verify.

---

### Q20 — NumPy + Pandas + Matplotlib: Performance Comparison
Same task (1 million numbers ka sum) Python loop, NumPy, aur Pandas se karo. `time` module se measure karo aur bar chart mein speedup dikhao.

**Libraries:** `numpy`, `pandas`, `matplotlib`  
**Hint:** `import time; time.time()` se measure karo. NumPy kitna fast hai Python se — yeh dekhna interesting hoga!

---

## ⚠️ Medium Questions

### Q7 — Matplotlib + NumPy: 2x2 Subplot Grid
Matplotlib mein 2x2 subplot grid banao: Line chart, Bar chart, Scatter plot, aur Histogram — sab ek hi figure mein.

**Libraries:** `matplotlib`, `numpy`  
**Hint:** `plt.subplots(2, 2)` use karo, `axes[0][0]` se access karo. `figsize` bhi set karo.

---

### Q8 — Pandas + Matplotlib + NumPy: Rolling Average
Ek time series data banao (365 days ka daily temperature). 7-day rolling average nikalo aur original + rolling average dono plot karo.

**Libraries:** `pandas`, `matplotlib`, `numpy`  
**Hint:** `pd.date_range()` se dates, `df.rolling(7).mean()` se rolling avg, dono lines ek plot pe.

---

### Q9 — NumPy + Matplotlib: Revenue Normalization
Do NumPy arrays lo (prices aur quantities). Total revenue calculate karo, normalize karo (0 to 1 range mein), aur scatter plot banao normalized values ka.

**Libraries:** `numpy`, `matplotlib`  
**Hint:** `revenue = prices * quantities`, normalization = `(x - min) / (max - min)`

---

### Q10 — Pandas + Matplotlib: City-wise Salary
Pandas groupby use karke: city-wise average salary nikalo, usse bar chart mein dikhao, aur sabse zyada salary wali city highlight karo.

**Libraries:** `pandas`, `matplotlib`  
**Hint:** `df.groupby('city')['salary'].mean()` → sort → bar chart → max value ko alag color do.

---

### Q12 — Pandas + Matplotlib: Missing Values Handling
CSV data mein missing values handle karo: numeric columns mein mean se fill karo, categorical mein mode se, phir ek heatmap banao missing values ka (before/after).

**Libraries:** `pandas`, `matplotlib`  
**Hint:** `df.fillna(df.mean())` numeric ke liye, `df.fillna(df.mode().iloc[0])` categorical ke liye. `seaborn` ya `matplotlib` se heatmap.

---

### Q15 — NumPy + Matplotlib: Broadcasting Outer Product
NumPy broadcasting use karke: ek (5,1) aur ek (1,5) array ka outer product banao bina loops ke, phir result plot karo as image (`imshow`).

**Libraries:** `numpy`, `matplotlib`  
**Hint:** `a.reshape(5,1) * b.reshape(1,5)` — broadcasting automatically kaam karega. `plt.imshow()` se visualize.

---

### Q17 — Pandas + Matplotlib: Employee Department Analysis
Pandas mein ek employee dataset banao. Department-wise: average salary, headcount, aur salary distribution (box plot) ek figure mein dikhao.

**Libraries:** `pandas`, `matplotlib`  
**Hint:** `groupby + agg({'salary': ['mean', 'count']})`, phir grouped boxplot ke liye `df.boxplot(by='department')`.

---

## 🔥 Hard Questions

### Q13 — NumPy + Matplotlib: Stock Price Simulation
Stock price simulation: 252 days (1 trading year) ka random walk simulate karo, cumulative returns nikalo, phir multiple simulations (100 runs) ek plot mein dikhao.

**Libraries:** `numpy`, `matplotlib`  
**Hint:** `np.random.normal()` se daily returns, `np.cumprod()` se cumulative. Loop mein 100 simulations karo, sab lines transparent rakhna.

---

### Q14 — Pandas + Matplotlib + NumPy: Sales Pivot Heatmap
Ek sales dataset banao (date, product, region, amount). Multi-level groupby karo (region + product), pivot table banao, aur heatmap se visualize karo.

**Libraries:** `pandas`, `matplotlib`, `numpy`  
**Hint:** `pd.pivot_table()` use karo, `plt.imshow()` ya seaborn heatmap. `plt.colorbar()` mat bhoolna.

---

### Q16 — NumPy + Pandas + Matplotlib: Anomaly Detection
Anomaly detection: ek normal distribution se 1000 points generate karo, phir 20 outliers inject karo. Z-score method se outliers detect karo aur scatter plot mein red dots se mark karo.

**Libraries:** `numpy`, `pandas`, `matplotlib`  
**Hint:** Z-score = `(x - mean) / std`, `|z| > 3` = outlier. Matplotlib mein alag color se plot karo.

---

### Q18 — NumPy + Matplotlib: Gaussian Blur (Manual Convolution)
Image-jaise data banao: 100x100 NumPy array (grayscale image simulate karo). Gaussian blur manually implement karo convolution se aur before/after dikhao.

**Libraries:** `numpy`, `matplotlib`  
**Hint:** `np.random.randint(0,255)` se image, Gaussian kernel banao, `np.convolve` ya `scipy.signal.convolve2d` use karo.

---

### Q19 — NumPy + Pandas + Matplotlib: Multi-Currency Converter
Multi-currency sales data: USD, EUR, INR mein values hain. Sab ko INR mein convert karo (exchange rates NumPy array mein rakho), Pandas mein calculate karo, aur pie + bar chart ek figure mein dikhao.

**Libraries:** `numpy`, `pandas`, `matplotlib`  
**Hint:** `np.array` se rates store karo, `df.apply()` ya vectorized multiplication se convert karo. `plt.subplot()` use karo.

---

## 📚 Libraries Quick Reference

| Library | Kaam | Install |
|---------|------|---------|
| `numpy` | Arrays, math, random, linear algebra | `pip install numpy` |
| `pandas` | DataFrames, CSV, groupby, time series | `pip install pandas` |
| `matplotlib` | Plots, charts, subplots, images | `pip install matplotlib` |

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

---

## 🎯 Suggested Learning Order

1. Pehle **Easy** questions complete karo (Q1–Q6, Q11, Q20)
2. Phir **Medium** try karo — especially Q8 (rolling avg) aur Q10 (groupby)
3. **Hard** mein Q13 (stock sim), Q16 (anomaly), Q19 (multi-currency) sabse interesting hain

---

*Happy Coding! 🚀*