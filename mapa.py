import streamlit as st
import leafmap.foliumap as leafmap


st.title("Mapa")

filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
m = leafmap.Map(center=[40, -100], zoom=4)
m.add_heatmap(
    filepath,
    latitude="latitude",
    longitude="longitude",
    value="pop_max",
    name="Heat map",
    radius=20,
)
