import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Executive Overview",
    page_icon="📊",
    layout="wide"
)

df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")
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








st.markdown("### Executive Overview")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💼 Total Jobs", len(filtered_df))

with col2:
    st.metric("🏢 Total Companies", filtered_df["company_name"].nunique())

with col3:
    st.metric("⭐ Avg Company Rating",
              round(filtered_df["company_rating"].mean(),2))

with col4:
    filtered_df["salary_midpoint_lpa"] = (filtered_df["salary_min_lpa"] + filtered_df["salary_max_lpa"]) / 2
    avg_salary = df["salary_midpoint_lpa"].mean()
    st.metric("💰 Avg Salary (LPA)",
              round(avg_salary,2))
    
st.markdown("---")
st.subheader("📊 Work Mode Distribution")

work_mode_count = filtered_df["work_mode"].value_counts().reset_index()
work_mode_count.columns = ["Work Mode", "Jobs"]

fig = px.bar( work_mode_count,x="Work Mode",  y="Jobs",color="Work Mode",text="Jobs", title="Distribution of Jobs by Work Mode"
)

st.plotly_chart(fig, use_container_width=True)


st.markdown("---")
st.subheader("🥧 Company Size Distribution")

company_size = filtered_df["company_size_bucket"].value_counts().reset_index()
company_size.columns = ["Company Size", "Jobs"]

fig = px.pie(
    company_size,
    names="Company Size",
    values="Jobs",
    hole=0.5,
    title="Company Size Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("🏙️ Top 10 Hiring Cities")

city_count = (
    filtered_df["scraped_city"]
    .value_counts()
    .head(10)
    .reset_index()
)

city_count.columns = ["City", "Jobs"]

fig = px.bar(
    city_count,
    x="Jobs",
    y="City",
    orientation="h",
    color="Jobs",
    text="Jobs",
    title="Top 10 Cities by Number of Job Openings"
)

fig.update_layout(yaxis={"categoryorder": "total ascending"})

st.plotly_chart(fig, use_container_width=True)


st.markdown("---")
st.subheader("📈 Hiring Trend Over Time")

filtered_df["posted_date_raw"] = pd.to_datetime(filtered_df["posted_date_raw"], errors="coerce")

trend = (
    filtered_df.groupby(filtered_df["posted_date_raw"].dt.date)
      .size()
      .reset_index(name="Jobs")
)

fig = px.line(
    trend,
    x="posted_date_raw",
    y="Jobs",
    markers=True,
    title="Job Postings Over Time"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("⭐Company Rating vs Average Salary")

fig5 = px.treemap(filtered_df,path=["company_rating", "salary_midpoint_lpa"],title="Company rating vs Average Salary"
)

st.plotly_chart(fig5, use_container_width=True)



st.markdown("---")
st.subheader("🌳 Jobs by Role Category")

role_count = (
   filtered_df["role_category"]
    .value_counts()
    .reset_index()
)

role_count.columns = ["Role", "Jobs"]

fig = px.treemap(
    role_count,
    path=["Role"],
    values="Jobs",
    color="Jobs",
    title="Job Distribution by Role Category"
)

st.plotly_chart(fig, use_container_width=True)





st.markdown("---")
st.subheader("🏢 Top 10 Hiring Companies")

top_companies = (
    filtered_df["company_name"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_companies.columns = ["Company", "Jobs"]

fig = px.bar(
    top_companies,
    x="Company",
    y="Jobs",
    color="Jobs",
    text="Jobs",
    title="Top 10 Companies by Number of Job Openings"
)

fig.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig, use_container_width=True)