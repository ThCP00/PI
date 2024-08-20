import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap
import geopandas as gpd
import matplotlib.pyplot as plt

st.set_page_config(page_icon='🔥', page_title='Calango', layout="wide", initial_sidebar_state="collapsed")

data = "DADOS/INPE_20_24.csv"
adm = "DADOS/sdia_ra_2022.shp"
dft= pd.read_csv('https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/inmet_inpe.csv')
anos = st.sidebar.selectbox("Selecione o ano:", dft["ano"].unique())
df_selection = dft.query(
        "ano == @anos")


m = leafmap.Map(center=[-15.7, -47.7], zoom=10)
df = pd.read_csv(data)
m.add_points_from_xy(df,
              x="Longitude",
              y="Latitude")
m.split_map(left_layer='ROADMAP', right_layer='HYBRID')
m.add_shp(adm)
m.to_streamlit(height=800)
st.bar_chart(dft, x='ano', y='frequencia_incendios', x_label='Ano', y_label='Incêndios', color="rgb(255, 75, 75)", horizontal=False, stack='layered')
st.bar_chart(df_selection, x="mes", y='frequencia_incendios', x_label='Mês', y_label='Incêndios', color="rgb(255, 75, 75)", horizontal=False, stack='layered')
