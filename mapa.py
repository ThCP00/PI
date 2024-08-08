import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap
import geopandas as gpd


st.set_page_config(layout="wide")


df = gpd.read_file('https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/geojs-DF.json')
st.map(df) 
