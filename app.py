import streamlit as st
import pandas as pd
from filters import get_filter_options, apply_filters
from visualizations import show_batting_charts, show_bowling_charts
from cricket_chatbot import cricket_chatbot_ui

# Load data
@st.cache_data
def load_data():
    batting = pd.read_csv("batting_detailed.csv")
    bowling = pd.read_csv("bowling_detailed.csv")
    return batting, bowling

batting, bowling = load_data()

# Sidebar: Advanced filters
st.sidebar.header("Advanced Filters")
filter_opts = get_filter_options(batting, bowling)
filters = {}
for key, values in filter_opts.items():
    filters[key] = st.sidebar.multiselect(f"Select {key.capitalize()}", values, default=values)

# Tabs for Batting/Bowling
tab1, tab2, tab3 = st.tabs(["Batting", "Bowling", "Chatbot"])

with tab1:
    st.subheader("Batting Stats & Visualizations")
    filtered_batting = apply_filters(batting, filters)
    show_batting_charts(filtered_batting)

with tab2:
    st.subheader("Bowling Stats & Visualizations")
    filtered_bowling = apply_filters(bowling, filters)
    show_bowling_charts(filtered_bowling)

with tab3:
    st.subheader("Cricket Q&A Chatbot")
    cricket_chatbot_ui(batting, bowling)