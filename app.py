import streamlit as st

# Set page config (optional)
st.set_page_config(page_title="AI Unit 2", layout="wide")

# Read your HTML file
with open("ai_unit2.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Display HTML
st.components.v1.html(html_content, height=1000, scrolling=True)
