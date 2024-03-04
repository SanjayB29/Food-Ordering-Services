import streamlit as st
from fpdf import FPDF
import pandas as pd
from auth import read_users, excel_file, sheet_name

def generate_bill_pdf(bill_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Bill Details", ln=True, align='C')
    for item, details in bill_data.items():
        subtotal = details['price'] * details['quantity']
        pdf.cell(200, 10, txt=f"{item}: {details['quantity']} x ${details['price']} = ${subtotal}", ln=True)
    total_cost = sum(details['price'] * details['quantity'] for details in bill_data.values())
    pdf.cell(200, 10, txt=f"Total: ${total_cost}", ln=True, align='C')
    pdf_file_path = 'bill.pdf'
    pdf.output(pdf_file_path)
    return pdf_file_path, total_cost

def attempt_payment(email, total_cost):
    users = read_users()
    user_index = users[users['Email'] == email].index[0]
    if users.loc[user_index, 'Balance'] >= total_cost:
        users.loc[user_index, 'Balance'] -= total_cost
        with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            users.to_excel(writer, index=False, sheet_name=sheet_name)
        return True, "Payment successful."
    else:
        return False, "Insufficient funds."

def show_bill_page():
    st.title("Bill Details")
    if 'cart' in st.session_state and st.session_state['cart']:
        bill_data = {item: {'price': details['price'], 'quantity': details['quantity'], 'subtotal': details['price'] * details['quantity']} for item, details in st.session_state['cart'].items()}
        bill_pdf_path, total_cost = generate_bill_pdf(bill_data)
        with open(bill_pdf_path, "rb") as pdf_file:
            st.download_button("Download Bill as PDF", data=pdf_file, file_name="bill.pdf")
        st.write(f"Total Cost: ${total_cost}")
        if st.button('Pay Now'):
            success, message = attempt_payment(st.session_state['email'], total_cost)
            if success:
                st.success(message)
                st.session_state['cart'] = {}
            else:
                st.error(message)
    else:
        st.write("Your cart is empty.")
