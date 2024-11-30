import streamlit as st
from datetime import timedelta, time, datetime

menu = st.sidebar.radio("Navegue:", ["Agendamento", "Reagendamento", "Cancelamento"])

if menu == "Agendamento":
    st.title("Agendamento")
    with st.form(key="agendamento_form"):
        doctor_name = st.selectbox("Nome do Psicólogo:", sorted(["Thayane", "Ana", "Carlos"]))
        patient_name = st.selectbox("Nome do paciente:", ["Thalita", "Diogo", "Joao"])
        day = st.date_input("Dia do agendamento:", format="DD/MM/YYYY")
        initial_time = st.time_input("Hora inicial:", time(9, 0))
        submit = st.form_submit_button("Confirmar")
        
        # Add 50 minutes using datetime and timedelta
        final_time = (datetime.combine(datetime.min, initial_time) + timedelta(minutes=50)).time()

        if submit:
            st.success(f"Agendamento realizado com sucesso para {patient_name} com {doctor_name} no dia {day.strftime('%d/%m/%Y')} das {initial_time} às {final_time}.")
            
elif menu == "Reagendamento":
    st.title("Reagendamento")
    with st.form(key="agendamento_form"):
        doctor_name = st.selectbox("Nome do Psicólogo:", sorted(["Thayane", "Ana", "Carlos"]))
        patient_name = st.selectbox("Nome do paciente:", ["Thalita", "Diogo", "Joao"])
        day = st.date_input("Dia do agendamento:", format="DD/MM/YYYY")
        initial_time = st.time_input("Hora inicial:", time(9, 0))
        submit = st.form_submit_button("Confirmar")
        
        # Add 50 minutes using datetime and timedelta
        final_time = (datetime.combine(datetime.min, initial_time) + timedelta(minutes=50)).time()

        if submit:
            st.success(f"Agendamento realizado com sucesso para {patient_name} com {doctor_name} no dia {day.strftime('%d/%m/%Y')} das {initial_time} às {final_time}.")
            
elif menu == "Cancelamento":
    st.title("Cancelamento")
    with st.form(key="agendamento_form"):
        doctor_name = st.selectbox("Nome do Psicólogo:", sorted(["Thayane", "Ana", "Carlos"]))
        patient_name = st.selectbox("Nome do paciente:", ["Thalita", "Diogo", "Joao"])
        day = st.date_input("Dia do agendamento:", format="DD/MM/YYYY")
        initial_time = st.time_input("Hora inicial:", time(9, 0))
        submit = st.form_submit_button("Confirmar")
        
        # Add 50 minutes using datetime and timedelta
        final_time = (datetime.combine(datetime.min, initial_time) + timedelta(minutes=50)).time()

        if submit:
            st.success(f"Agendamento realizado com sucesso para {patient_name} com {doctor_name} no dia {day.strftime('%d/%m/%Y')} das {initial_time} às {final_time}.")
            
            
