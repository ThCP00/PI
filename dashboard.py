import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    page_icon=":bar_chart: "
)

df = pd.read_excel("DB_FIRE.xlsx")
st.sidebar.header("Filtros")
anos = st.sidebar.selectbox("Selecione o ano:", df["Ano"].unique())
mes = st.sidebar.selectbox("Selecione o mês", df["Mês"].unique())
df_selection = df.query(
    "Ano == @anos & Mês == @mes"
)
df = df_selection

st.markdown('metricas')

col1, col2= st.columns(2)
col1.metric("Dias Sem Chuva", df["DiaSemChuva"])
col2.metric("Risco de Fogo", df["RiscoFogo"])

st.dataframe(df_selection)
