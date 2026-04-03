import pandas as pd

# Load data
df = pd.read_excel("../data/sales_data.xlsx")

# Convert date column
df['order_date'] = pd.to_datetime(df['order_date'])

# Create total sales column
df['total_sales'] = df['quantity'] * df['price']

# Save cleaned data
df.to_csv("../data/cleaned_sales_data.csv", index=False)

print("Data cleaned successfully!")