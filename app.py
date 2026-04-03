import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("📊 Sales Performance Dashboard")

engine = create_engine("sqlite:///sales.db")
df = pd.read_sql("SELECT * FROM sales", engine)

# KPIs
st.metric("Total Revenue", f"${df['total_sales'].sum():,.0f}")
st.metric("Total Orders", df['order_id'].nunique())
st.metric("Avg Order Value", f"${df['total_sales'].mean():.0f}")

# Filter
region = st.selectbox("Select Region", df['region'].unique())
filtered_df = df[df['region'] == region]

st.subheader("Revenue by Product")
st.bar_chart(filtered_df.groupby('product')['total_sales'].sum())