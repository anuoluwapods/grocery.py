import streamlit as st
import streamlit.auth as auth
from deta import Deta
from datetime import datetime
import authenticate
import secrets

# Authenticate the user
authenticator = auth.HmacAuthenticator(secret_key="your_secret_key_here")
user = auth.get_verified_email(authenticator)

# Initialize Deta
deta = Deta(st.secrets["deta_key"])
db = deta.Base("grocery")

# Add grocery items
def add_item(item_name, item_price):
    item = {"name": item_name, "price": item_price}
    db.put(item)

# Get all grocery items
def get_items():
    items = list(db.fetch())
    return items

# Delete a grocery item
def delete_item(item_key):
    db.delete(item_key)

# UI elements
st.title("Grocery List App")
st.write("Welcome, " + user)

item_name = st.text_input("Enter item name:")
item_price = st.text_input("Enter item price:")

if st.button("Add Item"):
    add_item(item_name, item_price)
    st.success("Item added!")

items = get_items()

if items:
    st.write("Grocery List:")
    for item in items:
        st.write(item["name"] + " - " + item["price"])
        if st.button("Delete " + item["name"]):
            delete_item(item["key"])
            st.success("Item deleted!")
else:
    st.warning("No items in the grocery list.")
