import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap

st.set_page_config(page_icon='🔥', page_title='Calango', layout="wide")


m = leafmap.Map(center=[-15.7, -47.7], zoom=10)
data = "https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/DB_FIRE_MIN.csv"
regiao = "https://raw.githubusercontent.com/ThCP00/PI/main/DADOS/ADM_DF.csv"
df = pd.read_file(data)

m.add_heatmap(df,
             latitude="latitude",
             longitude="longitude",
             value="DataHora")
m.to_streamlit(height=700)

