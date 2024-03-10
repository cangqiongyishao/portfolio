import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Ardit Sulce')
    content="""
    Hi, He is Ardit! nice to meet you all!
    """
    st.info(content)

col3=st.columns(1)

content="""
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content)

col3,col4= st.columns(2)

df=pandas.read_csv('data.csv',sep=';')

with col3:
    for index,row in df[:10].iterrows():
        st.header(row['title'])


with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title'])