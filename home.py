import streamlit as st
import functions


todos = functions.read_todos()


def add_todo():
    input_todo = st.session_state["new_todo"] + "\n"
    todos.append(input_todo.title())
    functions.write_todos(todos)


st.set_page_config(layout="wide")
st.title("Todo App")
st.subheader("This my todo app.")
st.write("This app to increase my <b>productivity</b>", unsafe_allow_html=True)


st.text_input(label="",
              placeholder="Add new todo...",
              key="new_todo",
              on_change=add_todo)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

