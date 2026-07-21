import streamlit as st
import pandas as pd
import plotly.express as px
# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Indian Tech Job Market Dashboard",
    page_icon="💼",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")

# ==========================
# Sidebar Filters
# ==========================

st.sidebar.header("🔍 Filter Dashboard")

# City Filter
selected_city = st.sidebar.selectbox(
    "Select City",
    ["All"] + sorted(df["scraped_city"].dropna().unique().tolist())
)

# Work Mode Filter
selected_workmode = st.sidebar.selectbox(
    "Select Work Mode",
    ["All"] + sorted(df["work_mode"].dropna().unique().tolist())
)

# Role Category Filter
selected_role = st.sidebar.selectbox(
    "Select Role Category",
    ["All"] + sorted(df["role_category"].dropna().unique().tolist())
)

# Apply Filters
filtered_df = df.copy()

if selected_city != "All":
    filtered_df = filtered_df[filtered_df["scraped_city"] == selected_city]

if selected_workmode != "All":
    filtered_df = filtered_df[filtered_df["work_mode"] == selected_workmode]

if selected_role != "All":
    filtered_df = filtered_df[filtered_df["role_category"] == selected_role]

# -----------------------------
# Sidebar
# -----------------------------
st.title("💼 Indian Tech Job Market Analytics Dashboard 2026")
