import streamlit as st


def authentication():
    user_dict = {
        "assistente@gmail.com": 
            {
                "name": "Joana Souza",
                "role": "assistente",
                "password": "assistente1",
            },
        "psico@gmail.com": 
            {
                "name": "Thayane Guimarães",
                "role": "psicologista",
                "password": "psicologista1",
            },
        "diogofs@msn.com": 
            {
                "name": "Diogo F S",
                "role": "paciente",
                "password": "paciente1",
            },
        "thalita@gmail.com": 
            {
                "name": "Thalita G S",
                "role": "paciente",
                "password": "paciente2",
            },
        "admin": 
            {
                "name": "Adminintrador",
                "role": "admin",
                "password": "admin1",
            },
        }


        
    # Create user_state
    if 'user_state' not in st.session_state:
        st.session_state.user_state = {
            'name': '',
            'role': '',
            'password': '',
            'logged_in': False,
        }

    if not st.session_state.user_state['logged_in']:
        # Create login form
        st.write('Please login')
        email = st.text_input('E-Mail')
        password = st.text_input('Senha', type='password')
        submit = st.button('Login')

        # Check if user is logged in
        if submit:
            
            try:
                user_ = user_dict[email]
                if user_['password'] == password:
                    st.session_state.user_state['name'] = user_['name']
                    st.session_state.user_state['role'] = user_['role']
                    st.session_state.user_state['logged_in'] = True
                    # st.write('You are logged in')
                    st.rerun()
                else:
                    st.warning('Usuário ou senha inválidos.')
            except SyntaxError:
                st.error('Usuário não encontrado.')

    elif st.session_state.user_state['logged_in']:
        st.write('Welcome to the app')
        st.write('You are logged in as:', st.session_state.user_state['name'])
        st.write('You are a:', st.session_state.user_state['role'])
        
        if st.session_state.user_state['role'] == 'admin':
            st.write('You have admin rights. Here is the database')
            st.write(user_dict)
            
        return user_['role']
