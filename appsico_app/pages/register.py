import streamlit as st


st.title("Cadastro de paciente")
with st.form(key="cadastro_form"):
    patient_name = st.text_input("Nome do paciente:")
    email = st.text_input("E-mail do paciente:")
    doctor_name = st.selectbox("Nome do médico:", ["Dr. João", "Dr. Ana", "Dr. Carlos"])
    submit = st.form_submit_button("Cadastrar")

    if submit:
        st.success(f"Paciente {patient_name} cadastrado com sucesso com o e-mail {email} para o médico {doctor_name}.")