from pathlib import Path

import altair
import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt


@st.cache()
def load_data():
    src_file = Path.cwd() / 'notebooks' / 'data' / 'raw' / 'fuel_summary.csv'
    raw_df = pd.read_csv(src_file)
    return raw_df


# Load the data
df = load_data()
min_year = int(df["year"].min())
max_year = int(df["year"].max())
valid_makes = ["ALL"] + sorted(df["make"].unique())
default_makes = df["make"].value_counts().nlargest(5).index.tolist()
# Setup the UI
make = st.multiselect("Select a make:", valid_makes, default=default_makes)
year_range = st.slider(
    label="Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
)

# Filter the Data

year_filter = df["year"].between(year_range[0], year_range[1])
if "ALL" in make:
    # Dummy filter to include all data
    make_filter = True
else:
    make_filter = df["make"].isin(make)

plot_df = df[make_filter & year_filter]

avg_fuel_economy = plot_df["fuelCost08"].mean()
st.sidebar.metric("Average", avg_fuel_economy)

# Plot the data
fig = px.histogram(plot_df, x="fuelCost08", color="class_summary", labels={"fuelCost08": "Annual Fuel Cost"},
                   nbins=40, title="Fuel Cost Distribution"
                   )
altair_chart = (altair.Chart(plot_df).mark_tick().encode(y="fuel_type_summary", x="barrels08").properties(width=600))
# Display the output results
st.write(fig)
st.write(altair_chart)
