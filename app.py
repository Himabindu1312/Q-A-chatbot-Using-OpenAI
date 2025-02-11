import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


import os
from dotenv import load_dotenv

load_dotenv()

##langsmith tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("langchain_api_key")
os.environ["LANGCHAIN_TRACING_V2"] = 'true'
os.environ["LANGCHIAN_PROJECT"] = "Q&A chatbot with OPENAI"


# #prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant, please respond to the user queries."),
        ("user","Question:{question}")
     ]
 )


def generate_response(question,api_key, engine, temperature , max_tokens):
    llm = ChatOpenAI(
        model=engine,
        openai_api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser


    try:
        # Generate the response using the chain
        answer = chain.invoke({'question': question})
        return answer
    except Exception as e:
        return f"Error: {e}"


##title of app
st.title('Q&A Chatbot with OPENAI')

api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

# ##drop down to select openai models
engine = st.sidebar.selectbox("Select an Open AI model", ['gpt-4o', 'gpt-4-turbo', 'gpt-4'])

temperature = st.sidebar.slider("Temperature", min_value = 0.0, max_value = 1.0, value = 0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value= 50, max_value= 1000, value = 150)

#main interface for user input
st.write("What can I help with?")
user_input = st.text_input("Message to model")

if user_input:
    response = generate_response(user_input,api_key, engine, temperature, max_tokens)
    st.write(response)
elif user_input: 
    st.warning("Please enter the Open AI api key in the side bar")
else:
    st.write("Please provide appropriate query")