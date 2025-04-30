import streamlit as st

if "click_count" not in st.session_state:
    st.session_state.click_count = 0
    st.text_area("Counter name", key="counter_name")

def click():
    st.session_state.click_count += 1

'Pre, ', st.session_state.click_count
st.button('Click me', on_click=click)
'Post, ', st.session_state.counter_name, st.session_state.click_count