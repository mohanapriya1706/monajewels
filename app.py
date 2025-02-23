import streamlit as st

# Configure the page
st.set_page_config(
    page_title="My Custom eCommerce Store",
    page_icon="🛒",
    layout="wide"
)

# Initialize session state for cart if it doesn't exist
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Sample product list with a category field
products = [
    {
        "id": 1,
        "name": "Product A",
        "price": 29.99,
        "image": "https://via.placeholder.com/150",
        "category": "Clothing"
    },
    {
        "id": 2,
        "name": "Product B",
        "price": 39.99,
        "image": "https://via.placeholder.com/150",
        "category": "Accessories"
    },
    {
        "id": 3,
        "name": "Product C",
        "price": 19.99,
        "image": "https://via.placeholder.com/150",
        "category": "Clothing"
    }
]

# Sidebar: Filtering options
st.sidebar.header("Filter Products")
category_options = list(set(product["category"] for product in products))
selected_category = st.sidebar.selectbox("Select Category", ["All"] + category_options)

# Custom CSS for styling product cards
st.markdown(
    """
    <style>
    .product-card {
        background-color: #f9f9f9;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Main title
st.title("My Custom eCommerce Store")

# Filter products based on the selected category
if selected_category != "All":
    filtered_products = [p for p in products if p["category"] == selected_category]
else:
    filtered_products = products

# Display products
st.header("Products")
for product in filtered_products:
    with st.container():
        cols = st.columns([1, 2])
        with cols[0]:
            st.image(product["image"], width=120)
        with cols[1]:
            st.markdown("<div class='product-card'>", unsafe_allow_html=True)
            st.subheader(product["name"])
            st.write(f"Price: ${product['price']}")
            if st.button("Add to Cart", key=f"add_{product['id']}"):
                st.session_state.cart.append(product)
                st.success(f"Added {product['name']} to cart!")
            st.markdown("</div>", unsafe_allow_html=True)

# Display Cart
st.header("Your Cart")
if st.session_state.cart:
    total = sum(item["price"] for item in st.session_state.cart)
    for item in st.session_state.cart:
        st.write(f"{item['name']} - ${item['price']}")
    st.write(f"**Total:** ${total:.2f}")
else:
    st.write("Your cart is empty.")

# Checkout Section
st.header("Checkout")
whatsapp_number = st.text_input("Enter your WhatsApp Number (optional):")

if st.button("Submit Order"):
    if not st.session_state.cart:
        st.error("Your cart is empty!")
    else:
        order_details = {
            "cart": st.session_state.cart,
            "total": total,
            "whatsapp_number": whatsapp_number
        }
        st.success("Order Submitted!")
        st.json(order_details)

        # Generate WhatsApp link:
        base_url = "https://wa.me/"
        if whatsapp_number:
            whatsapp_link = f"{base_url}{whatsapp_number}"
        else:
            # Replace 'YOUR_NUMBER' with your actual WhatsApp number (in international format, no '+' or dashes)
            whatsapp_link = f"{base_url}YOUR_NUMBER"
        st.markdown(f"[Contact us on WhatsApp]({whatsapp_link})")
