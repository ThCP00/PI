import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap



st.set_page_config(layout="wide")


m = leafmap.Map(center=[-20, -50], zoom=8)
data = "https://raw.githubusercontent.com/ThCP00/PI/main/DB_FIRE_MIN.csv"
df = pd.read_csv(data)
m.add_points_from_xy(df, x="longitude", y="latitude")

m.to_streamlit(height=700)
