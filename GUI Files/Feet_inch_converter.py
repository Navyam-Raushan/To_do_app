import PySimpleGUI as sg
import other_function as func

sg.theme("Black")

label1 = sg.Text("Enter feet: ", key="feet")
text_box1 = sg.InputText(key="f")

label2 = sg.Text("Enter inches: ", key="inches")
text_box2 = sg.InputText(key="i")

convert_button = sg.Button("Convert", key="convert")
output = sg.Text(key="output", text_color="Green")

close = sg.Button("Close", key="close")
col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[text_box1], [text_box2]])

window = sg.Window("Convertor", layout=[[col1, col2],
                                        [convert_button, output, close]])
while True:
    try:
        event, values = window.read()
        print(event)
        print(values)
        feet = int(values["f"])
        inches = int(values["i"])

        if event == "convert":
            res = func.feet_inch(feet, inches)
            window["output"].update(value=f"{res} m")
            print(res)
        if event == "close" or sg.WIN_CLOSED:
            break
    except ValueError:
        sg.theme("Black")
        sg.popup("Please provide two numbers", title="Warning!")


window.close()

