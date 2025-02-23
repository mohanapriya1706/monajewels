# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from your React frontend (adjust the origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample product data
products = [
    {"id": 1, "name": "Product A", "price": 29.99, "image": "https://via.placeholder.com/150", "category": "Clothing"},
    {"id": 2, "name": "Product B", "price": 39.99, "image": "https://via.placeholder.com/150", "category": "Accessories"},
    {"id": 3, "name": "Product C", "price": 19.99, "image": "https://via.placeholder.com/150", "category": "Clothing"}
]

@app.get("/api/products")
def get_products():
    return products

@app.post("/api/orders")
def create_order(order: dict):
    # Process or save the order details here.
    return {"status": "success", "order": order}
