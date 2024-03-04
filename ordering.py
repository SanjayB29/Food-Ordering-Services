import streamlit as st

# Sample menu data with image placeholders
menu_items = [
    {"name": "Cheeseburger", "price": 8, "image": "images/cb.jpeg"},
    {"name": "Veggie Burger", "price": 9, "image": "images/vb.jpeg"},
    {"name": "Chicken Nuggets", "price": 5, "image": "images/cn.jpeg"},
    {"name": "Large Fries", "price": 4, "image": "images/lf.jpeg"},
    {"name": "Soft Drink", "price": 2, "image": "images/sd.jpeg"},
    {"name": "Milkshake", "price": 3, "image": "images/ms.jpeg"},
]

def show_ordering_page():
    st.title("Fast Food Ordering Page")
    st.write("Welcome to our Fast Food Ordering System!")

    for item in menu_items:
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            st.image(item["image"], width=100, caption=item["name"])
        
        with col2:
            st.write(f"Price: ${item['price']}")
        
        with col3:
            qty_key = f"qty_{item['name']}"
            if qty_key not in st.session_state:
                st.session_state[qty_key] = 1
            quantity = st.number_input("Quantity", min_value=1, value=st.session_state[qty_key], key=qty_key)
            if st.button("Add", key=f"btn_{item['name']}"):
                if item['name'] in st.session_state['cart']:
                    st.session_state['cart'][item['name']]['quantity'] += quantity
                else:
                    st.session_state['cart'][item['name']] = {'price': item['price'], 'quantity': quantity}
                st.success(f"Added {quantity} x {item['name']} to your cart.")

    if st.button('Proceed to Bill Generation'):
        st.session_state['page'] = 'generate_bill'
    if st.button('Check Wallet Balance'):
        st.session_state['page'] = 'check_balance'

    st.write("Cart:", st.session_state['cart'])
