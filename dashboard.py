import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    page_icon=":bar_chart: "
)
df = pd.read_excel("DB_FIRE.xlsx")

with st.sidebar:
    st.sidebar.header("Filtros")
    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
    anos = st.sidebar.selectbox("Selecione o ano:", df["Ano"].unique())
    mes = st.sidebar.selectbox("Selecione o mês", df["Mês"].unique())
    df_selection = df.query(
        "Ano == @anos & Mês == @mes"
    )

def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
    heatmap = alt.Chart(input_df).mark_rect().encode(
            y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Ano", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
            x=alt.X(f'{input_x}:O', axis=alt.Axis(title="Mes", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
            color=alt.Color(f'max({input_color}):Q',
                             legend=None,
                             scale=alt.Scale(scheme=input_color_theme)),
            stroke=alt.value('black'),
            strokeWidth=alt.value(0.25),
        ).properties(width=900
        ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
        ) 
    # height=300
    return heatmap


heatmap = make_heatmap(df_selection, 'anos', 'mes', 'Dia', selected_color_theme)
st.altair_chart(heatmap, use_container_width=True)

st.dataframe(df_selection)
