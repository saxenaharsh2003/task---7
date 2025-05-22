import sqlite3
import random

# Connect to (or create) the SQLite database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create the sales table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Define products and their fixed prices
products = {
    "Apple": 1.2,
    "Banana": 0.5,
    "Orange": 0.8,
    "Mango": 1.5,
    "Grapes": 2.0,
    "Pineapple": 3.0,
    "Watermelon": 4.0,
    "Papaya": 2.5,
    "Kiwi": 1.8,
    "Strawberry": 3.5
}

# Generate bulk sales data (e.g., 200 records)
sample_data = []
for _ in range(200):
    product = random.choice(list(products.keys()))
    quantity = random.randint(1, 25)
    price = products[product]
    sample_data.append((product, quantity, price))

# Insert data into the database
cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)

# Commit and close connection
conn.commit()
conn.close()

print("sales_data.db created and populated with 200 sample sales records.")
