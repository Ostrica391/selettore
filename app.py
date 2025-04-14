import streamlit as st
from PIL import Image, ImageOps
import base64
import io

# Sfondo gradiente più marcato: bianco -> blu profondo + larghezza massima container
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #ffffff, #ffffff);
        background-attachment: fixed;
    }
    .block-container {
        max-width: 90% !important;
        padding: 2rem 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# Menu link in alto a sinistra
st.markdown("""
    <style>
    .top-menu {
        position: absolute;
        top: 60px;
        left: 0px;
        z-index: 1;
    }
    .top-menu a {
        display: block;
        background-color: #004890;
        color: white;
        padding: 8px 16px;
        margin-bottom: 8px;
        text-decoration: none;
        border-radius: 6px;
        font-size: 14px;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        transition: background 0.3s;
    }
    .top-menu a:hover {
        background-color: #0060b0;
    }
    </style>
    <div class="top-menu">
        <a href="https://selettore-cs.streamlit.app/" target="_blank">Calcolatore CS</a>
        <a href="https://selettore-scl-adv.streamlit.app/" target="_blank">Calcolatore SCL-ADV</a>
        <a href="https://www.tslac.it/">Work in progress</a>
        <a href="https://www.tslac.it/">Work in progress</a>
    </div>
""", unsafe_allow_html=True)

# Logo centrato
st.markdown("""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,""" + base64.b64encode(open("TSLAC.png", "rb").read()).decode() + """' style='width: 400px; margin-bottom: 10px;'>
    </div>
""", unsafe_allow_html=True)

# Titolo
st.title("Morbide Sagittali - TS LAC")

# Input
val1 = st.number_input("Inserisci SAG 5.00mm 0°", value=1700, step=10)
val2 = st.number_input("Inserisci SAG 5.00mm 180°", value=1700, step=10)

# Lista delle voci
voci = ["Voce 1", "Voce 2", "Voce 3", "Voce 4", "Voce 5", "Voce 6", "Voce 7"]

# Menu a tendina
scelta = st.selectbox("Seleziona una voce:", voci)

# Mostra la voce selezionata
st.write(f"Hai selezionato: {scelta}")
