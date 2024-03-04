import streamlit as st
import pandas as pd
from auth import read_users, excel_file, sheet_name

def update_balance(email, amount):
    users = read_users()
    user_index = users[users['Email'] == email].index[0]
    users.loc[user_index, 'Balance'] += amount
    with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        users.to_excel(writer, index=False, sheet_name=sheet_name)
    st.success(f"Added ${amount} to your wallet.")

def show_balance_page():
    st.title("Wallet Balance")
    if 'email' in st.session_state:
        users = read_users()
        user_data = users[users['Email'] == st.session_state['email']].iloc[0]
        st.write(f"Current Balance: ${user_data['Balance']}")
        amount = st.number_input("Amount to Add", min_value=0.00, max_value=10000.00, value=0.00, step=10.00)
        if st.button("Add Money"):
            update_balance(st.session_state['email'], amount)
    else:
        st.error("You are not logged in.")
