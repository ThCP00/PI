import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap
import geopandas as gpd


st.set_page_config(layout="wide")

m = leafmap.Map(center=[-15.7, -47.7], zoom=10)
data = "https://raw.githubusercontent.com/ThCP00/PI/main/DB_FIRE_MIN.csv"
df = pd.read_csv(data)
m.add_points_from_xy(df, x="longitude", y="latitude")

m.to_streamlit(height=600)


df = gpd.read_file('https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/geojs-DF.json')
df['lon'] = df.geometry.0  # extract longitude from geometry
df['lat'] = df.geometry.1  # extract latitude from geometry
df = df[['lon','lat']]     # only keep longitude and latitude
st.write(df.head())        # show on table for testing only
st.map(df)                 # show on map
