import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd


st.set_page_config(
    page_icon='📈',
    page_title="Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)
tab1, tab2 = st.tabs(["Ano","Mes"])
df= pd.read_csv('https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/inmet_inpe.csv')
anos = st.sidebar.selectbox("Selecione o ano:", df["ano"].unique())
df_selection = df.query(
        "ano == @anos")

with tab1:
    st.markdown("<h3 style='text-align: center; color: white;'>Frequência de Incêndios por Ano</h3>",unsafe_allow_html=True)
    st.bar_chart(df, x='ano', y='frequencia_incendios', x_label='Ano', y_label='Incêndios', color="rgb(255, 75, 75)", horizontal=False, stack='layered')
    c1, c2 = st.columns((5,5))
    with c1:
        fig=px.pie(df, values='frequencia_incendios', names='ano')
        st.plotly_chart(fig, use_container_width=True,theme="streamlit")
    with c2:
        fig=px.scatter(df_selection, x="ano", y='frequencia_incendios')
        fig.update_layout(scattermode="group", scattergap=1)
        st.plotly_chart(fig, use_container_width=True,theme="streamlit")

with tab2:
   st.markdown("<h3 style='text-align: center; color: white;'>Frequência de Incêndios por Mês</h3>",unsafe_allow_html=True)
   st.bar_chart(df_selection, x="mes_numero", y='frequencia_incendios', x_label='Mês', y_label='Incêndios', color="rgb(255, 75, 75)", horizontal=False, stack='layered')
   c1, c2 = st.columns((5,5))
   with c1:    
       fig=px.pie(df_selection, values='frequencia_incendios', names='mes')
       st.plotly_chart(fig, use_container_width=True,theme="streamlit")
   with c2:
       fig=px.scatter(df_selection, x="mes_numero", y='frequencia_incendios')
       st.plotly_chart(fig, use_container_width=True,theme="streamlit")
