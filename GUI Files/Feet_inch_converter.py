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

window = sg.Window("Convertor", layout=[[label1, text_box1],
                                        [label2, text_box2],
                                       [convert_button, output, close]])
while True:
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


window.close()

