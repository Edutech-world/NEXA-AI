// Ta clé API Google Gemini
const NEXA_CORE_KEY = "AQ.Ab8RN6LHaSlLd8Djldm4mhAG1F8fZ-PivNM6UiYnMa_c0q9BwQ"; 

const displayArea = document.getElementById('display-area');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

async function callNexa(message) {
    const url = https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${NEXA_CORE_KEY};
    
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                contents: [{ parts: [{ text: message }] }]
            })
        });
        const data = await response.json();
        return data.candidates[0].content.parts[0].text;
    } catch (e) {
        return "Erreur de connexion au noyau NEXA.";
    }
}

function appendMessage(role, text) {
    const msg = document.createElement('div');
    msg.className = message ${role}-msg;
    msg.innerHTML = <div class="bubble">${text}</div>;
    displayArea.appendChild(msg);
    displayArea.scrollTop = displayArea.scrollHeight;
}

sendBtn.addEventListener('click', async () => {
    const text = userInput.value.trim();
    if(!text) return;

    appendMessage('user', text);
    userInput.value = "";

    const loading = document.createElement('div');
    loading.innerText = "NEXA analyse...";
    displayArea.appendChild(loading);

    const reply = await callNexa(text);
    displayArea.removeChild(loading);
    appendMessage('nexa', reply);
});