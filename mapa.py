import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
st.set_page_config(page_icon='🔥', page_title='Calango', layout="wide")

data = "https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/DB_FIRE_MIN.csv"
adm = "DADOS/sdia_ra_2022.shp"

df = gpd.read_file(data)
df = df[['DataHora','longitude','latitude','Satelite']]

m = leafmap.Map(center=[-15.7, -47.7], zoom=10)
m.add_shp(adm)

left_layer=folium.WmsTileLayer(
    url=data,
    layers="ROADMAP",
    name="left",
    m.add_points_from_xy(df,
                     x="longitude",
                     y="latitude"))




m.split_map(left_layer, right_layer='SATELLITE')
m.to_streamlit(height=800)
