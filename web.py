import streamlit as st

import functions

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app will help you to boost your productivity. "
         "You can monitor yourself.")

todos = functions.read_todos()
st.subheader("Here is your todos for today..")
for todo in todos:
    st.checkbox(todo)

new_todo = st.text_input(label="", placeholder="Add a new todo...")