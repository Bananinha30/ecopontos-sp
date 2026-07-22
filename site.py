import streamlit as st 
import folium 
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Ecocoleta")
st.divider()

st.button("Teste deste botão")

st.write("Teste do site")

tab1, tab2 = st.tabs(["Pontos de coleta", "Pontos eletronicos"])

with tab1:
    st.header("Pontos de coleta")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://infonet.com.br/wp-content/uploads/2025/08/Pontos-de-coleta-foto-PMA-28082025.jpg  ")
    with col2: 
        st.write("Estes pontos de coleta estão espalhados pelo mundo inteiro, nesta demonstração iremos mostrar todos os 125 pontos de São Paulo")
with tab2: 
    st.header("Pontos de eletronicos")
