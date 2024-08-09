import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap
import geopandas as gpd
from utils.plots import line_plot, bar_plot

st.set_page_config(page_icon='🔥', page_title='Calango', layout="wide")

options = list(leafmap.basemaps.keys()) 
index = options.index("OpenTopoMap")
basemap = st.selectbox("Selecione o tipo de mapa:", options, index)

m = leafmap.Map(center=[-15.7, -47.7], zoom=10)
data = "https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/ADM_DF.csv"
df = pd.read_csv(data)
m.add_points_from_xy(df, x="longitude", y="latitude", layer_name="ra_nome")
m.add_basemap(basemap)

m.to_streamlit(height=700)

df= pd.read_csv('https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/inmet_inpe.csv')
st.plotly_chart(bar_plot(df.groupby('ano').sum('frequencia_incendios')))
