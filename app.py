# UNIFICAZIONE DUE CALCOLATORI IN UNA SOLA APP STREAMLIT

import streamlit as st
from PIL import Image
import base64
import io

# --- FUNZIONE UTILE ---
def pil_to_base64(img):
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode()
    return encoded

# --- STILE GENERALE ---
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
    .top-menu {
        position: absolute;
        top: 60px;
        left: 0px;
        z-index: 1;
    }
    .top-menu button {
        display: block;
        background-color: #004890;
        color: white;
        padding: 8px 16px;
        margin-bottom: 8px;
        border: none;
        border-radius: 6px;
        font-size: 14px;
        text-align: center;
        width: 160px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        cursor: pointer;
    }
    .top-menu button:hover {
        background-color: #0060b0;
    }
    </style>
""", unsafe_allow_html=True)

# --- MENU ---
st.markdown("""
    <div class="top-menu">
        <form action="" method="post">
            <button name="page" value="cs">Calcolatore CS</button>
            <button name="page" value="scl">Calcolatore SCL-ADV</button>
            <button name="page" value="wip">Work in progress</button>
            <button name="page" value="wip2">Work in progress</button>
        </form>
    </div>
""", unsafe_allow_html=True)

# --- LOGO ---
st.markdown("""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,""" + base64.b64encode(open("TSLAC.png", "rb").read()).decode() + """' style='width: 400px; margin-bottom: 10px;'>
    </div>
""", unsafe_allow_html=True)

# --- SCELTA PAGINA ---
if 'page' not in st.session_state:
    st.session_state.page = 'cs'

# Hack per cambiare pagina via pulsanti
page = st.query_params.get("page", st.session_state.page)
st.session_state.page = page

# --- CALCOLATORE CS ---
def mostra_calcolatore_cs():
    st.title("Selettore CS - TS LAC")
    val1 = st.number_input("Inserisci SAG 5.00mm 0°", value=1700, step=10)
    val2 = st.number_input("Inserisci SAG 5.00mm 180°", value=1700, step=10)
    val3 = st.number_input("Central Clearance", value=250, step=5)
    risultato = (val1 + val2) / 2 + 1080 + val3
    st.markdown(f"### SAG Lente: {int(risultato)} µm")

    indice = None
    if 2080 <= risultato <= 3050:
        indice = 0
    elif 3051 <= risultato <= 3200:
        indice = 1
    elif 3201 <= risultato <= 3300:
        indice = 2
    elif 3301 <= risultato <= 3400:
        indice = 3
    elif 3401 <= risultato <= 3500:
        indice = 4
    elif 3501 <= risultato <= 3650:
        indice = 5
    elif 3651 <= risultato <= 3900:
        indice = 6

    paths = [f"cs{i+1}.png" for i in range(7)]
    labels = ["SAG 3000µm", "SAG 3150µm", "SAG 3250µm", "SAG 3350µm", "SAG 3450µm", "SAG 3600µm", "SAG 3850µm"]

    show_cassette(paths, labels, [indice] if indice is not None else [])

    # immagini finali
    for img_name in ["totalsag.png", "totalsagb.png", "totalsagc.png"]:
        with open(img_name, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            st.markdown(f"""
                <div style='margin-top: 30px; text-align: center;'>
                    <img src='data:image/png;base64,{encoded}' style='width: 650px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);'>
                </div>
            """, unsafe_allow_html=True)

# --- CALCOLATORE SCL ADV ---
def mostra_calcolatore_scl():
    st.title("Selettore SCL ADV - TS LAC")
    val1 = st.number_input("Inserisci SAG 5.00mm 0°", value=1800, step=10)
    val2 = st.number_input("Inserisci SAG 5.00mm 180°", value=1800, step=10)
    val3 = st.number_input("Central Clearance", value=350, step=10)

    risultato = (val1 + val2) / 2 + 2000 + val3
    risultato2 = (val1 + val2) / 2 + 1200 + val3
    st.markdown(f"### SAG Lente: {int(risultato)} µm")

    indici = []
    for (rng, idx) in [((3600, 3850), 0), ((3851, 4050), 1), ((4051, 4250), 2), ((4251, 4450), 3),
                       ((4451, 4650), 4), ((4651, 4850), 5), ((4851, 5050), 6),
                       ((3200, 3450), 7), ((3451, 3650), 8), ((3651, 3850), 9),
                       ((3900, 4150), 10), ((4151, 4350), 11), ((4351, 4550), 12), ((4551, 4750), 13)]:
        if (idx < 7 and rng[0] <= risultato <= rng[1]) or (idx >= 7 and rng[0] <= risultato2 <= rng[1]):
            indici.append(idx)

    paths = [f"scl{i+1}.png" for i in range(7)]
    labels = ["SAG 3800µm", "SAG 4000µm", "SAG 4200µm", "SAG 4400µm", "SAG 4600µm", "SAG 4800µm", "SAG 5000µm"]

    paths_2 = [f"scl{i+8}.png" for i in range(7)]
    labels_2 = ["SAG 3400µm", "SAG 3600µm", "SAG 3800µm", "SAG 4100µm", "Toric SAG 4300µm", "Toric SAG 4500µm", "Toric SAG 4700µm"]

    show_double_cassette(paths, labels, paths_2, labels_2, indici)

    for img_name in ["scladv1.png", "scladv2.png"]:
        with open(img_name, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            st.markdown(f"""
                <div style='margin-top: 30px; text-align: center;'>
                    <img src='data:image/png;base64,{encoded}' style='width: 600px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);'>
                </div>
            """, unsafe_allow_html=True)

# --- FUNZIONI DI VISUALIZZAZIONE ---
def show_cassette(paths, labels, selected):
    st.markdown("<div class='cassette'>", unsafe_allow_html=True)
    html = "<div style='display: flex; justify-content: center; gap: 25px;'>"
    for i, path in enumerate(paths):
        img = Image.open(path)
        encoded = pil_to_base64(img)
        arrow = "<div class='arrow'>⬇️</div>" if i in selected else ""
        highlight = "selected" if i in selected else ""
        html += f"<div class='lens'>{arrow}<img src='data:image/png;base64,{encoded}' style='width: 190px; border-radius: 10px;' class='{highlight}'><div>{labels[i]}{' (Lente ideale)' if i in selected else ''}</div></div>"
    html += "</div>"
    st.markdown(html + "</div>", unsafe_allow_html=True)

def show_double_cassette(paths1, labels1, paths2, labels2, selected):
    st.markdown("<div class='cassette'>", unsafe_allow_html=True)
    for paths, labels, offset in [(paths1, labels1, 0), (paths2, labels2, 7)]:
        html = "<div class='cassette-row'>"
        for i, path in enumerate(paths):
            img = Image.open(path)
            encoded = pil_to_base64(img)
            idx = i + offset
            arrow = "<div class='arrow'>⬇️</div>" if idx in selected else ""
            highlight = "selected" if idx in selected else ""
            html += f"<div class='lens'>{arrow}<img src='data:image/png;base64,{encoded}' style='width: 190px; border-radius: 10px;' class='{highlight}'><div>{labels[i]}{' (Lente ideale)' if idx in selected else ''}</div></div>"
        html += "</div>"
        st.markdown(html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- AVVIO ---
if page == "cs":
    mostra_calcolatore_cs()
elif page == "scl":
    mostra_calcolatore_scl()
else:
    st.title("Work in progress 🛠")
