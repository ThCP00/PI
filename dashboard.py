import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd
import altair as alt

st.set_page_config(
    page_icon='📈',
    page_title="Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.markdown("<h2 style='text-align: center; color: white;'> Visualização das séries históricas </h2>",
            unsafe_allow_html=True)
tab1, tab2 = st.tabs(["Ano","Mes"])
df= pd.read_csv('https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/inmet_inpe.csv')
anos = st.sidebar.selectbox("Selecione o ano:", df["ano"].unique())
df_selection = df.query(
        "ano == @anos")

with tab1:
    st.bar_chart(df, x='ano', y='frequencia_incendios', x_label='Ano', y_label='Incêndios', color="rgb(255, 75, 75)", horizontal=False, stack='layered')
with tab2:
   st.bar_chart(df_selection, x="mes", y='frequencia_incendios', x_label='Mês', y_label='Incêndios', color="rgb(255, 75, 75)", horizontal=False, stack='layered')
    px.bar(df_selection, x="mes", y="frequencia_incendios")

