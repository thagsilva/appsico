import streamlit as st

    
# Sample username and password for demonstration
USERNAME = "admin"
PASSWORD = "123"

st.title("Autenticação")

# Create a login form
username = st.text_input("Usuário")
password = st.text_input("Senha", type="password")

if st.button("Login"):
    if username == USERNAME and password == PASSWORD:
        st.switch_page("pages/home.py")
    else:
        st.error("Usuário ou senha inválidos.")
