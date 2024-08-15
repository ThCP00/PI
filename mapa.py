import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap
import geopandas as gpd
import matplotlib.pyplot as plt

st.set_page_config(page_icon='🔥', page_title='Calango', layout="wide")

data = "https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/DB_FIRE_MIN.csv"
adm = "DADOS/sdia_ra_2022.shp"
area_protec = "DADOS/Area_de_Protecao_Ambiental.shp"
m = leafmap.Map(center=[-15.7, -47.7], zoom=10)
df = gpd.read_file(data)
df = df[['DataHora','longitude','latitude','Satelite']]
m.add_points_from_xy(df,
                     x="longitude",
                     y="latitude")
m.split_map(left_layer='ROADMAP', right_layer='HYBRID')
m.add_shp(area_protec)

m.to_streamlit(height=800)
