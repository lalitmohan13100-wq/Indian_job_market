import streamlit as st
import pandas as pd
import plotly.express as px
import theme as th

st.set_page_config(
    page_title="Hiring Trends & Market Insights",
    page_icon="📈",
    layout="wide"
)
th.apply_theme()

df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")

st.title("📈 Hiring Trends & Market Insights")
st.markdown("Analyze hiring trends across cities, work modes, and experience levels.")
st.markdown("---")


st.sidebar.header("🔍 Filter Dashboard")

selected_city = st.sidebar.selectbox(
    "Select City",
    ["All"] + sorted(df["scraped_city"].dropna().unique().tolist())
)

selected_workmode = st.sidebar.selectbox(
    "Select Work Mode",
    ["All"] + sorted(df["work_mode"].dropna().unique().tolist())
)

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

# Calculate Midpoint Salary
filtered_df["salary_midpoint_lpa"] = (
    filtered_df["salary_min_lpa"] + filtered_df["salary_max_lpa"]
) / 2





col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Jobs", len(df))

with col2:
    st.metric("Cities",filtered_df["scraped_city"].nunique())

with col3:
    st.metric("Work Modes", filtered_df["work_mode"].nunique())

with col4:
    st.metric("Role Categories", filtered_df["role_category"].nunique())


st.subheader("🌆 Top 10 Hiring Cities")

city = filtered_df["scraped_city"].value_counts().head(10).reset_index()
city.columns = ["City", "Jobs"]

fig = px.bar(city,x="Jobs",y="City",orientation="h",color="Jobs",text="Jobs",title="Top 10 Hiring Cities"
)

st.plotly_chart(fig, use_container_width=True)


st.markdown("---")
st.subheader("🏠 Work Mode Distribution")

workmode = filtered_df["work_mode"].value_counts().reset_index()
workmode.columns = ["Work Mode", "Jobs"]

fig2 = px.pie(workmode,names="Work Mode",values="Jobs",hole=0.4,title="Distribution of Work Modes"
)

st.plotly_chart(fig2, use_container_width=True)



st.markdown("---")
st.subheader("📈 Hiring by Experience")

exp = (
    filtered_df.groupby("experience_min_yrs")
      .size()
      .reset_index(name="Jobs")
)

fig3 = px.line(exp,x="experience_min_yrs",y="Jobs",markers=True,title="Job Openings by Minimum Experience"
)

fig3.update_layout(
    xaxis_title="Minimum Experience (Years)",
    yaxis_title="Number of Jobs"
)

st.plotly_chart(fig3, use_container_width=True)




st.markdown("---")
st.subheader("💼 Top 10 Job Categories")

job_category = (
    filtered_df["role_category"]
    .value_counts()
    .head(10)
    .reset_index()
)

job_category.columns = ["Role Category", "Jobs"]

fig4 = px.bar(job_category,x="Role Category",y="Jobs",color="Jobs",text="Jobs",title="Top 10 Job Categories"
)

fig4.update_layout(
    xaxis_tickangle=-45,
    xaxis_title="Role Category",
    yaxis_title="Number of Jobs"
)

st.plotly_chart(fig4, use_container_width=True)



st.markdown("---")
st.subheader("🌳 Jobs by City & Role Category")

fig5 = px.treemap(filtered_df,path=["scraped_city", "role_category"],title="Jobs by City and Role Category"
)

st.plotly_chart(fig5, use_container_width=True)