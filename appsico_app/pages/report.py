import streamlit as st
from datetime import datetime


menu = st.sidebar.radio("Navegue:", ["Novo relatório", "Editar relatório"])


if menu == "Novo relatório":
    
    st.title("Relatório")
    
    with st.form(key="relatorio_form", enter_to_submit=False):
        patient_name = st.selectbox("Nome do paciente:", ["Thalita", "Diogo", "João"])
        
        date_now = datetime.now().strftime(format='%d/%m/%Y')    
        report = st.text_area(f"Relatório do dia {date_now}.", height=500)
        submit = st.form_submit_button("Submeter")

        if submit:
            st.success(f"Relatório do paciente {patient_name} submetido com sucesso.")


elif menu == "Editar relatório":
    
    st.title("Relatório")
    
    with st.form(key="relatorio_form", enter_to_submit=False):
        patient_name = st.selectbox("Nome do paciente:", ["Thalita", "Diogo", "João"])
        
        date_now = datetime.now().strftime(format='%d/%m/%Y')    
        report = st.text_area(f"Relatório do dia {date_now}.", height=500)
        submit = st.form_submit_button("Submeter")

        if submit:
            st.success(f"Relatório do paciente {patient_name} submetido com sucesso.")


