import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///../sales.db")

df = pd.read_sql("SELECT * FROM sales", engine)

# KPIs
total_revenue = df['total_sales'].sum()
total_orders = df['order_id'].nunique()
avg_order_value = total_revenue / total_orders

print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)
print("Average Order Value:", avg_order_value)