import streamlit as st
import google.generativeai as genai

# 1. Configuration de la page
st.set_page_config(
    page_title="NEXA Global Intelligence",
    page_icon="🌐",
    layout="centered"
)

# 2. Configuration de l'IA (Ta clé est intégrée ici)
API_KEY = "AQ.Ab8RN6LHaSlLd8Djldm4mhAG1F8fZ-PivNM6UiYnMa_c0q9BwQ"
genai.configure(api_key=API_KEY)

# Initialisation du modèle Gemini 1.5 Flash
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Style personnalisé (pour retrouver l'esprit NEXA)
st.markdown("""
    <style>
    .stApp {
        background-color: #0a0c10;
        color: white;
    }
    .stChatInput {
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 NEXA Global Intelligence")
st.subheader("Système d'intelligence centralisé")

# 4. Gestion de l'historique des messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage des anciens messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Zone de saisie utilisateur
if prompt := st.chat_input("Posez une question à NEXA..."):
    # Ajouter le message de l'utilisateur à l'historique
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Réponse de l'IA
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("NEXA réfléchit...")
        
        try:
            # Appel à l'API Gemini
            response = model.generate_content(prompt)
            full_response = response.text
            message_placeholder.markdown(full_response)
            
            # Sauvegarder la réponse dans l'historique
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            message_placeholder.markdown(f"Erreur de connexion au noyau NEXA : {e}")