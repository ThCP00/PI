import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    page_icon=":bar_chart: "
)

df = pd.read_excel("DB_FIRE.xlsx")
st.sidebar.header("Filtros")
anos = st.sidebar.selectbox("Selecione o ano:", df["Ano"])

df_selection = df.query(
    "Ano == @anos"
)
df = df_selection
with st.expander("Grafico"):
    st.line_chart(df, x="Ano", y="Mês")

st.dataframe(df_selection)
