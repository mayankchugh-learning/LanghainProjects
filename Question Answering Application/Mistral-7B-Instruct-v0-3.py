import os
import streamlit as st


from dotenv import load_dotenv
from langchain.llms import HuggingFaceEndpoint

load_dotenv()

os.environ["HUGGINGFACEHUB_API_TOKEN"]=os.getenv("HF_TOKEN")

huggingface_token = os.environ["HUGGINGFACEHUB_API_TOKEN"]


#llm = HuggingFaceEndpoint(
#    repo_id="mistralai/Mistral-7B-Instruct-v0.2")

# The LLM takes a prompt as an input and outputs a completion
#our_query = "What is the currency of India?"

#Last week langchain has recommended to use invoke function for the below please :)
#completion = llm.invoke(our_query)

#print(completion)

#Function to return the response


#Function to return the response
def load_answer(question):
    # "text-davinci-003" model is depreciated, so using the latest one https://platform.openai.com/docs/deprecations
    if question:
        llm = HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.2")

        #Last week langchain has recommended to use invoke function for the below please :)
        answer=llm.invoke(question)
        return answer


#App UI starts here
st.set_page_config(page_title="LangChain Demo - Mistral", page_icon=":robot:")
st.header("LangChain Demo - Mistral")

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

