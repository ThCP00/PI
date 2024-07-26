import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    page_icon=":bar_chart: "
)

df = pd.read_excel("DB_FIRE.xlsx")
st.sidebar.header("Filtros")


ano = st.sidebar.multiselect(
    "Selecione o ano",
    options=df["Ano"].unique(),
    default=df["Ano"].unique()
)
mes = st.sidebar.multiselect(
    "Selecione o mes",
    options=df["Mês"].unique(),
    default=df["Mês"].unique()
)

df_selection = df.query(
    "Ano == @ano & Mês == @mes"
)
df = df_selection
with st.expander("Grafico"):
    st.line_chart(df, x="Ano", y="Mês")

st.dataframe(df_selection)
