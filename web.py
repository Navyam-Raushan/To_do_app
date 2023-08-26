import streamlit as st

import functions

todos = functions.read_todos()


def add_todos():
    # just enter key values session state contain all keys
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app will help you to boost your productivity. "
         "You can monitor yourself.")

st.subheader("Here is your todos for today..")
for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todos,
              key="new_todo")
