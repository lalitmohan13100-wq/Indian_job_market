import streamlit as st
import pandas as pd
import plotly.express as px
import theme as th

st.set_page_config(
    page_title="Salary & Experience Analysis",
    page_icon="💰",
    layout="wide"
)
th.apply_theme()

# Load Dataset
df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")

st.title("💰 Salary & Experience Analysis")
st.markdown("Analyze salary trends and experience requirements in the Indian Tech Job Market.")
st.markdown("---")

df["salary_midpoint_lpa"] = (
    df["salary_min_lpa"] +
    df["salary_max_lpa"]
) / 2




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
    st.metric("Average Salary", f"{df['salary_midpoint_lpa'].mean():.2f} LPA")

with col2:
    st.metric("Highest Salary", f"{df['salary_max_lpa'].max():.2f} LPA")

with col3:
    st.metric("Minimum Experience", f"{df['experience_min_yrs'].min()} Years")

with col4:
    st.metric("Maximum Experience", f"{df['experience_max_yrs'].max()} Years")

    st.markdown("---")
st.subheader("📊 Salary Distribution")


salary_bins = [0, 5, 10, 20, 30, 50, 100]

salary_labels = [
    "0-5 LPA",
    "5-10 LPA",
    "10-20 LPA",
    "20-30 LPA",
    "30-50 LPA",
    "50+ LPA"
]

df["salary_range"] = pd.cut(
    df["salary_midpoint_lpa"],
    bins=salary_bins,
    labels=salary_labels,
    include_lowest=True
)


fig = px.histogram(df,x="salary_range",color="salary_range",title="Salary Distribution by Salary Range"
)

fig.update_layout(
    xaxis_title="Salary Range",
    yaxis_title="Number of Jobs"
)

st.plotly_chart(fig, use_container_width=True)


fig = px.histogram(df,x="experience_min_yrs",nbins=25,title="Distribution of Experience",color_discrete_sequence=["#0EA599"]
)

fig.update_layout(
    xaxis_title="Experience (Years) ",
    yaxis_title="Number of Jobs"
)

st.plotly_chart(fig, use_container_width=True)



salary_role = df.groupby("role_category", as_index=False)["salary_midpoint_lpa"].mean()

fig1 = px.bar(data_frame=salary_role,x="role_category",y="salary_midpoint_lpa",color="role_category",title="Average Salary by Role Category",text_auto=".1f"
)

fig1.update_layout(
    xaxis_title="Role Category",
    yaxis_title="Average Salary (LPA)"
)

st.plotly_chart(fig1, use_container_width=True)




salary_variation = df.groupby("experience_tier", as_index=False)["salary_midpoint_lpa"].mean()

fig1 = px.bar(data_frame=salary_variation,x="experience_tier",y="salary_midpoint_lpa",color="experience_tier",title="Salary variation across experience levels",text_auto=".1f"
)

fig1.update_layout(
    xaxis_title="experience_tier",
    yaxis_title="Average Salary (LPA)"
)

st.plotly_chart(fig1, use_container_width=True)





st.markdown("---")
st.subheader("")

fig5 = px.treemap(df,path=["experience_min_yrs", "salary_midpoint_lpa"],title="experience vs salary distribution"
)

st.plotly_chart(fig5, use_container_width=True)