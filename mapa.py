import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap
import geopandas as gpd
import geobr
st.set_page_config(page_icon='🔥', page_title='Calango', layout="wide")

gdf= geobr.read_municipality(code_muni='DF', year=2020)
gdf.head()
m = leafmap.Map(center=[-15.7, -47.7], zoom=10)
data = "https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/DB_FIRE_MIN.csv"
regiao = "https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/ADM_DF.csv"
df = gpd.read_file(data)
df = df[['DataHora','longitude','latitude','Satelite']]
m.add_points_from_xy(df,
                     x="longitude",
                     y="latitude",
                    color_column="regiao")
m.to_streamlit(height=700)

