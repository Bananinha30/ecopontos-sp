import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation
from geopy.distance import geodesic

st.set_page_config(layout="wide")

st.title("♻️ Ecopontos de São Paulo")

# localização em tempo real
location = streamlit_geolocation()

# carrega ecopontos
df = pd.read_csv("ecopontos.csv")

# centro padrão
lat = -23.5505
lon = -46.6333

if location["latitude"] is not None:
    lat = location["latitude"]
    lon = location["longitude"]

# cria mapa
m = folium.Map(
    location=[lat, lon],
    zoom_start=12
)

# usuário
folium.Marker(
    [lat, lon],
    tooltip="Você está aqui",
    icon=folium.Icon(color="blue", icon="user")
).add_to(m)

# ecopontos
for _, row in df.iterrows():

    distancia = geodesic(
        (lat, lon),
        (row["Latitude"], row["Longitude"])
    ).km

    folium.Marker(
        [row["Latitude"], row["Longitude"]],
        tooltip=row["Nome"],
        popup=f"""
        <b>{row['Nome']}</b><br>
        Distância: {distancia:.2f} km
        """,
        icon=folium.Icon(color="green", icon="trash")
    ).add_to(m)

st_folium(
    m,
    width=1200,
    height=700
)

import folium
from streamlit_folium import st_folium

if location["latitude"] is not None:

    lat = location["latitude"]
    lon = location["longitude"]

    mapa = folium.Map(
        location=[lat, lon],
        zoom_start=14
    )

    folium.Marker(
        [lat, lon],
        popup="Minha localização",
        icon=folium.Icon(color="blue", icon="user")
    ).add_to(mapa)

    st_folium(mapa, width=1200, height=700)
