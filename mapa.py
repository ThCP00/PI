import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap



st.set_page_config(layout="wide")

m = leafmap.Map()
data = "https://raw.githubusercontent.com/ThCP00/PI/main/DB_F.xlsx"
df = pd.read_excel(data)
m.add_points_from_xy(df, x="longitude", y="latitude")

m.to_streamlit(height=700)
