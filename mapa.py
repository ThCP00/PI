import streamlit as st
import pandas as pd
import leafmap.leafmap as leafmap
import geopandas as gpd
import matplotlib.pyplot as plt

st.set_page_config(page_icon='🔥', page_title='Calango', layout="wide")

data = "DADOS/INPE_20_24.csv"
adm = "DADOS/sdia_ra_2022.shp"
area_protec = "DADOS/Area_de_Protecao_Ambiental.shp"
m = leafmap.Map(center=[-15.7, -47.7], zoom=10)
df = pd.read_csv(data)
m.add_heatmap(df,
              x="Longitude",
              y="Latitude",
             value="id")
m.split_map(left_layer='ROADMAP', right_layer='HYBRID')
m.add_shp(adm)
m.to_streamlit(height=800)
