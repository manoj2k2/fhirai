import streamlit as st
import ollama as ollama
import rest_client as rc

def ollama_chat(prompt, model="deepseek-r1:1.5b"):
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']


# Title of the app
st.title("Sahani AI Chatbot")

# Initialize session state for storing chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "bot", "content": "Hello! How can I assist you today?"}]

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**Bot:** {message['content']}")

# Input box for user message
user_input = st.text_input("Type your message:", key="user_input", 
                           value="Patient: manoj sahani, Male, 1984-01-01")

user_input_ai = st.text_input("Ask Ollama:")
if user_input_ai:
    st.write(ollama_chat(user_input_ai))

# Handle user input
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    api_response= rc.call_health_agent_api_Status()
    st.session_state.messages.append({"role": "api", "content": api_response})

    api_response_map= rc.call_health_agent_api(user_input)
    st.session_state.messages.append({"role": "api", "content": api_response_map})
    # # Generate a simple bot response
    # bot_response = f"I heard you say: '{user_input}'"
    # st.session_state.messages.append({"role": "bot", "content": bot_response})

    # Clear input box
    # st.session_state.user_input = ""