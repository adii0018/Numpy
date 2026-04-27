import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate Data (10 students, 5 subjects)
np.random.seed(0)
marks = np.random.randint(40, 100, (10, 5))

students = [f"Student {i+1}" for i in range(10)]
subjects = ["Math", "Science", "English", "CS", "History"]

print("Marks Matrix:\n", marks)

# Step 2: Analysis using NumPy
avg_marks = np.mean(marks, axis=1)
max_marks = np.max(marks, axis=1)
min_marks = np.min(marks, axis=1)

print("\nAverage Marks:", avg_marks)
print("Highest Marks:", max_marks)
print("Lowest Marks:", min_marks)

# Step 3: Visualization

# 📌 Bar Graph (Average Marks)

plt.figure()
plt.bar(students, avg_marks)
plt.xticks(rotation=45)
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 📌 Line Graph (Marks of Student 1)
plt.figure()
plt.plot(subjects, marks[0], marker='o')
plt.title("Marks of Student 1")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 📌 Histogram (All Marks Distribution)

plt.figure()
plt.hist(marks.flatten(), bins=10)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()