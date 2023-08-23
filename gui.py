import functions
import PySimpleGUI as sg

label = sg.Text("Type a to-do")
input_box = sg.InputText(tooltip="Enter to-do here", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(enable_events=True, size=(45, 5), values=functions.read_todos(), key="todo_list")

# Each row is a list in window

window = sg.Window("My First todo app",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos_list = functions.read_todos()
            todos_list.append(values["todo"] + "\n")
            functions.write_todos(todos_list)
            window["todo_list"].update(values=todos_list)

        case "Edit":
            # values["todo_list"] = [i.strip() for i in values["todo_list"]]
            todo_to_edit = values["todo_list"][0]
            new_todos = values["todo"]

            old_todos = functions.read_todos()
            index = old_todos.index(todo_to_edit)
            old_todos[index] = new_todos
            functions.write_todos(old_todos)
            window["todo_list"].update(values=old_todos)

        case "todo_list":
            window["todo"].update(value= values["todo_list"][0])

        case sg.WIN_CLOSED:
            break
# event, values = window.read()
# print(event)
# print(values)

# This line will be executed when we press close
window.close()
