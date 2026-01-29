const API_URL = 'http://127.0.0.1:8000/chat';

const chatInput = document.getElementById('chat-input');
const sendBtn = document.getElementById('send-btn');
const chatHistory = document.getElementById('chat-history');

// Simulating session history in frontend for this demo
let history = [];

// Handle Enter key
chatInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

sendBtn.addEventListener('click', sendMessage);

async function sendMessage() {
    const text = chatInput.value.trim();
    if (!text) return;

    // Add User Message
    addMessageToUI('user', text);
    chatInput.value = '';

    // Disable input while generating
    setLoading(true);

    try {
        // Collect history for context (simplified)
        // In a real app, backend handles session state mainly
        const payload = {
            history: history
        };

        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error("API Error");

        const data = await response.json();

        // Add Assistant Message
        addMessageToUI('assistant', data.response);

    } catch (error) {
        addMessageToUI('assistant', `⚠️ Error: ${error.message}`);
    } finally {
        setLoading(false);
    }
}

function addMessageToUI(role, text) {
    // Add to local history stack
    history.push({ role, content: text });

    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${role}`;

    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.innerText = role === 'user' ? '👤' : '🤖';

    const content = document.createElement('div');
    content.className = 'content';

    // Parse Markdown for Assistant only (or both)
    // Using marked.js if available, else plain text
    if (window.marked) {
        content.innerHTML = marked.parse(text);
    } else {
        content.innerText = text;
    }

    msgDiv.appendChild(avatar);
    msgDiv.appendChild(content);

    chatHistory.appendChild(msgDiv);
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

function setLoading(isLoading) {
    sendBtn.disabled = isLoading;
    chatInput.disabled = isLoading;
    if (isLoading) {
        sendBtn.innerText = "Thinking...";
    } else {
        sendBtn.innerText = "Send 🚀";
        chatInput.focus();
    }
}
