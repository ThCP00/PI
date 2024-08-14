import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap
import geopandas as gpd
st.set_page_config(page_icon='🔥', page_title='Calango', layout="wide")


m = leafmap.Map(center=[-15.7, -47.7], zoom=10)
data = "https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/DF_Municipios_2022.shp"
df = gpd.read_file(data)
st.dataframe(df)

m.to_streamlit(height=700)

