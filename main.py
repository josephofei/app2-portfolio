import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Joseph Ofei")
    content = """
Hi, my name is Joseph Ofei, I am a python pragram with 2 years of experience and willing to gain new and more skills.
"""
    st.info(content)
