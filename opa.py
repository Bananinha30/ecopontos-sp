import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation

# Configura a página do Streamlit para ocupar a largura total
st.set_page_config(layout="wide")
st.title("📍 Localização em Tempo Real no Folium")

# 1. Inicializa as variáveis na memória do Streamlit (Session State)
# Isso impede que o app resete o mapa quando você clica ou move ele
if "lat" not in st.session_state:
    st.session_state.lat = -23.5505  # Latitude padrão (São Paulo - SP)
    st.session_state.lon = -46.6333  # Longitude padrão
    st.session_state.localizado = False

# 2. Renderiza o botão que pede permissão de GPS ao navegador
st.write("Clique no botão abaixo para capturar suas coordenadas atuais:")
location = streamlit_geolocation()

# 3. Se o navegador capturar o GPS, atualiza a memória do app
if location and location.get("latitude") is not None and not st.session_state.localizado:
    st.session_state.lat = location["latitude"]
    st.session_state.lon = location["longitude"]
    st.session_state.localizado = True
    st.rerun()  # Recarrega o app uma única vez para desenhar o novo mapa

# 4. Mostra o status atual para o usuário
if st.session_state.localizado:
    st.success(f"📍 GPS Ativo! Coordenadas: {st.session_state.lat:.4f}, {st.session_state.lon:.4f}")
else:
    st.info("ℹ️ Exibindo localização padrão. Aguardando você clicar no botão de localização acima.")

# 5. Cria o mapa centralizado nas coordenadas da memória
m = folium.Map(
    location=[st.session_state.lat, st.session_state.lon], 
    zoom_start=15
)

# 6. Adiciona o marcador da posição atual
folium.Marker(
    [st.session_state.lat, st.session_state.lon],
    tooltip="Você está aqui" if st.session_state.localizado else "Posição Padrão",
    icon=folium.Icon(color="blue" if st.session_state.localizado else "orange", icon="user")
).add_to(m)

# 7. Renderiza o mapa de forma estável na tela
st_folium(m, use_container_width=True, height=500, key="mapa_realtime")

