
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'sales': [1000, 1500, 1200, 1800, 2000]
}

df = pd.DataFrame(data)

# Line Chart
plt.figure()
plt.plot(df['month'], df['sales'], marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()

# Save chart
plt.savefig("sales_trend.png")

# Bar Chart
plt.figure()
plt.bar(df['month'], df['sales'])
plt.title("Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")

# Save chart
plt.savefig("sales_bar.png")

print("Charts created successfully!")
