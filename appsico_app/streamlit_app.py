import streamlit as st

def main():
    
    pages = {
        "Menu": [
            st.Page("pages/home.py", title="Página inicial"),
            st.Page("pages/management.py", title="Gestão de consultas"),
            st.Page("pages/register.py", title="Cadastro de clientes"),
            st.Page("pages/report.py", title="Relatórios"),
        ],
    }

    pg = st.navigation(pages)
    pg.run()


if __name__ == "__main__":
    main()
