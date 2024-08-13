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
df = pd.read_excel("https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/DB_FIRE.xlsx")

with st.sidebar:
    st.sidebar.header("Filtros")
    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
    anos = st.sidebar.selectbox("Selecione o ano:", df["Ano"].unique())
    df_selection = df.query(
        "Ano == @anos"
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
def make_choropleth(input_df, input_id, input_column, input_color_theme):
    choropleth = px.choropleth(input_df, locations = input_id, color=input_column, locationmode="USA-states",
                               color_continuous_scale=input_color_theme,
                               range_color=(0, max(df_selection.Ano)),
                               scope="usa",
                               labels={'population':'Population'}
                              )
    choropleth.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=350
    )
    return choropleth

choropleth = make_choropleth(df_selection, 'Ano', 'Mês', selected_color_theme)
st.plotly_chart(choropleth, use_container_width=True)

heatmap = make_heatmap(df_selection, 'Ano', 'Mês', 'Dia', selected_color_theme)
st.altair_chart(heatmap, use_container_width=True)

df= pd.read_csv('https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/inmet_inpe.csv')
st.bar_chart(df, x='ano', y='frequencia_incendios', x_label='Ano', y_label='Incêndios', color="#ffffff", horizontal=False, stack='layered')
st.bar_chart(df, x='mes', y='frequencia_incendios', x_label='Mês', y_label='Incêndios', color="#ffffff", horizontal=False, stack='layered')
st.bar_chart(df.groupby('mes_numero', sort=False).sum('frequencia_incendios'))


st.dataframe(df_selection)
st.dataframe(df)
