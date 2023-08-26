import PySimpleGUI as sg
import other_function

label1 = sg.Text("Choose files that will be compressed")
filepath1 = sg.Input(key="src")
button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Choose files that will be compressed")
filepath2 = sg.Input(key="dest")
button2 = sg.FolderBrowse("Choose", key="folder")
compress = sg.Button("Compress")

output = sg.Text(key="output")
close = sg.Button("Close", key="close")

window = sg.Window("File Compressor",
                   layout=[[label1, filepath1, button1],
                           [label2, filepath2, button2],
                           [compress, output, close]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    other_function.make_zip(filepaths, folder)
    window["output"].update(value="Compression completed !!!")

    if event == "close":
        break

window.close()
