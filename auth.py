import streamlit as st
import pandas as pd
from openpyxl import load_workbook
from pathlib import Path

# Ensure the Excel file exists for storing user credentials
excel_file = 'user_credentials.xlsx'
sheet_name = 'Users'
Path(excel_file).touch(exist_ok=True)

def read_users():
    try:
        return pd.read_excel(excel_file, sheet_name=sheet_name)
    except Exception as e:
        return pd.DataFrame(columns=['Name', 'Email', 'Password', 'Balance'])

def write_user(name, email, password, initial_balance=50):
    users = read_users()
    new_user = pd.DataFrame([[name, email, password, initial_balance]], columns=['Name', 'Email', 'Password', 'Balance'])
    updated_users = pd.concat([users, new_user], ignore_index=True)
    with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        updated_users.to_excel(writer, index=False, sheet_name=sheet_name)

def check_login(email, password):
    users = read_users()
    if not users[(users['Email'] == email) & (users['Password'] == password)].empty:
        st.session_state['email'] = email
        return True
    else:
        return False

def show_auth_page():
    st.sidebar.title('Navigation')
    mode = st.sidebar.radio("Choose mode", ["Login", "Sign Up"])

    if mode == "Sign Up":
        st.header('Sign Up')
        name = st.text_input('Name')
        email = st.text_input('Email')
        password = st.text_input('Password', type='password')
        if st.button('Sign Up'):
            write_user(name, email, password)
            st.success('You have successfully signed up!')
            st.session_state['authenticated'] = True
            st.session_state['page'] = 'ordering'

    elif mode == "Login":
        st.header('Login')
        email = st.text_input('Email')
        password = st.text_input('Password', type='password')
        if st.button('Login'):
            if check_login(email, password):
                st.success('You have successfully logged in!')
                st.session_state['authenticated'] = True
                st.session_state['page'] = 'ordering'
            else:
                st.error('Login failed. Check your email and password.')
