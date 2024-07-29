import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap



st.set_page_config(layout="wide")


m = leafmap.Map(center=[-15.7, -47.7], zoom=10)
data = "https://raw.githubusercontent.com/ThCP00/PI/main/DB_FIRE_MIN.csv"
df = pd.read_csv(data)
m.add_points_from_xy(df, x="longitude", y="latitude")

m.to_streamlit(height=700)
