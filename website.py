import streamlit as st

st.title("My App")
st.write("Hello world!")

name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}!")