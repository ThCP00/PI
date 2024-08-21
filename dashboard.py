import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd
import altair as alt
import plost

st.set_page_config(
    page_icon='📈',
    page_title="Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)
c1, c2 = st.columns((5,5))
tab1, tab2 = st.tabs(["Ano","Mes"])
df= pd.read_csv('https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/inmet_inpe.csv')
anos = st.sidebar.selectbox("Selecione o ano:", df["ano"].unique())
df_selection = df.query(
        "ano == @anos")

with tab1:
    st.markdown("<h3 style='text-align: center; color: white;'>Frequência de Incêndios por Ano</h3>",
            unsafe_allow_html=True)
    st.bar_chart(df, x='ano', y='frequencia_incendios', x_label='Ano', y_label='Incêndios', color="rgb(255, 75, 75)", horizontal=False, stack='layered')
    st.markdown("<h3 style='text-align: center; color: white;'>Precipitação por Ano</h3>",
            unsafe_allow_html=True)
    st.bar_chart(df, x="ano" , y="PRECIPITACAO",x_label='Ano', y_label='Precipitação', stack='layered')
    st.markdown("<h3 style='text-align: center; color: white;'>Temperatura Média por Ano</h3>",
            unsafe_allow_html=True)
    st.bar_chart(df, x="ano" , y="TEMPERATURA_MEDIA",x_label='Ano', y_label='Temperatura Média', stack='layered')

with tab2:
   st.markdown("<h3 style='text-align: center; color: white;'>Frequência de Incêndios por Mês</h3>",
            unsafe_allow_html=True)
   st.bar_chart(df_selection, x="mes_numero", y='frequencia_incendios', x_label='Mês', y_label='Incêndios', color="rgb(255, 75, 75)", horizontal=False, stack='layered')
   st.markdown("<h3 style='text-align: center; color: white;'>Precipitação por Mês</h3>",
            unsafe_allow_html=True)
   st.bar_chart(df_selection, x="mes_numero" , y="PRECIPITACAO", x_label='Mês', y_label='Precipitação',stack='layered')
   st.markdown("<h3 style='text-align: center; color: white;'>Temperatura Média por Mês</h3>",
            unsafe_allow_html=True)
   st.bar_chart(df_selection, x="mes_numero" , y="TEMPERATURA_MEDIA", x_label='Mês', y_label='Temperatura Média',stack='layered')
