import functions
import time
import PySimpleGUI as sg
import os

"""This will help to create todoo file if it
    does not exist"""

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkPurple4")
my_clock = sg.Text(key="clock")

label = sg.Text("Type a to-do")
input_box = sg.InputText(tooltip="Enter to-do here", key="todo")

add_button = sg.Button("Add", size=8)
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit", key="exit")

list_box = sg.Listbox(enable_events=True, size=(45, 10),
                      values=functions.read_todos(), key="todo_list")

# Each row is a list in window

window = sg.Window("My First todo app",
                   layout=[[my_clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 16))
while True:
    event, values = window.read(timeout=300)
    window["clock"].update(time.strftime("%a, %d %b %Y %H:%M:%S"))

    match event:
        case "Add":
            todos_list = functions.read_todos()
            todos_list.append(values["todo"] + "\n")
            functions.write_todos(todos_list)
            window["todo_list"].update(values=todos_list)

        case "Edit":
            try:
                # values["todo_list"] = [i.strip() for i in values["todo_list"]]
                todo_to_edit = values["todo_list"][0].strip()
                new_todos = values["todo"] + "\n"

                old_todos = functions.read_todos()
                index = old_todos.index(todo_to_edit + "\n")
                old_todos[index] = new_todos
                functions.write_todos(old_todos)
                window["todo_list"].update(values=old_todos)
            except IndexError:
                sg.popup("Please select an item", title="Warning Message", font=("Helvetica", 16))

        case "Complete":
            try:
                todo_to_complete = values["todo_list"][0]
                todos = functions.read_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todo_list"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item", title="Warning Message", font=("Helvetica", 16))

        case "todo_list":
            window["todo"].update(value=values["todo_list"][0])
        case "exit":
            break

        case sg.WIN_CLOSED:
            break
# event, values = window.read()
# print(event)
# print(values)

# This line will be executed when we press close
window.close()
