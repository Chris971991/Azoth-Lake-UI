
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from turtle import width


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Azoth Lake - v1.6")
window.geometry("800x400")
window.configure(bg = "#1E1D22")

# ----- Window Icon ----- #
p1 = PhotoImage(file=relative_to_assets("favicon.png"))
window.iconphoto(False, p1)

# ----- Canvas Settings ----- #
canvas = Canvas(
    window,
    bg = "#1E1D22",
    height = 400,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# ----- Canvas Background ----- #
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("botselection/background.png"))
image_1 = canvas.create_image(
    400.0,
    200.0,
    image=image_image_1
)

# ----- Version + Detection Headings - Text ----- #
canvas.create_text(
    5.0,
    370.0,
    anchor="nw",
    text="Client Version - \nDetection Status -",
    fill="#D5D5D5",
    font=("Montserrat Regular", 11 * -1)
)

# ----- Version Status - Text ----- #
canvas.create_text(
    90.0,
    370.0,
    anchor="nw",
    text="Updated",
    fill="#24FF00",
    font=("Montserrat Regular", 11 * -1)
)

# ----- Detection Status - Text ----- #
canvas.create_text(
    105.0,
    385.0,
    anchor="nw",
    text="Undetected",
    fill="#24FF00",
    font=("Montserrat Regular", 11 * -1)
)

# ----- Discord Details - Text ----- #
canvas.create_text(
    715.0,
    370.0,
    anchor="ne",
    text="Discord User - \nDiscord Server - ",
    fill="#D5D5D5",
    font=("Montserrat Regular", 11 * -1)
)

# ----- Program Creator Discord - Text ----- #
canvas.create_text(
    795.0,
    370.0,
    anchor="ne",
    text="AzothLake#0261",
    fill="#24FF00",
    font=("Montserrat Regular", 11 * -1)
)

# ----- Discord Server Link - Text ----- #
canvas.create_text(
    795.0,
    385.0,
    anchor="ne",
    text="vwWJCFkK6a",
    fill="#24FF00",
    font=("Montserrat Regular", 11 * -1)
)

# ----- Time Remaining Heading - Text ----- #
canvas.create_text(
    323.0,
    380.0,
    anchor="nw",
    text="Time Remaining - ",
    fill="#D5D5D5",
    font=("Montserrat Regular", 11 * -1)
)

# ----- Time Remaining - Text ----- #
canvas.create_text(
    426.0,
    380.0,
    anchor="nw",
    text="365 Days",
    fill="#24FF00",
    font=("Montserrat Regular", 11 * -1)
)

# ----- Main Heading - Image ----- #
heading_image = PhotoImage(
    file=relative_to_assets("botselection/heading.png"))
heading = canvas.create_image(
    400.0,
    44.0,
    image=heading_image
)

# ----- Fishing Button - Button ----- #
# -- Define the mouse enter and leave events
def on_enter(e):
    fishing_button_image = PhotoImage(file=relative_to_assets("botselection/fishing_button_active.png"))
    fishing_button.config(image=fishing_button_image)
    fishing_button.image = fishing_button_image

def on_leave(e):
    fishing_button_image = PhotoImage(file=relative_to_assets("botselection/fishing_button.png"))
    fishing_button.config(image=fishing_button_image)
    fishing_button.image = fishing_button_image 

# -- Create the button
fishing_button_image = PhotoImage(
    file=relative_to_assets("botselection/fishing_button.png"))
fishing_button = Button(
    image=fishing_button_image,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Fishing Button clicked"),
    relief="flat"
)

# -- Place the button
fishing_button.place(
    x=70.0,
    y=124.0,
    width=175.0,
    height=175.0
)

# -- Bind the enter + leave events
fishing_button.bind("<Enter>", on_enter)
fishing_button.bind("<Leave>", on_leave)

# ----- Music Button - Button ----- #
# -- Define the mouse enter and leave events
def on_enter(e):
    music_button_image = PhotoImage(file=relative_to_assets("botselection/music_button_active.png"))
    music_button.config(image=music_button_image)
    music_button.image = music_button_image

def on_leave(e):
    music_button_image = PhotoImage(file=relative_to_assets("botselection/music_button.png"))
    music_button.config(image=music_button_image)
    music_button.image = music_button_image 

# -- Create the button
music_button_image = PhotoImage(
    file=relative_to_assets("botselection/music_button.png"))
music_button = Button(
    image=music_button_image,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Music Button clicked"),
    relief="flat"
)

# -- Place the button
music_button.place(
    x=312.0,
    y=124.0,
    width=175.0,
    height=175.0
)

# -- Bind the enter + leave events
music_button.bind("<Enter>", on_enter)
music_button.bind("<Leave>", on_leave)

# ----- Gathering Button - Button ----- #
# -- Define the mouse enter and leave events
def on_enter(e):
    gathering_button_image = PhotoImage(file=relative_to_assets("botselection/gathering_button_active.png"))
    gathering_button.config(image=gathering_button_image)
    gathering_button.image = gathering_button_image

def on_leave(e):
    gathering_button_image = PhotoImage(file=relative_to_assets("botselection/gathering_button.png"))
    gathering_button.config(image=gathering_button_image)
    gathering_button.image = gathering_button_image 

# -- Create the button
gathering_button_image = PhotoImage(
    file=relative_to_assets("botselection/gathering_button.png"))
gathering_button = Button(
    image=gathering_button_image,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Gathering Button clicked"),
    relief="flat"
)

# -- Place the button
gathering_button.place(
    x=550.0,
    y=124.0,
    width=175.0,
    height=175.0
)

# -- Bind the enter + leave events
gathering_button.bind("<Enter>", on_enter)
gathering_button.bind("<Leave>", on_leave)

# ----- Fishing Heading - Image ----- #
fishing_heading_image = PhotoImage(
    file=relative_to_assets("botselection/fishing_heading.png"))
fishing_heading = canvas.create_image(
    157.0,
    105.0,
    image=fishing_heading_image
)

# ----- Music Heading - Image ----- #
music_heading_image = PhotoImage(
    file=relative_to_assets("botselection/music_heading.png"))
music_heading = canvas.create_image(
    399.0,
    102.0,
    image=music_heading_image
)

# ----- Gathering Heading - Image ----- #
gathering_heading_image = PhotoImage(
    file=relative_to_assets("botselection/gathering_heading.png"))
gathering_heading = canvas.create_image(
    637.0,
    105.0,
    image=gathering_heading_image
)

# ----- Serial Key Input - Textbox ----- #
serial_input_image = PhotoImage(
    file=relative_to_assets("botselection/textbox_background.png"))
serial_input = canvas.create_image(
    340.0,
    333.5,
    image=serial_input_image
)
serial_input = Entry(
    bd=0,
    bg="#28272E",
    highlightthickness=0,
    fg="#d5d5d5",
    insertbackground="#d5d5d5",
    justify='center',
    font=("Montserrat Regular", 14 * -1)
)
serial_input.place(
    x=263.0,
    y=322.0,
    width=150.0,
    height=23.0
)

serial_input.insert(0, "Enter Serial Key")

# ----- Submit Serial Key - Button ----- #
# -- Define the mouse enter and leave events
def on_enter(e):
    submit_button_image = PhotoImage(file=relative_to_assets("botselection/submit_button-active.png"))
    submit_button.config(image=submit_button_image)
    submit_button.image = submit_button_image

def on_leave(e):
    submit_button_image = PhotoImage(file=relative_to_assets("botselection/submit_button.png"))
    submit_button.config(image=submit_button_image)
    submit_button.image = submit_button_image 

# -- Create the button
submit_button_image = PhotoImage(
    file=relative_to_assets("botselection/submit_button.png"))
submit_button = Button(
    image=submit_button_image,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Submit Button clicked"),
    relief="flat"
)

# -- Place the button
submit_button.place(
    x=439.0,
    y=322.0,
    width=105.0,
    height=25.0
)

# -- Bind the enter + leave events
submit_button.bind("<Enter>", on_enter)
submit_button.bind("<Leave>", on_leave)
window.resizable(False, False)
window.mainloop()
