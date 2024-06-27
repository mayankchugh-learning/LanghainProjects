# Streamlit is a powerful open-source framework used for building web applications with interactive data visualizations and machine learning models. To import Streamlit, you'll need to ensure that you have it installed in your Python environment.
# Once you have Streamlit installed, you can import it into your Python script using the import statement,

import streamlit as st
# Use a pipeline as a high-level helper
import torch
from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM, Conversation

#As Langchain team has been working aggresively on improving the tool, we can see a lot of changes happening every weeek,
#As a part of it, the below import has been depreciated

#When deployed on huggingface spaces, this values has to be passed using Variables & Secrets setting, as shown in the video :)

# response_generator = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3")

modelname = ("/Users/mayankchugh/gitRepos/mayankchugh.learning/HuggingFace-ML-GenerativeAI-Gradio-Streamlit-Apps/Models/models--mistralai--Mistral-7B-Instruct-v0.3/snapshots/83e9aa141f2e28c82232fea5325f54edf17c43de")

# hand over model & tokenizer instantiations to pipeline
model = AutoModelForCausalLM.from_pretrained(modelname)
tokenizer = AutoTokenizer.from_pretrained(modelname)
tokenizer.pad_token_id = tokenizer.eos_token_id

response_generator = pipeline("text-generation", model=modelname, tokenizer=tokenizer, framework='pt')

#Function to return the response
def load_answer(question):
    answer = response_generator(question)
    return answer


#App UI starts here
st.set_page_config(page_title="LangChain Demo - Chatbot ", page_icon=":robot:")
st.header("LangChain Demo")

#Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input=get_text()
response = load_answer(user_input)

submit = st.button('Generate')  

#If generate button is clicked
if submit:

    st.subheader("Answer:")

    st.write(response)

