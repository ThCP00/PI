import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap
import geopandas as gpd

st.set_page_config(page_icon='🔥', page_title='Calango', layout="wide")


m = leafmap.Map(center=[-15.7, -47.7], zoom=10)
data = "https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/DB_FIRE_MIN.csv"
df = gpd.read_csv(data)
m.add_points_from_xy(df, x="longitude", y="latitude", layer_name="ra_nome")

m.to_streamlit(height=700)

