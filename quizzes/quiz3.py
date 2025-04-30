import streamlit as st

if "name" not in st.session_state:
    st.session_state.name = ""

'Hi,', st.session_state.name

st.session_state.name = st.text_area("", "")

'Bye,', st.session_state.name