import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.environ.get("GOOGLE_API_KEY")
)

st.title("🤖 Chat with Google Gemini 2.5")
st.write("This is a simple chat interface using Google Gemini 2.5 model.")

if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


query = st.chat_input("Type your message here...")
if query:
    st.chat_message("user").write(query)
    st.session_state.messages.append({"role": "user", "content": query})
    with st.spinner("Generating response..."):
        response = llm.invoke(query)
        st.chat_message("assistant").write(response.content)
        st.session_state.messages.append({"role": "assistant", "content": response.content})