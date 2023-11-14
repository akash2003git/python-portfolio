import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Akash Tayade")
    content1 = """
    Hi, I am Akash! I am a beginner Python programmer and a student.
     I am currently pursuing B-tech. in Electronics Engineering at YCCE Nagpur.
     This is my portfolio website to showcase my Python projects. 
    """
    st.info(content1)

content2 = """Below you can find some of the apps I have built in Python. 
              Feel free to contact me!"""
st.write(content2)

col3, empty_col, col4 = st.columns([3, 1, 3])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row[0]) #title column
        st.write(row[1]) #description column
        st.image("images/" + row[3]) #images column
        st.write(f"[Source Code]({row[2]})") #url row

with col4:
    for index, row in df[10:].iterrows():
        st.header(row[0])
        st.write(row[1])
        st.image("images/" + row[3])
        st.write(f"[Source Code]({row[2]})")