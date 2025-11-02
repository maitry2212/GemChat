import streamlit as st
from graph import create_chat_graph
from memory_manager import save_conversation, list_conversations, load_conversation

# --- Page Config ---
st.set_page_config(page_title="Chatbot", layout="wide")

st.title("Chatbot")
st.sidebar.title("🧠 Conversations")

# --- Load Session ---
if "messages" not in st.session_state:
    st.session_state.messages = []

graph = create_chat_graph()

# Sidebar controls
convos = list_conversations()
selected = st.sidebar.selectbox("📜 Load Conversation", ["New Chat"] + convos)

if selected != "New Chat":
    st.session_state.messages = load_conversation(selected)
    st.sidebar.success(f"Loaded: {selected}")

if st.sidebar.button("🆕 New Conversation"):
    st.session_state.messages = []

# --- Display previous messages ---
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# --- Chat input + streaming output ---
if prompt := st.chat_input("Type your message..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Assistant streaming response
    with st.chat_message("assistant"):
        state = {"user_input": prompt}
        with st.spinner("Thinking..."):
            stream_placeholder = st.empty()
            final_response = ""

            for event in graph.stream(state):
                if not event:
                    continue
                # Each event = {'chat': {'response': 'partial text'}}
                for node_name, node_output in event.items():
                    if isinstance(node_output, dict) and "response" in node_output:
                        chunk = node_output["response"]
                        if chunk:
                            final_response += chunk
                            stream_placeholder.markdown(final_response + "▌")

            stream_placeholder.markdown(final_response)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": final_response})

# --- Save button ---
if st.button("💾 Save Conversation"):
    file_path = save_conversation(st.session_state.messages)
    st.success(f"Saved to {file_path}")