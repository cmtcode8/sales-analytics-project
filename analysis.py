import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Clean data
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])

# Analysis
total_sales = df['Sales'].sum()
best_product = df.groupby('Product')['Sales'].sum().idxmax()

# Monthly sales
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

# Save results to file
with open("insights.txt", "w") as f:
    f.write(f"Total Sales: {total_sales}\n")
    f.write(f"Best Product: {best_product}\n\n")
    f.write("Monthly Sales:\n")
    f.write(str(monthly_sales))

# Print results
print("Total Sales:", total_sales)
print("Best Product:", best_product)

# Visualization
monthly_sales.plot(kind='bar')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()