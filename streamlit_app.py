import streamlit as st

col1, col2 = st.columns([6, 6])

with col1:
   st.write("Enter your name:")
   name = st.text_area("")

with col2:
   if name != "":
       st.write(f" Hi {name}, nice to meet you !")