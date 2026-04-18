import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="NEXA Global Intelligence", layout="wide")

# --- STYLE CSS (Le look de ton projet) ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    
    /* Barre de connexion Google en haut à droite */
    .google-btn {
        position: absolute;
        top: 10px;
        right: 20px;
        background-color: #ffffff;
        color: #000;
        padding: 5px 15px;
        border-radius: 5px;
        font-weight: bold;
        cursor: pointer;
    }
    
    /* Style Sidebar */
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    
    /* Barre de saisie personnalisée */
    .input-container {
        display: flex;
        align-items: center;
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 20px;
        padding: 5px 15px;
    }
    </style>
    <div class="google-btn">G Sign in with Google</div>
    """, unsafe_allow_html=True)

# --- ACTIVATION API GEMINI ---
API_KEY = "AQ.Ab8RN6LHaSlLd8Djldm4mhAG1F8fZ-PivNM6UiYnMa_c0q9BwQ"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- BARRE LATÉRALE (SIDEBAR) ---
with st.sidebar:
    st.title("NEXA Global")
    st.button("🧠 NEXA Brain")
    st.button("🖼️ Generate Image")
    st.button("📂 Media Library")
    st.button("📺 NEXA TV")
    st.write("---")
    st.write("⚙️ Settings")

# --- ZONE DE CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --- BARRE DE SAISIE AVEC CAMÉRA ET VOIX ---
# On utilise des colonnes pour l'alignement exact
col_cam, col_text, col_voice = st.columns([1, 8, 1])

with col_cam:
    if st.button("📷"): # Bouton caméra à gauche
        st.toast("Caméra activée")

with col_text:
    prompt = st.chat_input("Posez une question à NEXA...")

with col_voice:
    if st.button("🎤"): # Bouton voix à droite
        st.toast("Microphone activé")

# Logique de réponse
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception:
            st.error("Erreur : L'API Gemini n'est pas activée sur Google Cloud.")
