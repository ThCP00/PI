import streamlit as st
import leafmap.foliumap as leafmap



st.set_page_config(layout="wide")


m = leafmap.Map(center=[40, -100], zoom=4)
cities = "https://raw.githubusercontent.com/ThCP00/PI/main/DB_FIRE_MIN.csv"

m.add_points_from_xy(
    cities,
    x="longitude",
    y="latitude",
    icon_names=["gear", "map", "leaf", "globe"],
    spin=True,
    add_legend=True,
    )

m.add_heatmap(
    cities,
    latitude="latitude",
    longitude="longitude",
    name="Heat map",
    radius=20,
)

m.to_streamlit(height=700)
