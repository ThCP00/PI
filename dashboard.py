import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    page_icon=":bar_chart: "
)

df = pd.read_excel("DB_FIRE.xlsx")
anos = [2020, 2021, 2022, 2023, 2024]
st.sidebar.header("Filtros")
year = st.sidebar.selectbox("Selecione o ano:", anos)

df_selection = df.query(
    "year == ano"
)
df = df_selection
with st.expander("Grafico"):
    st.line_chart(df, x="Ano", y="Mês")

st.dataframe(df_selection)

