import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to the SQLite database
conn = sqlite3.connect("sales_data.db")

# Step 2: Run SQL query to fetch total quantity and revenue by product
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM 
    sales 
GROUP BY 
    product
"""

# Step 3: Load data into pandas DataFrame
df = pd.read_sql_query(query, conn)

# Step 4: Print the results
print(df)

# Step 5: Plot the revenue per product using a bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title('Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.tight_layout()

# Step 6: Save the chart if needed
plt.savefig("sales_chart.png")

# Optional: Show the plot
plt.show()

# Close the connection
conn.close()
