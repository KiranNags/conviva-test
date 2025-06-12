
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Conviva Test Player", layout="wide")
st.title("🎥 Conviva Test Player (Embedded)")
st.markdown("This embeds the HTML video player page with DPI and VideoSensor.")

with open("index.html", 'r') as f:
    html_content = f.read()

components.html(html_content, height=700, scrolling=True)
