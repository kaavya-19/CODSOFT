
# CodSoft Python Internship Task
# Task Name: Password Generator
# Author: Kaavya B M

import streamlit as st
import random
import string

def generate_password(length):
    """Generate a strong random password"""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+"

    # Ensure password contains all character types
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = lowercase + uppercase + digits + symbols

    for _ in range(length - 4):
        password_chars.append(random.choice(all_chars))

    random.shuffle(password_chars)
    return "".join(password_chars)

# ---------------- Streamlit UI ----------------

st.set_page_config(page_title="Password Generator", page_icon="🔐")

st.title("🔐 Password Generator")
st.write("Generate a strong and secure password easily")

length = st.number_input(
    "Enter desired password length (minimum 6):",
    min_value=6,
    max_value=50,
    value=8,
    step=1
)

if st.button("Generate Password"):
    password = generate_password(length)
    st.success("Password Generated Successfully!")
    st.code(password)
