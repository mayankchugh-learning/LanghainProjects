#Hello! It seems like you want to import the Streamlit library in Python. Streamlit is a powerful open-source framework used for building web applications with interactive data visualizations and machine learning models. To import Streamlit, you'll need to ensure that you have it installed in your Python environment.
#Once you have Streamlit installed, you can import it into your Python script using the import statement,

import streamlit as st
# Use a pipeline as a high-level helper
import torch
from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM, Conversation

#As Langchain team has been working aggresively on improving the tool, we can see a lot of changes happening every weeek,
#As a part of it, the below import has been depreciated
#from langchain.llms import OpenAI

#New import from langchain, which replaces the above
from langchain_openai import OpenAI

#When deployed on huggingface spaces, this values has to be passed using Variables & Secrets setting, as shown in the video :)
#import os
#os.environ["OPENAI_API_KEY"] = "sk----"

#import os
#from dotenv import load_dotenv

#load_dotenv()

#os.environ["ANY_SCALE_API_KEY"]=os.getenv("ANY_SCALE_API_KEY")
#os.environ["ANY_SCALE_API_BASE"]=os.getenv("ANY_SCALE_API_BASE")
#anyscale_base_url = os.environ["ANY_SCALE_API_BASE"]
#anyscale_api_key = os.environ["ANY_SCALE_API_KEY"]
#model = 'mistralai/Mixtral-8x7B-Instruct-v0.1'

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
    # "text-davinci-003" model is depreciated, so using the latest one https://platform.openai.com/docs/deprecations
    #llm = OpenAI(model_name=model,temperature=0,base_url=anyscale_base_url,api_key=anyscale_api_key)

    #Last week langchain has recommended to use invoke function for the below please :)
    #answer=llm.invoke(question)
    return answer


#App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
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

