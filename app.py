import streamlit as st
from auth import show_auth_page
from ordering import show_ordering_page
from generate_bill import show_bill_page
from check_balance import show_balance_page

def main():
    if 'page' not in st.session_state:
        st.session_state['page'] = 'auth'
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False
    if 'cart' not in st.session_state:
        st.session_state['cart'] = {}

    if st.session_state['page'] == 'auth' and not st.session_state['authenticated']:
        show_auth_page()
    elif st.session_state['page'] == 'ordering':
        show_ordering_page()
    elif st.session_state['page'] == 'generate_bill':
        show_bill_page()
    elif st.session_state['page'] == 'check_balance':
        show_balance_page()

if __name__ == "__main__":
    main()
