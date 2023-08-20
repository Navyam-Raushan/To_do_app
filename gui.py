import functions
import PySimpleGUI as sg

label = sg.Text("Type a to-do")
input_box = sg.InputText(tooltip="Enter to-do here")
add_button = sg.Button("Add")

window = sg.Window("My First todo app", layout=[[label], [input_box, add_button]])
window.read()

# This line will be executed when we press close
window.close()
