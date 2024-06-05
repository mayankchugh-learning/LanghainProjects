from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# os.environ["OPENAI_MODEL_NAME"]=os.getenv("OPENAI_MODEL_NAME")
os.environ["ANY_SCALE_API_KEY"]=os.getenv("ANY_SCALE_API_KEY")
os.environ["ANY_SCALE_API_BASE"]=os.getenv("ANY_SCALE_API_BASE")
anyscale_base_url = os.environ["ANY_SCALE_API_BASE"]
anyscale_api = os.environ["ANY_SCALE_API_KEY"]
model = 'mistralai/Mixtral-8x7B-Instruct-v0.1'

#model = os.environ["OPENAI_MODEL_NAME"]
## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI using Lancghain")

    
input_text=st.text_input("Enter text to search")

llm = ChatOpenAI(
     model=model,
     base_url=anyscale_base_url,
     api_key=anyscale_api
)


output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))