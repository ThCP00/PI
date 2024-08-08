import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap



st.set_page_config(layout="wide")
m = leafmap.Map(center=[-15.7, -47.7], zoom=10)
data = "https://raw.githubusercontent.com/ThCP00/PI/main/ADM_DF.csv"
df = pd.read_csv(data)

m.add_basemap(basemap)

m.to_streamlit(height=700)
