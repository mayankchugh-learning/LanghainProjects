import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import streamlit as st

load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

groq_api_key = os.environ["GROQ_API_KEY"]

chat = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="llama3-8b-8192")

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title("💬 Chatbo using GROQ")
st.caption("🚀 A Streamlit chatbot powered by GROQ using Langchain")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

input_text=st.text_input("Enter text to search")

output_parser=StrOutputParser()
chain=prompt|chat|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))