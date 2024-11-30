import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Assistente", "Psicologista", "Admin"]


def login():

    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
home = st.Page(
    "pages/home.py",
    title="Página inicial",
    icon=":material/help:",
    # default=(role == "Assistente"), 
)
management = st.Page(
    "pages/management.py",
    title="Gestão de consultas", 
    icon=":material/bug_report:",
    default=(role == "Assistente"),
)
register = st.Page(
    "pages/register.py",
    title="Cadastro de clientes",
    icon=":material/healing:",
    # default=(role == "Assistente"),
)
report = st.Page(
    "pages/report.py",
    title="Relatórios",
    icon=":material/security:",
    default=(role == "Psicologista"),
)
admin_1 = st.Page(
    "pages/admin_1.py",
    title="Admin 1",
    icon=":material/person_add:",
    default=(role == "Admin"),
)

account_pages = [home, logout_page, settings]
assistent_pages = [management, register]
psychologist_pages = [report]
admin_pages = [admin_1]

st.logo("images/logo.png", icon_image="images/logo.png")

page_dict = {}
if st.session_state.role in ["Assistente", "Admin"]:
    page_dict["Assistente"] = assistent_pages
if st.session_state.role in ["Psicologista", "Admin"]:
    page_dict["Psicologista"] = psychologist_pages
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Conta": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()

# import streamlit as st

# def main():
    
#     st.set_page_config(page_title="Appsico", page_icon="🤖")
    
#     pages = {
#         "Menu": [
#             # st.Page("pages/authentication.py", title="Autenticação"),
#             st.Page("pages/home.py", title="Página inicial"),
#             st.Page("pages/management.py", title="Gestão de consultas"),
#             st.Page("pages/register.py", title="Cadastro de clientes"),
#             st.Page("pages/report.py", title="Relatórios"),
#         ],
#     }

#     pg = st.navigation(pages)
#     pg.run()
    

# if __name__ == "__main__":
#     main()
