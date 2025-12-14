import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books.csv")

# Clean Price column (robust)
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace(r"[^\d.]", "", regex=True)
)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Clean Availability
df["Availability"] = df["Availability"].astype(str).str.strip()

# PRICE ANALYSIS
print("Average Price:", df["Price"].mean())
print("Minimum Price:", df["Price"].min())
print("Maximum Price:", df["Price"].max())

# ================== VISUALS ==================

# Histogram
plt.figure()
plt.hist(df["Price"].dropna(), bins=20)
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Frequency")
plt.show()

# Boxplot
plt.figure()
plt.boxplot(df["Price"].dropna())
plt.title("Box Plot of Book Prices")
plt.ylabel("Price (£)")
plt.show()

# Availability bar chart
plt.figure()
df["Availability"].value_counts().plot(kind="bar")
plt.title("Book Availability")
plt.xlabel("Status")
plt.ylabel("Count")
plt.show()
