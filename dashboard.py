import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd
import altair as alt

st.set_page_config(
    page_icon='📈',
    page_title="Dashboard",
    layout="wide",
)

df= pd.read_csv('https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/inmet_inpe.csv')
anos = st.sidebar.selectbox("Selecione o ano:", df["ano"].unique())
df_selection = df.query(
        "ano == @anos")
st.bar_chart(df, x='ano', y='frequencia_incendios', x_label='Ano', y_label='Incêndios', color="#ffffff", horizontal=False, stack='layered')
st.bar_chart(df_selection, x='mes', y='frequencia_incendios', x_label='Mês', y_label='Incêndios', color="#ffffff", horizontal=False, stack='layered')
st.bar_chart(df.groupby('mes', sort=False).sum('frequencia_incendios'))


st.dataframe(df_selection)
st.dataframe(df)
