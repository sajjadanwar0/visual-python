from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

# Streamlit Import: Add interactivity with the simple code like


src_file = Path.cwd() / 'notebooks' / 'data' / 'raw' / 'fuel_summary.csv'
df = pd.read_csv(src_file)
fig = px.histogram(df, x="fuelCost08", color="class_summary", labels={"fuelCost08": "Annual Fuel Cost"},
                   nbins=40, title="Fuel Cost Distribution"
                   )
st.title("Sample Example Update")
st.write(fig)


@st.cache()
def load_data():
    src_file = Path.cwd() / 'notebooks' / 'data' / 'raw' / 'fuel_summary.csv'
    raw_df = pd.read_csv(src_file)
    return raw_df



