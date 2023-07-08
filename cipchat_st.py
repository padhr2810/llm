
"""
https://www.youtube.com/watch?v=MlK6SIjcjE8
"""

import os 
#from apikey import apikey 

import streamlit as st 
from langchain.llms import OpenAI 

#os.environ['OPENAI_API_KEY'] = apikey 


st.title('CIPChat') 
prompt = st.text_input('Plug in your prompt here')
