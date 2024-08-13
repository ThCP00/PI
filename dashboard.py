import streamlit as st
import pandas as pd


st.set_page_config(
    page_icon='📈',
    page_title="Dashboard",
    layout="wide",
)
df = pd.read_excel("https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/DB_FIRE.xlsx")

with st.sidebar:
    st.sidebar.header("Filtros")
    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
    anos = st.sidebar.selectbox("Selecione o ano:", df["Ano"].unique())
    df_selection = df.query(
        "Ano == @anos"
    )


df= pd.read_csv('https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/inmet_inpe.csv')
st.bar_chart(df, x='ano', y='frequencia_incendios', x_label='Ano', y_label='Incêndios', color="#ffffff", horizontal=False, stack='layered')
st.bar_chart(df, x='mes', y='frequencia_incendios', x_label='Mês', y_label='Incêndios', color="#ffffff", horizontal=False, stack='layered')
st.bar_chart(df.groupby('mes_numero', sort=False).sum('frequencia_incendios'))


st.dataframe(df_selection)
st.dataframe(df)
