import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    page_icon=":bar_chart: "
)
df = pd.read_excel("DB_FIRE.xlsx")
lat = df["latitude"]
long = df["longitude"]

st.sidebar.header("Filtros")
anos = st.sidebar.selectbox("Selecione o ano:", df["Ano"].unique())
mes = st.sidebar.selectbox("Selecione o mês", df["Mês"].unique())
df_selection = df.query(
    "Ano == @anos & Mês == @mes"
)
st.map(data=df, latitude=lat, longitude=long, use_container_width=True)
df = df_selection


st.dataframe(df_selection)
