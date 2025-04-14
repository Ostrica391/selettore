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
val3 = st.number_input("Inserisci TD lente°", value=14.00, step=0.05, format="%.2f")

# Lista delle voci
voci = ["SiHy7", "SiHy6", "B5X", "B4X", "B3X", "M7", "M4", "M3"]

# Valori extra da aggiungere per ogni voce
extra_valori = {
    "SiHy7": 350,
    "SiHy6": 300,
    "B5X": 250,
    "B4X": 200,
    "B3X": 150,
    "M7": 100,
    "M4": 50,
    "M3": 0
}

# Menu a tendina
scelta = st.selectbox("Seleziona il materiale:", voci)

# Calcolo base
risultato_base = (val1 + val2) / 2 + ((val3 - 10) * 400)

# Ottieni valore extra
valore_extra = extra_valori.get(scelta, 0)

# Risultato finale
risultato = risultato_base + valore_extra

# Output
st.subheader(f"Sag da ordinare: {risultato:.2f}")

# Calcolo del raggio base
rb = ((val3 * 1000)**2 / (8000 * risultato)) + (risultato / 2000)

st.markdown(f"<h4 style='color:#004890;'>Raggio base da ordinare: <b>{rb:.2f}</b> mm</h4>", unsafe_allow_html=True)
