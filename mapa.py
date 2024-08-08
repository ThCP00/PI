import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap
import geopandas as gpd


st.set_page_config(layout="wide")


df = gpd.read_file('https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/geojs-DF.json')
df['lon'] = df.geometry.x  # extract longitude from geometry
df['lat'] = df.geometry.y  # extract latitude from geometry
df = df[['lon','lat']]     # only keep longitude and latitude
st.write(df.head())        # show on table for testing only
st.map(df)                 # show on map
