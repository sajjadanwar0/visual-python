from pathlib import Path
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
valid_makes = sorted(df["make"].unique())

# Setup the UI
make = st.multiselect("Select a make:", valid_makes)
year_range = st.slider(
    label="Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
)

# Filter the data based on the inputs
year_filter = df["year"].between(year_range[0], year_range[1])
make_filter = df["make"].isin(make)

plot_df = df[make_filter & year_filter]

avg_fuel_economy = plot_df["fuelCost08"].mean()
st.metric("Average", avg_fuel_economy)

# Plot the data
fig = px.histogram(plot_df,
                   x="fuelCost08",
                   color="class_summary",
                   labels={"fuelCost08": "Annual Fuel Cost"},
                   nbins=40,
                   title="Fuel Cost Distribution",

                   )

altair_chart = alt.Chart(plot_df).mark_tick().encode(y="fuel_type_summary", x="barrels08")

# Display the Output
st.write(fig)
st.write(altair_chart)
st.write("Sample Data", plot_df.head(10))
