import streamlit as st

with st.chat_message("user"):
    st.write("Hello 👋")
st.radio("Pick one", ["cats", "dogs"])
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

st.snow()