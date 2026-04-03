import pandas as pd
from sqlalchemy import create_engine

# Create database
engine = create_engine("sqlite:///../sales.db")

# Load cleaned data
df = pd.read_csv("../data/cleaned_sales_data.csv")

# Store in database
df.to_sql("sales", engine, if_exists="replace", index=False)

print("Data stored in database!")