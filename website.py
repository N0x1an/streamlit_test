import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from time import sleep

# --- TITLE & MARKDOWN ---
st.title("🌟 Streamlit Demo App")
st.markdown("""
This app demonstrates **Streamlit** capabilities in one simple page:
- Inputs
- Outputs
- Charts
- Tables
- File uploads
- Session state
- Progress bars
""")

# --- INPUTS ---
name = st.text_input("What's your name?", "Streamlit User")
age = st.slider("Select your age", 1, 100, 25)
st.write(f"Hello, {name}! You are {age} years old.")

if st.button("Click me"):
    st.success("Button clicked!")

# --- SESSION STATE DEMO ---
if 'counter' not in st.session_state:
    st.session_state['counter'] = 0
if st.button("Increase counter"):
    st.session_state['counter'] += 1
st.write(f"Counter value: {st.session_state['counter']}")

# --- FILE UPLOAD ---
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Here’s your data:")
    st.dataframe(df)

# --- DATA TABLE ---
st.subheader("Sample Data Table")
data = pd.DataFrame({
    'A': np.random.randn(10),
    'B': np.random.randn(10)
})
st.dataframe(data)

# --- MATPLOTLIB CHART ---
st.subheader("Matplotlib Chart")
fig, ax = plt.subplots()
ax.plot(data['A'], data['B'], marker='o')
ax.set_title("A vs B")
st.pyplot(fig)

# --- PLOTLY CHART ---
st.subheader("Plotly Chart")
fig2 = px.scatter(data, x='A', y='B', title="Plotly Scatter Example")
st.plotly_chart(fig2)

# --- IMAGES ---
st.subheader("Image Display")
st.image("https://placekitten.com/400/300", caption="Kitten Placeholder")

# --- PROGRESS BAR ---
st.subheader("Progress Bar")
progress = st.progress(0)
for percent in range(100):
    sleep(0.01)
    progress.progress(percent + 1)

# --- END ---
st.info("🎉 This is the end of the demo. Feel free to edit and expand!")

