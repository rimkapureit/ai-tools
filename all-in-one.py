import time
import streamlit as st

from SimplerLLM.language.llm import LLM, LLMProvider
from SimplerLLM.tools.generic_loader import load_content

llm_instance = LLM.create(provider=LLMProvider.OPENAI, model_name="gpt-4o")

st.title("10 best AI tools")

tool1 = "Ask any question"
tool2 = "Blog post generator"
tool3 = "YT ideas"
option = st.selectbox("Your 10 prefered tools are listed below:", (tool1, tool2 , tool3), index=None, placeholder="choose an option")

# Ask any question section

if option == tool1:
 st.header(tool1)
 user_input = st.text_input("No need for search engines for the information you’re looking for.:")
 summarize_prompt = f"Please give me the details answer about {user_input} this. The answer should be specific.: "
 generated_text = llm_instance.generate_response(prompt=summarize_prompt)

 if st.button("Show me the magic"): 
   with st.spinner("Wait for it ..."):
    time.sleep(3)
    st.success("Here it is :")
    st.write(generated_text)

# Blog post generator section

if option == tool2:
 st.header(tool2)
 user_input = st.text_input("write key idea to your blog post")
 summarize_prompt = f"Please give me some blog post ideas related to this topic {user_input}  "
 generated_text = llm_instance.generate_response(prompt=summarize_prompt)

 if st.button("Show me the magic"): 
   with st.spinner("Wait for it ..."):
    time.sleep(3)
    st.success("Here it is :")
    st.write(generated_text)