import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

FILE = "expenses.csv"

# 📂 Load or create file
try:
    df = pd.read_csv(FILE)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE, index=False)

# ➕ Add expense
def add_expense():
    category = input("Enter category (Food/Travel/Other): ")
    amount = float(input("Enter amount: "))
    date = datetime.now().strftime("%Y-%m-%d")

    new_data = pd.DataFrame([[date, category, amount]],
                            columns=["Date", "Category", "Amount"])
    
    new_data.to_csv(FILE, mode='a', header=False, index=False)
    print("✅ Expense added!")

# 📊 Show summary
def show_summary():
    df = pd.read_csv(FILE)
    
    if df.empty:
        print("No data available.")
        return
    
    print("\n📌 Total Spending:", df["Amount"].sum())

    print("\n📂 Category-wise spending:")
    print(df.groupby("Category")["Amount"].sum())

# 📈 Plot graph
def plot_data():
    df = pd.read_csv(FILE)

    if df.empty:
        print("No data to plot.")
        return
    
    df.groupby("Category")["Amount"].sum().plot(kind='bar')
    plt.title("Expenses by Category")
    plt.ylabel("Amount")
    plt.show()

# 🔁 Menu loop
while True:
    print("\n1. Add Expense")
    print("2. Show Summary")
    print("3. Show Graph")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        show_summary()
    elif choice == '3':
        plot_data()
    elif choice == '4':
        break
    else:
        print("Invalid choice")