import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION DES IDENTIFIANTS (Mets tes codes ici) ---
# Ton Client ID obtenu sur Google Cloud
GOOGLE_CLIENT_ID = "TON_CLIENT_ID_ICI.apps.googleusercontent.com"
# Ton API Key Gemini
API_KEY = "AQ.Ab8RN6LHaSlLd8Djldm4mhAG1F8fZ-PivNM6UiYnMa_c0q9BwQ"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- CONFIGURATION INTERFACE ---
st.set_page_config(page_title="NEXA Global Intelligence", layout="wide")

# Design fidèle à tes images (1000086052.jpg)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #21262d; color: white; border: 1px solid #30363d; }
    .premium-card { background: linear-gradient(135deg, #1e3a8a, #1e40af); padding: 15px; border-radius: 10px; border: 1px solid #3b82f6; }
    </style>
    """, unsafe_allow_html=True)

# Navigation
if "section" not in st.session_state:
    st.session_state.section = "NEXA Brain"

with st.sidebar:
    st.title("NEXA Global")
    if st.button("🧠 NEXA Brain"): st.session_state.section = "NEXA Brain"
    if st.button("🖼️ Images & 3D (Gratuit)"): st.session_state.section = "Free"
    if st.button("🎬 Studio Premium (Payant)"): st.session_state.section = "Premium"
    st.write("---")
    st.markdown("👤 *Utilisateur : Guerrier Karl Alejandro*")

# --- LOGIQUE DES PAGES ---

# 1. NEXA Brain (IA Textuelle)
if st.session_state.section == "NEXA Brain":
    st.subheader("🧠 NEXA Brain Intelligence")
    # Logique de chat standard...

# 2. Section GRATUITE (Images et Plans 3D)
elif st.session_state.section == "Free":
    st.subheader("🎨 Génération Gratuite")
    mode = st.radio("Choisis ton outil :", ["Générateur d'Images", "Plan 3D (Ville/Pays)"])
    
    prompt = st.text_input("Que voulez-vous créer ?")
    if st.button("Lancer la création gratuite"):
        with st.spinner("NEXA travaille..."):
            if mode == "Générateur d'Images":
                st.info("Utilisation du modèle Nano Banana 2...")
                # L'IA génère l'image ici
            else:
                st.success(f"Plan 3D de {prompt} en cours de rendu via Google Earth 3D...")

# 3. Section PREMIUM (Vidéos, Musique, Films)
elif st.session_state.section == "Premium":
    st.subheader("💎 NEXA Studio Premium")
    st.markdown("<div class='premium-card'>Générez des vidéos 4K, de la musique et des films comiques.</div>", unsafe_allow_html=True)
    
    media_type = st.selectbox("Type de média :", ["Film Comique", "Musique Originale (Lyria 3)", "Vidéo Cinématique (Veo)"])
    details = st.text_area("Détails du script ou de l'ambiance :")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("💰 *Prix : 2.50$ USD*")
    with col2:
        if st.button("Payer avec MonCash/PayPal"):
            st.warning("Redirection vers la passerelle sécurisée...")
