import streamlit as st
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY"
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

st.title("Gemini Chat Agent")

# Initialize conversation history in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display conversation history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Agent:** {msg['content']}")

def process_input():
    user_input = st.session_state["user_input"]
    if user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})
        response = model.invoke([HumanMessage(content=user_input)])
        st.session_state["messages"].append({"role": "agent", "content": response.content})
        st.session_state["user_input"] = ""  # This works inside the callback

if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

st.text_input("Ask something:", key="user_input", on_change=process_input)
