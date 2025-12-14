import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books.csv")

# Clean Price
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace(r"[^\d.]", "", regex=True)
)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# ================= TASK 3 VISUALIZATION =================

# 1. Price Range Categories
price_bins = [0, 10, 20, 30, 40, 50, 100]
price_labels = ["0-10", "10-20", "20-30", "30-40", "40-50", "50+"]

df["Price Range"] = pd.cut(df["Price"], bins=price_bins, labels=price_labels)

plt.figure()
df["Price Range"].value_counts().sort_index().plot(kind="bar")
plt.title("Books by Price Range")
plt.xlabel("Price Range (£)")
plt.ylabel("Number of Books")
plt.show()

# 2. Top 10 Most Expensive Books
top_prices = df.sort_values("Price", ascending=False).head(10)

plt.figure()
plt.barh(top_prices.index.astype(str), top_prices["Price"])
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Index")
plt.show()

# 3. Percentage Availability
availability_percent = df["Availability"].value_counts(normalize=True) * 100

plt.figure()
availability_percent.plot(kind="bar")
plt.title("Availability Percentage of Books")
plt.xlabel("Availability Status")
plt.ylabel("Percentage (%)")
plt.show()

print("Task 3: Insight-based Data Visualization completed successfully.")
