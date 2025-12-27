# CodSoft Python Internship Task
# Task Name: To-Do List (Streamlit App)
# Author: Kaavya B M

import streamlit as st

# Initialize session state
if "todo_list" not in st.session_state:
    st.session_state.todo_list = []

st.title("📝 To-Do List Application")

# Add Task
st.subheader("Add a New Task")
new_task = st.text_input("Enter your task")

if st.button("Add Task"):
    if new_task.strip():
        st.session_state.todo_list.append(
            {"task": new_task, "status": "Pending"}
        )
        st.success("Task added successfully!")
        st.rerun()
    else:
        st.warning("Please enter a task.")

# View Tasks
st.subheader("Your Tasks")

if not st.session_state.todo_list:
    st.info("No tasks available.")
else:
    for index, task in enumerate(st.session_state.todo_list):
        col1, col2, col3 = st.columns([4, 2, 2])

        col1.write(f"{index + 1}. {task['task']}")
        col2.write(task["status"])

        if col3.button("✔ Complete", key=f"complete_{index}"):
            st.session_state.todo_list[index]["status"] = "Completed"
            st.rerun()

# Delete Task
st.subheader("Delete a Task")

if st.session_state.todo_list:
    task_numbers = list(range(1, len(st.session_state.todo_list) + 1))
    delete_task_no = st.selectbox("Select task number", task_numbers)

    if st.button("Delete Task"):
        removed = st.session_state.todo_list.pop(delete_task_no - 1)
        st.success(f"Deleted task: {removed['task']}")
        st.rerun()
    
