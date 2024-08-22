import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap
import geopandas as gpd
import plotly.express as px

st.set_page_config(page_icon='🔥', page_title='Calango', layout="wide", initial_sidebar_state="collapsed")
tab1, tab2 = st.tabs(["Pontos","Mapa de Calor"])
col1, col2 = st.columns((2))
data = "DADOS/INPE_20_24.csv"
adm = "DADOS/sdia_ra_2022.shp"
style= {
    "color": "#ff4b4b",
}
df = pd.read_csv(data)

df["DataHora"]=pd.to_datetime(df["DataHora"])

inicio = pd.to_datetime(df["DataHora"]).min()
final = pd.to_datetime(df["DataHora"]).max()

with col1:
    data1= pd.to_datetime(st.date_input("Data Inicio", inicio))
with col2:
    data2= pd.to_datetime(st.date_input("Data Final", final))
df = df[(df["DataHora"]>=data1) & (df["DataHora"]<=data2)].copy()

m = leafmap.Map(center=[-15.7, -47.7], zoom=10)

with tab1:
    m.add_points_from_xy(df,
                  x="Longitude",
                  y="Latitude")
    m.split_map(left_layer='ROADMAP', right_layer='HYBRID')
    m.add_shp(adm, style=style)
    m.to_streamlit(height=800)

with tab2:
    fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='FRP', radius=20,
                        center=dict(lat=-15.7, lon=-47.7), zoom=10,
                        mapbox_style="ROADMAP",height=800)
    st.plotly_chart(fig, use_container_width=True)
