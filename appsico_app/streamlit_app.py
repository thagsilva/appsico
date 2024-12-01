import streamlit as st
from pages.authentication import authentication

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Assistente", "Psicologista", "Paciente", "Admin"]


def login():
    
    # role = authentication()
    # st.session_state.role = role
    # st.rerun()

    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(
    logout, 
    title="Log out", 
    icon=":material/logout:")

settings = st.Page(
    "settings.py", 
    title="Settings", 
    icon=":material/settings:")

home = st.Page(
    "pages/home.py",
    title="Página inicial",
    icon=":material/help:")

management = st.Page(
    "pages/management.py",
    title="Gestão de consultas", 
    icon=":material/bug_report:",
    default=(role == "Assistente"))

register = st.Page(
    "pages/register.py",
    title="Cadastro de clientes",
    icon=":material/healing:")

report = st.Page(
    "pages/report.py",
    title="Relatórios",
    icon=":material/security:",
    default=(role == "Psicologista"))

research = st.Page(
    "pages/research.py",
    title="Pesquisa",
    icon=":material/person_add:",
    default=(role == "Paciente"))

bill = st.Page(
    "pages/bill.py",
    title="Pagamentos",
    icon=":material/person_add:")

dashboard = st.Page(
    "pages/dashboard.py",
    title="Dashboard",
    icon=":material/person_add:",
    default=(role == "Admin"))

account_pages = [home, logout_page, settings]
assistent_pages = [management, register]
psychologist_pages = [report]
patient_pages = [research, bill]
admin_pages = [dashboard]

st.logo("images/logo.png", icon_image="images/logo.png")

page_dict = {}
if st.session_state.role in ["Assistente", "Admin"]:
    page_dict["Assistente"] = assistent_pages
if st.session_state.role in ["Psicologista", "Admin"]:
    page_dict["Psicologista"] = psychologist_pages
if st.session_state.role in ["Paciente", "Admin"]:
    page_dict["Paciente"] = patient_pages
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Conta": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
