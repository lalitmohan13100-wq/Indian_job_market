import streamlit as st
import pandas as pd
import plotly.express as px
import theme as th


st.set_page_config(
    page_title="company and skill analysis",
    page_icon="💰",
    layout="wide"
)
th.apply_theme()
# Load Dataset
df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")

st.title("🏢 Company Skills Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Companies", df["company_name"].nunique())

with col2:
    st.metric("Average Company Rating", round(df["company_rating"].mean(), 2))

with col3:
    st.metric("Average Skills Required", round(df["skills_count"].mean(), 1))


    company = df["company_name"].value_counts().head(10).reset_index()
company.columns = ["company_name", "jobs"]

fig = px.bar(company, x="jobs", y="company_name", orientation="h", color="jobs", title="Top 10 Hiring Companies"
)

st.plotly_chart(fig, use_container_width=True)



st.markdown("---")
st.subheader("⭐ Company Rating Distribution")

fig2 = px.histogram( df, x="company_rating", nbins=10, title="Distribution of Company Ratings", color_discrete_sequence=["#00CC96"]
)

fig2.update_layout(
    xaxis_title="Company Rating",
    yaxis_title="Number of Companies"
)

st.plotly_chart(fig2, use_container_width=True)


st.markdown("---")
st.subheader("🥧 Skills Required Distribution")

skills = df["skills_count"].value_counts().sort_index().reset_index()
skills.columns = ["skills_count", "jobs"]

fig3 = px.pie(skills,names="skills_count",values="jobs",title="Distribution of Skills Required"
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.subheader("🏢 Company Size Distribution")

company_size = (
    df["company_size_bucket"]
    .value_counts()
    .reset_index()
)

company_size.columns = ["company_size_bucket", "jobs"]

fig4 = px.bar(company_size,x="company_size_bucket",y="jobs", color="company_size_bucket",title="Jobs by Company Size",text_auto=True
)

fig4.update_layout(
    xaxis_title="Company Size",
    yaxis_title="Number of Jobs",
    showlegend=False
)

st.plotly_chart(fig4, use_container_width=True)