import streamlit as st
import pandas as pd
import theme as th


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Indian Tech Job Market Dashboard",
    page_icon="💼",
    layout="wide"
)
th.apply_theme()

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")

# -----------------------------
# Title
# -----------------------------
st.title("💼 Indian Tech Job Market Analytics Dashboard")
st.markdown("### Welcome")
st.markdown("---")

st.write("""
This dashboard analyzes the *Indian Tech Job Market 2026* using Python,
Pandas, Plotly, and Streamlit.

Use the navigation menu on the left to explore different dashboard pages.
""")

# -----------------------------
# Project Summary
# -----------------------------
st.subheader("📌 Project Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💼 Total Jobs", len(df))

with col2:
    st.metric("🏢 Companies", df["company_name"].nunique())

with col3:
    st.metric("🏙️ Cities", df["scraped_city"].nunique())

with col4:
    st.metric("📂 Role Categories", df["role_category"].nunique())

st.markdown("---")

# -----------------------------
# Dashboard Pages
# -----------------------------
st.subheader("📊 Dashboard Pages")

st.markdown("""
- 📈 Executive Overview
- 💰 Salary & Experience Analysis
- 🏢 Company Skills Analysis
- 📊 Hiring Trends & Market Insights
""")

st.markdown("---")

# -----------------------------
# Dataset Preview
# -----------------------------
st.subheader("📋 Dataset Preview")

st.dataframe(df.head(10), use_container_width=True)

st.markdown("---")

st.success("✅ Project developed using Python, Pandas, Plotly Express and Streamlit.")