import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap
import geopandas as gpd
import matplotlib.pyplot as plt

st.set_page_config(page_icon='🔥', page_title='Calango', layout="wide", initial_sidebar_state="collapsed")

data = "DADOS/INPE_20_24.csv"
adm = "DADOS/sdia_ra_2022.shp"


m = leafmap.Map(center=[-15.7, -47.7], zoom=10)
df = pd.read_csv(data)
anos = st.sidebar.selectbox("Selecione o ano:", df["DataHora"].unique())
df_selection = df.query(
        "DataHora == @anos")
m.add_points_from_xy(df_selection,
              x="Longitude",
              y="Latitude")
m.split_map(left_layer='ROADMAP', right_layer='HYBRID')
m.add_shp(adm)
m.to_streamlit(height=800)

