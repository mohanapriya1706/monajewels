import streamlit as st

# Initialize session state for cart if it doesn't exist
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Sample product list
products = [
    {
        'id': 1,
        'name': 'Product A',
        'price': 29.99,
        'image': 'https://via.placeholder.com/150'
    },
    {
        'id': 2,
        'name': 'Product B',
        'price': 39.99,
        'image': 'https://via.placeholder.com/150'
    },
    {
        'id': 3,
        'name': 'Product C',
        'price': 19.99,
        'image': 'https://via.placeholder.com/150'
    }
]

st.title("My eCommerce Store")

# Display products with "Add to Cart" buttons
st.header("Products")
for product in products:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(product['image'], width=100)
    with col2:
        st.subheader(product['name'])
        st.write(f"Price: ${product['price']}")
        # Use a unique key for each button using product id
        if st.button("Add to Cart", key=product['id']):
            st.session_state.cart.append(product)
            st.success(f"Added {product['name']} to cart!")

# Show cart details
st.header("Your Cart")
if st.session_state.cart:
    total = 0
    for item in st.session_state.cart:
        st.write(f"{item['name']} - ${item['price']}")
        total += item['price']
    st.write(f"**Total:** ${total:.2f}")
else:
    st.write("Your cart is empty.")

# Checkout section
st.header("Checkout")

# Input for WhatsApp number (optional)
whatsapp_number = st.text_input("Enter your WhatsApp Number (optional):")

# When the order is submitted
if st.button("Submit Order"):
    if not st.session_state.cart:
        st.error("Your cart is empty!")
    else:
        # Capture the order details as structured data
        order_details = {
            "cart": st.session_state.cart,
            "total": total,
            "whatsapp_number": whatsapp_number
        }
        st.success("Order Submitted!")
        st.json(order_details)

        # Generate WhatsApp link:
        # If the user provided their number, use it; otherwise, use your contact number.
        base_url = "https://wa.me/"
        if whatsapp_number:
            whatsapp_link = f"{base_url}{whatsapp_number}"
        else:
            # Replace 'YOUR_NUMBER' with your actual WhatsApp number in international format (no '+' or dashes)
            whatsapp_link = f"{base_url}YOUR_NUMBER"
        st.markdown(f"[Contact us on WhatsApp]({whatsapp_link})")
