import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap
import geopandas as gpd
from utils.plots import line_plot, bar_plot
from utils.style import set_background

st.set_page_config(layout="wide")

options = list(leafmap.basemaps.keys()) 
index = options.index("OpenTopoMap")
basemap = st.selectbox("Selecione o tipo de mapa:", options, index)

m = leafmap.Map(center=[-15.7, -47.7], zoom=10)
data = "https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/ADM_DF.csv"
df = pd.read_csv(data)
m.add_points_from_xy(df, x="longitude", y="latitude", layer_name="ra_nome")
m.add_basemap(basemap)

m.to_streamlit(height=700)

d= pd.read_csv('Data/inmet_inpe.csv')
st.plotly_chart(line_plot(d, 'Data Medição', 'Frequência de incêndios',
                    'Frequência de incêndios em Brasília - 1998 a 2022', 'red'), use_container_width=True)
