import streamlit as st
import leafmap.foliumap as leafmap



st.set_page_config(layout="wide")


m = leafmap.Map(center=[40, -100], zoom=4)
cidade = "https://raw.githubusercontent.com/ThCP00/PI/main/teste%20db1.csv"

m.add_points_from_xy(
    cidade,
    x="latitude",
    y="longitude",
    icon_names=["gear", "map", "leaf", "globe"],
    spin=True,
    add_legend=True,
    )

m.to_streamlit(height=700)
