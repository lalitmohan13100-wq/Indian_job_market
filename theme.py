import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Page Configuration (Must be at the very top)
st.set_page_config(
    page_title="Indian Tech Jobs Analytics 2026", page_icon="📊", layout="wide"
)


# 2. Refined CSS Theme
def apply_theme():
    st.markdown(
        """
    <style>
    /* Entire Dashboard Background */
    .stApp {
        background: linear-gradient(180deg, #0E1726 0%, #030712 100%);
        color: #F8FAFC;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0B1120;
        border-right: 1px solid #1E293B;
    }

    [data-testid="stSidebar"] * {
        color: #F8FAFC !important;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #F8FAFC !important;
        font-family: 'Inter', sans-serif;
    }

    /* Paragraphs & Text */
    p, span, label {
        color: #94A3B8 !important;
    }

    /* Metric Cards */
    [data-testid="stMetric"] {
        background-color: #1E293B;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #334155;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.25);
    }

    [data-testid="stMetricLabel"] {
        color: #94A3B8 !important;
        font-size: 0.9rem !important;
        font-weight: 500;
    }

    [data-testid="stMetricValue"] {
        color: #06B6D4 !important;
        font-weight: 700;
    }

    /* Custom Divider Styling */
    hr {
        border-color: #1E293B !important;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


# 3. Refined Plotly Theme
def chart_theme(fig):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#F8FAFC", family="Inter, Arial", size=12),
        title_font=dict(color="#F8FAFC", size=18),
        title_x=0.0,  # Left-aligned titles look cleaner on dashboards
        hoverlabel=dict(
            bgcolor="#1E293B", font_color="#F8FAFC", bordercolor="#334155"
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color="#94A3B8"),
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
        margin=dict(l=20, r=20, t=50, b=20),
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="#1E293B",  # Subtle grid line color
        tickfont=dict(color="#94A3B8", size=11),
        title_font=dict(color="#F8FAFC", size=13),
        zeroline=False,
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="#1E293B",  # Subtle grid line color
        tickfont=dict(color="#94A3B8", size=11),
        title_font=dict(color="#F8FAFC", size=13),
        zeroline=False,
    )

    return fig