import PySimpleGUI as sg
from pathlib import Path

sg.theme("GrayGrayGray")
smileys = [
    "happy", [":)", "<3", ":D"],
    "sad", [":(", "T_T"],
    "other", [":3"]

]

smileys_event = smileys[1] + smileys[3] + smileys[5]

menu_layout = [
    ["File", ["Open", "save", "---", "Exit"]],
    ["Tools", ["Word Count"]],
    ["Add", smileys],
]
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text("Untitled", key="-DOCNAME-")],
    [sg.Multiline(no_scrollbar=True, size=(40, 30), key="-TEXT BOX-")]
]
window = sg.Window("Text Editor", layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "open":
        file_path = sg.popup_get_file("open", no_window=True)
        if file_path:
            file = Path(file_path)
            window["-TEXTBOX-"].update(file.read_text())
            window["-DOCNAME-"].update(file_path.split("/")[-1])

    if event == "save":
        file_path = sg.popup_get_file("save as", no_window=True, save_as=True)
        file = Path(file_path)
        file.write_text(values["-TEXTBOX-"])
        window["-DOCNAME-"].update(file_path.split("/")[-1])

    if event == "Word Count":
        full_text = values["-TEXT BOX-"]
        clean_text = full_text.replace("\n", " ").split(" ")
        word_count = len(clean_text)
        char_count = len("".join(clean_text))
        sg.popup(f"Words : {word_count}\ncharacters : {char_count}")
    if event in smileys_event:
        current_text = values["-TEXT BOX-"]
        new_text = current_text + " " + event
        window["-TEXT BOX-"].update(new_text)
window.close()
