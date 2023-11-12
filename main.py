import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Akash Tayade")
    content1 = """
    Hi, I am Akash! I am a beginner Python programmer and a student.
     I am currently pursuing Btech. in Electronics Engineering at YCCE Nagpur.
     This is my portfolio website to showcase my Python projects. 
     (Also, this is my dog, his name is Jimmy and he's an Indian Spitz.)
    """
    st.info(content1)

content2 = """Below you can find some of the apps I have built in Python. 
              Feel free to contact me!"""

st.write(content2)