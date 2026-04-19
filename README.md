# 🚀 NumPy Mastery Hub

<div align="center">

![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

**A comprehensive collection of NumPy tutorials, examples, and practice problems**

[Getting Started](#-getting-started) • [Features](#-features) • [Project Structure](#-project-structure) • [Practice Questions](#-practice-questions) • [Contributing](#-contributing)

</div>

---

## 📖 About

Welcome to **NumPy Mastery Hub** — your one-stop resource for mastering NumPy from basics to advanced concepts! This repository contains hands-on examples, real-world use cases, and challenging practice problems to help you become proficient in numerical computing with Python.

Whether you're a beginner starting your data science journey or an experienced developer looking to sharpen your NumPy skills, this repository has something for everyone.

---

## ✨ Features

- 📚 **Structured Learning Path** — From basics to advanced topics
- 💡 **Hands-on Examples** — Real code snippets you can run immediately
- 🎯 **Practice Questions** — 20+ curated problems with varying difficulty levels
- 🔥 **Performance Optimization** — Learn vectorization and broadcasting
- 📊 **Data Manipulation** — Master array operations, reshaping, and indexing
- 🧮 **Mathematical Operations** — Statistical functions, linear algebra, and more
- 🌟 **Best Practices** — Industry-standard coding patterns

---

## 🗂️ Project Structure

```
📦 NumPy-Mastery-Hub
├── 📁 Intro/                          # Getting started with NumPy basics
│   ├── 01.py - 12.py                  # Fundamental concepts & array creation
│
├── 📁 arr property/                   # Array properties & attributes
│   ├── dtype.py                       # Data types
│   ├── shape.py                       # Array dimensions
│   ├── ndim.py                        # Number of dimensions
│   ├── size.py                        # Total elements
│   ├── math.py                        # Mathematical operations
│   └── aggrigation.py                 # Aggregation functions
│
├── 📁 indexing & slicing/             # Data access techniques
│   ├── access.py                      # Basic indexing
│   ├── slicing.py                     # Array slicing
│   ├── fancy.py                       # Fancy indexing
│   └── filtering.py                   # Boolean indexing
│
├── 📁 reshaping & manuplating/        # Array transformation
│   ├── reshape.py                     # Changing array shape
│   └── flatten.py                     # Flattening arrays
│
├── 📁 Advanced numpy/                 # Advanced operations
│   ├── append.py                      # Adding elements
│   ├── insert.py & insert_2d.py       # Inserting elements
│   ├── remove.py & remove_2d.py       # Removing elements
│   ├── concatination.py               # Joining arrays
│   ├── spliting.py                    # Splitting arrays
│   └── stacking.py                    # Stacking arrays
│
├── 📁 broadcasting/                   # Broadcasting rules & examples
│   ├── single.py                      # Single value broadcasting
│   ├── 1d_to_2d.py                    # 1D to 2D broadcasting
│   ├── problm.py & solution.py        # Common issues & fixes
│
├── 📁 Vectorization/                  # Performance optimization
│   ├── 01.py                          # Vectorization basics
│   ├── fast.py & fast2.py             # Speed comparisons
│
├── 📁 matrix/                         # Matrix operations
│   ├── 01.py & 02.py                  # Matrix arithmetic & algebra
│
├── 📁 handling and missing values/    # Data cleaning
│   ├── isnan.py                       # Detecting NaN values
│   ├── nan_to_num.py                  # Converting NaN
│   ├── replace.py                     # Replacing values
│   └── infinite.py                    # Handling infinity
│
├── 📁 Q🍃/                            # Practice problems & solutions
│   ├── 01.py & 02.py                  # Solved examples
│   └── q.csv                          # Sample dataset
│
├── 📄 npfunctions.md                  # NumPy functions cheat sheet
├── 📄 arrymethods.md                  # Array methods reference
└── 📄 question.md                     # 20+ practice questions
```

---

## 🎯 Learning Path

### 1️⃣ Beginner Level
Start here if you're new to NumPy:
- **Intro/** — Array creation, basic operations
- **arr property/** — Understanding array attributes
- **indexing & slicing/** — Accessing and manipulating data

### 2️⃣ Intermediate Level
Build on the basics:
- **reshaping & manuplating/** — Transform array structures
- **Advanced numpy/** — Insert, append, concatenate operations
- **matrix/** — Matrix arithmetic and operations

### 3️⃣ Advanced Level
Master performance and complex operations:
- **broadcasting/** — Efficient array operations
- **Vectorization/** — Speed up your code 100x
- **handling and missing values/** — Real-world data cleaning

---

## 📝 Practice Questions

This repository includes **20+ practice questions** covering NumPy, Pandas, and Matplotlib integration:

### Difficulty Levels:
- ✅ **Easy** (8 questions) — Perfect for beginners
- ⚠️ **Medium** (7 questions) — Intermediate challenges
- 🔥 **Hard** (5 questions) — Advanced problem-solving

### Topics Covered:
- Statistical analysis & aggregations
- Data visualization with Matplotlib
- Broadcasting & vectorization
- Matrix operations & linear algebra
- Time series analysis
- Anomaly detection
- Performance optimization

📄 **Full question list:** [question.md](question.md)

---

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.7+
```

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/numpy-mastery-hub.git
cd numpy-mastery-hub
```

2. Install NumPy
```bash
pip install numpy
```

3. (Optional) Install additional libraries for practice questions
```bash
pip install pandas matplotlib
```

### Running Examples

```bash
# Run any example file
python "Intro/01.py"

# Or navigate to specific folders
cd "Advanced numpy"
python append.py
```

---

## 📚 Quick Reference

### Essential NumPy Functions

| Category | Functions |
|----------|-----------|
| **Array Creation** | `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()` |
| **Math Operations** | `np.sum()`, `np.mean()`, `np.std()`, `np.min()`, `np.max()` |
| **Array Manipulation** | `np.reshape()`, `np.flatten()`, `np.transpose()`, `np.concatenate()` |
| **Indexing** | Boolean indexing, Fancy indexing, Slicing |
| **Linear Algebra** | `np.dot()`, `np.matmul()`, `np.linalg.inv()`, `np.linalg.det()` |

📄 **Complete reference:** [npfunctions.md](npfunctions.md) & [arrymethods.md](arrymethods.md)

---

## 💡 Key Concepts

### Broadcasting
```python
import numpy as np

arr = np.array([[100, 200, 300], [20, 300, 400]])
arr2 = np.array([10, 30, 40])

result = arr + arr2  # Broadcasting in action!
print(result)
```

### Vectorization (100x Faster!)
```python
# ❌ Slow: Python loops
result = [x + y for x, y in zip(arr1, arr2)]

# ✅ Fast: NumPy vectorization
result = arr1 + arr2
```

### Handling Missing Values
```python
arr = np.array([1, 2, np.nan, 4, np.nan])
print(np.isnan(arr))  # Detect NaN values
arr_clean = np.nan_to_num(arr)  # Replace NaN with 0
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a new branch (`git checkout -b feature/amazing-feature`)
3. ✍️ Commit your changes (`git commit -m 'Add some amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🎉 Open a Pull Request

### Ideas for Contributions:
- Add more practice problems
- Create Jupyter notebooks for tutorials
- Add performance benchmarks
- Improve documentation
- Add visualization examples

---

## 📊 Why NumPy?

- ⚡ **Speed** — 10-100x faster than pure Python
- 🧮 **Efficiency** — Optimized C/Fortran backend
- 🔧 **Versatility** — Foundation for Pandas, Scikit-learn, TensorFlow
- 🌍 **Industry Standard** — Used by data scientists worldwide
- 📈 **Scalability** — Handle millions of data points effortlessly

---

## 📖 Additional Resources

- 📘 [Official NumPy Documentation](https://numpy.org/doc/)
- 🎓 [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- 📊 [NumPy for Data Science](https://numpy.org/numpy-tutorials/)
- 🎥 [NumPy Video Tutorials](https://www.youtube.com/results?search_query=numpy+tutorial)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Show Your Support

If this repository helped you learn NumPy, please consider:
- ⭐ Starring the repository
- 🍴 Forking it for your own learning
- 📢 Sharing it with others
- 💬 Providing feedback

---

## 📬 Contact

Have questions or suggestions? Feel free to:
- Open an issue
- Submit a pull request
- Reach out via GitHub discussions

---

<div align="center">

**Happy Learning! 🚀**

Made with ❤️ for the Data Science Community

</div>
