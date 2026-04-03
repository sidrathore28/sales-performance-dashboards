import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Title
st.title("📊 Sales Performance Dashboard")

# Load data
engine = create_engine("sqlite:///sales.db")
df = pd.read_sql("SELECT * FROM sales", engine)
# Convert date
df['order_date'] = pd.to_datetime(df['order_date'])

# Create month column
df['month'] = df['order_date'].dt.to_period('M').astype(str)

# Profit calculation
df['cost'] = df['total_sales'] * 0.7
df['profit'] = df['total_sales'] - df['cost']

# KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Revenue", f"${df['total_sales'].sum():,.0f}")
col2.metric("📦 Total Orders", df['order_id'].nunique())
col3.metric("📊 Avg Order Value", f"${df['total_sales'].mean():.0f}")
col4.metric("💸 Total Profit", f"${df['profit'].sum():,.0f}")

st.markdown("---")
top_region = df.groupby('region')['total_sales'].sum().idxmax()
st.success(f"🏆 Top Performing Region: {top_region}")

# Filter
region = st.selectbox("📍 Select Region", df['region'].unique())
filtered_df = df[df['region'] == region]

# Charts
col1, col2 = st.columns(2)
st.subheader("📈 Monthly Revenue Trend")
monthly_sales = df.groupby('month')['total_sales'].sum()
st.line_chart(monthly_sales)
with col1:
    st.subheader("Revenue by Product")
    st.bar_chart(filtered_df.groupby('product')['total_sales'].sum())

with col2:
    st.subheader("Revenue by Category")
    st.bar_chart(filtered_df.groupby('category')['total_sales'].sum())
