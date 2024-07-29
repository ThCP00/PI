import streamlit as st
import leafmap.foliumap as leafmap



st.set_page_config(layout="wide")
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['latitude', 'longitude'])
st.map(df)

m = leafmap.Map(center=[40, -100], zoom=4)
cities = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"

m.add_points_from_xy(
    cities,
    x="longitude",
    y="latitude",
    icon_names=["gear", "map", "leaf", "globe"],
    spin=True,
    add_legend=True,
    )

m.to_streamlit(height=700)
