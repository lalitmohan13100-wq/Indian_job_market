import pandas as pd
import plotly.express as px
import streamlit as st
import theme as th

# 1. Page Configuration (Must be at the very top)
st.set_page_config(
    page_title="Indian Tech Jobs Analytics 2026", page_icon="📊", layout="wide"
)


# Apply Custom Theme
th.apply_theme()

# Load Data Once
df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")

# ==========================
# Sidebar Filters
# ==========================
st.sidebar.header("🔍 Filter Dashboard")

selected_city = st.sidebar.selectbox(
    "Select City",
    ["All"] + sorted(df["scraped_city"].dropna().unique().tolist()),
)

selected_workmode = st.sidebar.selectbox(
    "Select Work Mode",
    ["All"] + sorted(df["work_mode"].dropna().unique().tolist()),
)

selected_role = st.sidebar.selectbox(
    "Select Role Category",
    ["All"] + sorted(df["role_category"].dropna().unique().tolist()),
)

# Apply Filters
filtered_df = df.copy()

if selected_city != "All":
    filtered_df = filtered_df[filtered_df["scraped_city"] == selected_city]

if selected_workmode != "All":
    filtered_df = filtered_df[filtered_df["work_mode"] == selected_workmode]

if selected_role != "All":
    filtered_df = filtered_df[filtered_df["role_category"] == selected_role]

# Calculate Midpoint Salary
filtered_df["salary_midpoint_lpa"] = (
    filtered_df["salary_min_lpa"] + filtered_df["salary_max_lpa"]
) / 2

# ==========================
# Main Content Area
# ==========================
st.title("💼 Indian Tech Job Market Analytics Dashboard 2026")
st.markdown("### Executive Overview")
st.markdown("---")

# Key Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💼 Total Jobs", f"{len(filtered_df):,}")

with col2:
    st.metric(
        "🏢 Total Companies", f"{filtered_df['company_name'].nunique():,}"
    )

with col3:
    avg_rating = filtered_df["company_rating"].mean()
    st.metric(
        "⭐ Avg Company Rating", f"{round(avg_rating, 2)}" if avg_rating else "N/A"
    )

with col4:
    avg_salary = filtered_df["salary_midpoint_lpa"].mean()
    st.metric(
        "💰 Avg Salary (LPA)", f"₹{round(avg_salary, 2)}" if avg_salary else "N/A"
    )

st.markdown("---")

# Work Mode Chart
st.subheader("📊 Work Mode Distribution")
work_mode_count = filtered_df["work_mode"].value_counts().reset_index()
work_mode_count.columns = ["Work Mode", "Jobs"]

fig_workmode = px.bar(
    work_mode_count,
    x="Work Mode",
    y="Jobs",
    color="Jobs",
    color_continuous_scale=["#06B6D4", "#3B82F6"],
    text="Jobs",
    title="Distribution of Jobs by Work Mode",
)
st.plotly_chart(chart_theme(fig_workmode), use_container_width=True)

st.markdown("---")

# Company Size Chart
st.subheader("🥧 Company Size Distribution")
company_size = filtered_df["company_size_bucket"].value_counts().reset_index()
company_size.columns = ["Company Size", "Jobs"]

fig_size = px.pie(
    company_size,
    names="Company Size",
    values="Jobs",
    hole=0.6,
    color_discrete_sequence=["#06B6D4", "#3B82F6", "#8B5CF6", "#EC4899"],
    title="Company Size Distribution",
)
st.plotly_chart(chart_theme(fig_size), use_container_width=True)

st.markdown("---")

# Top Hiring Cities
st.subheader("🏙️ Top 10 Hiring Cities")
city_count = (
    filtered_df["scraped_city"].value_counts().head(10).reset_index()
)
city_count.columns = ["City", "Jobs"]

fig_city = px.bar(
    city_count,
    x="Jobs",
    y="City",
    orientation="h",
    color="Jobs",
    color_continuous_scale=["#06B6D4", "#6366F1"],
    text="Jobs",
    title="Top 10 Cities by Number of Job Openings",
)
fig_city.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(chart_theme(fig_city), use_container_width=True)

st.markdown("---")

# Hiring Trend Over Time
st.subheader("📈 Hiring Trend Over Time")
filtered_df["posted_date_raw"] = pd.to_datetime(
    filtered_df["posted_date_raw"], errors="coerce"
)
trend = (
    filtered_df.groupby(filtered_df["posted_date_raw"].dt.date)
    .size()
    .reset_index(name="Jobs")
)

fig_trend = px.line(
    trend,
    x="posted_date_raw",
    y="Jobs",
    markers=True,
    title="Job Postings Over Time",
)
fig_trend.update_traces(line_color="#06B6D4", marker=dict(color="#8B5CF6"))
st.plotly_chart(chart_theme(fig_trend), use_container_width=True)

st.markdown("---")

# Role Category Treemap
st.subheader("🌳 Jobs by Role Category")
role_count = filtered_df["role_category"].value_counts().reset_index()
role_count.columns = ["Role", "Jobs"]

fig_role = px.treemap(
    role_count,
    path=["Role"],
    values="Jobs",
    color="Jobs",
    color_continuous_scale=["#0F172A", "#06B6D4", "#8B5CF6"],
    title="Job Distribution by Role Category",
)
st.plotly_chart(chart_theme(fig_role), use_container_width=True)

st.markdown("---")

# Top Hiring Companies
st.subheader("🏢 Top 10 Hiring Companies")
top_companies = (
    filtered_df["company_name"].value_counts().head(10).reset_index()
)
top_companies.columns = ["Company", "Jobs"]

fig_companies = px.bar(
    top_companies,
    x="Company",
    y="Jobs",
    color="Jobs",
    color_continuous_scale=["#3B82F6", "#8B5CF6"],
    text="Jobs",
    title="Top 10 Companies by Number of Job Openings",
)
fig_companies.update_layout(xaxis_tickangle=-45)
st.plotly_chart(chart_theme(fig_companies), use_container_width=True)