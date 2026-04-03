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

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Revenue", f"${df['total_sales'].sum():,.0f}")
col2.metric("📦 Total Orders", df['order_id'].nunique())
col3.metric("📊 Avg Order Value", f"${df['total_sales'].mean():.0f}")

st.markdown("---")

# Filter
region = st.selectbox("📍 Select Region", df['region'].unique())
filtered_df = df[df['region'] == region]

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Revenue by Product")
    st.bar_chart(filtered_df.groupby('product')['total_sales'].sum())

with col2:
    st.subheader("Revenue by Category")
    st.bar_chart(filtered_df.groupby('category')['total_sales'].sum())
