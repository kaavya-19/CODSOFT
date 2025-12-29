# CodSoft Python Internship Task
# Task Name: Contact Management System (Streamlit App)
# Author: Kaavya B M

import streamlit as st

# Initialize contacts list in session state
if "contacts" not in st.session_state:
    st.session_state.contacts = []

st.title("📇 Contact Management System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Contact", "View Contacts", "Search Contact", "Update Contact", "Delete Contact"]
)

# ---------------- ADD CONTACT ----------------
if menu == "Add Contact":
    st.subheader("➕ Add New Contact")

    name = st.text_input("Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")
    address = st.text_area("Address")

    if st.button("Add Contact"):
        if name and phone:
            st.session_state.contacts.append({
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            })
            st.success("Contact added successfully!")
        else:
            st.warning("Name and Phone Number are required")

# ---------------- VIEW CONTACTS ----------------
elif menu == "View Contacts":
    st.subheader("📋 Contact List")

    if not st.session_state.contacts:
        st.info("No contacts found.")
    else:
        for i, contact in enumerate(st.session_state.contacts, start=1):
            st.write(f"**{i}. {contact['name']}**")
            st.write(f"📞 {contact['phone']}")
            st.write(f"📧 {contact['email']}")
            st.write(f"🏠 {contact['address']}")
            st.divider()

# ---------------- SEARCH CONTACT ----------------
elif menu == "Search Contact":
    st.subheader("🔍 Search Contact")

    search_key = st.text_input("Enter name or phone number")

    if st.button("Search"):
        found = False
        for contact in st.session_state.contacts:
            if search_key.lower() in contact["name"].lower() or search_key in contact["phone"]:
                st.success("Contact Found")
                st.write(f"**Name:** {contact['name']}")
                st.write(f"**Phone:** {contact['phone']}")
                st.write(f"**Email:** {contact['email']}")
                st.write(f"**Address:** {contact['address']}")
                found = True
        if not found:
            st.error("No matching contact found")

# ---------------- UPDATE CONTACT ----------------
elif menu == "Update Contact":
    st.subheader("✏️ Update Contact")

    if not st.session_state.contacts:
        st.info("No contacts available")
    else:
        names = [c["name"] for c in st.session_state.contacts]
        selected = st.selectbox("Select Contact", names)

        contact = next(c for c in st.session_state.contacts if c["name"] == selected)

        new_name = st.text_input("Name", contact["name"])
        new_phone = st.text_input("Phone", contact["phone"])
        new_email = st.text_input("Email", contact["email"])
        new_address = st.text_area("Address", contact["address"])

        if st.button("Update"):
            contact.update({
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            })
            st.success("Contact updated successfully!")

# ---------------- DELETE CONTACT ----------------
elif menu == "Delete Contact":
    st.subheader("🗑️ Delete Contact")

    if not st.session_state.contacts:
        st.info("No contacts available")
    else:
        names = [c["name"] for c in st.session_state.contacts]
        selected = st.selectbox("Select Contact to Delete", names)

        if st.button("Delete"):
            st.session_state.contacts = [
                c for c in st.session_state.contacts if c["name"] != selected
            ]
            st.success("Contact deleted successfully!")
