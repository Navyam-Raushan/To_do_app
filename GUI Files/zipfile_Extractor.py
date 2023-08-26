import PySimpleGUI as sg
import other_function as func

sg.theme("Black")

label1 = sg.Text("Choose a zipfile")
filepath1 = sg.Input(key="src")
button1 = sg.FileBrowse("Choose", key="zipfile")

label2 = sg.Text("Choose destination folder")
filepath2 = sg.Input(key="dest")
button2 = sg.FolderBrowse("Choose", key="folder")

extract = sg.Button("Extract")
output = sg.Text(key="output", text_color="green")
close = sg.Button("Close", key="close")

col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[filepath1], [filepath2]])
col3 = sg.Column([[button1], [button2]])


window = sg.Window("Zipfile Extractor",
                   layout=[[col1, col2, col3],
                           [extract, output, close]],
                   font=("Helvetica", 16))


while True:
    event, values = window.read()
    print(event, values)  # returning actual path of the file

    zipfilepath = values["zipfile"]
    dest_path = values["folder"]
    func.extract_zip(zipfilepath, dest_path)
    window["output"].update(value="Extracted Successfully!")

    if event == "close":
        break

window.close()
