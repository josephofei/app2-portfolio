import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Joseph Ofei")
    content = """
I am a software engineer with a Certificate from the Flatiron School. During my time at Flatiron School, I acquired a strong foundation in crafting powerful web applications using a variety of technologies, including JavaScript, React, Python, Flask, Ruby, Rails, and SQL. Additionally, my educational background includes Google Data Analytics Certificate, IBM FullStack Developer Certificate. These certificates have equipped me with essential skills in leadership, communication, problem-solving and most importantly a better coder.  My passion for coding is deeply rooted in the boundless possibilities it offers for shaping our world. From launching rockets into space to engineering groundbreaking solutions, I see coding as a means to contribute to the future of technology, where innovation is not confined to a single field but serves as a global catalyst for progress. As a dedicated software engineer, I thrive on embracing new challenges and am committed to continually expanding my skill set.
"""
    st.info(content)

content = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
text = st.write(content)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])
        st.write(f"[source code]({row['url']})")
