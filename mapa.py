import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap
import geopandas as gpd
import matplotlib.pyplot as plt

st.set_page_config(page_icon='🔥', page_title='Calango', layout="wide")

data = "https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/DB_FIRE_MIN.csv"
adm = "DADOS/sdia_ra_2022.shp"
tab1, tab2 = st.tabs(["Pontos","Calor"])
m = leafmap.Map(center=[-15.7, -47.7], zoom=10)
with tab1:
  df = gpd.read_file(data)
  df = df[['DataHora','longitude','latitude','Satelite']]
  m.add_points_from_xy(df,
                     x="longitude",
                     y="latitude")
with tab2:
  df = gpd.read_file(data)
  df = df[['DataHora','longitude','latitude','Satelite']]
  m.add_heatmap(df,
               x="longitude",
               y="latitude",
               value="DataHora")

m.add_shp(adm)
m.to_streamlit(height=800)
