import streamlit as st
import os
from langchain_groq import ChatGroq
 # Import ChatGroq from langchain_groq

# Set page config
st.set_page_config(page_title="SK Chatbot")
st.title("🤖 SK Chatbot")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to get DeepSeek response
def get_deepseek_response(prompt):
    try:
        # Initialize ChatGroq with appropriate parameters
        llm = ChatGroq(
            temperature=0,
            groq_api_key='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',
            model_name="deepseek-r1-distill-qwen-32b"
        )
        
        # Invoke ChatGroq and get response
        response = llm.invoke(prompt)
        return response.content

    except Exception as e:
        return f"Error: {str(e)}"

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("How can I help you?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get and display assistant response
    with st.chat_message("assistant"):
        response = get_deepseek_response(prompt)
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content":response})
