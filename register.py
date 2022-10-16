
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


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
    file=relative_to_assets("register/image_1.png"))
image_1 = canvas.create_image(
    400.0,
    200.0,
    image=image_image_1
)

# ----- Back Button - Button ----- #
# -- Define the mouse enter and leave events
def on_enter(e):
    back_button_image = PhotoImage(file=relative_to_assets("register/back_button-active.png"))
    back_button.config(image=back_button_image)
    back_button.image = back_button_image

def on_leave(e):
    back_button_image = PhotoImage(file=relative_to_assets("register/back_button.png"))
    back_button.config(image=back_button_image)
    back_button.image = back_button_image

# -- Create the button
back_button_image = PhotoImage(
    file=relative_to_assets("register/back_button.png"))
back_button = Button(
    image=back_button_image,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Back Button clicked"),
    relief="flat"
)

# -- Place the button
back_button.place(
    x=403.0,
    y=355.0,
    width=105.0,
    height=32.0
)

# -- Bind the enter + leave events
back_button.bind("<Enter>", on_enter)
back_button.bind("<Leave>", on_leave)

# ----- Back Button - Button ----- #
# -- Define the mouse enter and leave events
def on_enter(e):
    register_button_image = PhotoImage(file=relative_to_assets("register/register_button-active.png"))
    register_button.config(image=register_button_image)
    register_button.image = register_button_image

def on_leave(e):
    register_button_image = PhotoImage(file=relative_to_assets("register/register_button.png"))
    register_button.config(image=register_button_image)
    register_button.image = register_button_image

# -- Create the button
register_button_image = PhotoImage(
    file=relative_to_assets("register/register_button.png"))
register_button = Button(
    image=register_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Register Button clicked"),
    relief="flat"
)

# -- Place the button
register_button.place(
    x=293.0,
    y=355.0,
    width=105.0,
    height=32.0
)

# -- Bind the enter + leave events
register_button.bind("<Enter>", on_enter)
register_button.bind("<Leave>", on_leave)

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

# ----- Username - TextBox ----- #
username_input_image = PhotoImage(
    file=relative_to_assets("register/username_input.png"))
username_input_bg = canvas.create_image(
    275.5,
    140.0,
    image=username_input_image
)
username_input = Entry(
    bd=0,
    bg="#28272E",
    highlightthickness=0,
    fg="#d5d5d5",
    insertbackground="#d5d5d5",
    justify='center',
    font=("Montserrat Regular", 14 * -1)
)
username_input.place(
    x=173.0,
    y=124.0,
    width=205.0,
    height=30.0
)

# ----- Password - TextBox ----- #
password_input_image = PhotoImage(
    file=relative_to_assets("register/password_input.png"))
password_input_bg = canvas.create_image(
    527.5,
    140.0,
    image=password_input_image
)
password_input = Entry(
    bd=0,
    bg="#28272E",
    highlightthickness=0,
    fg="#d5d5d5",
    insertbackground="#d5d5d5",
    justify='center',
    font=("Montserrat Regular", 14 * -1),
    show="*"
)
password_input.place(
    x=425.0,
    y=124.0,
    width=205.0,
    height=30.0
)

# ----- First Name - TextBox ----- #
firstname_input_image = PhotoImage(
    file=relative_to_assets("register/firstname_input.png"))
firstname_input_bg = canvas.create_image(
    274.5,
    225.0,
    image=firstname_input_image
)
firstname_input = Entry(
    bd=0,
    bg="#28272E",
    highlightthickness=0,
    fg="#d5d5d5",
    insertbackground="#d5d5d5",
    justify='center',
    font=("Montserrat Regular", 14 * -1)
)
firstname_input.place(
    x=172.0,
    y=209.0,
    width=205.0,
    height=30.0
)

# ----- Last Name - TextBox ----- #
lastname_input_image = PhotoImage(
    file=relative_to_assets("register/lastname_input.png"))
lastname_input_bg = canvas.create_image(
    526.5,
    225.0,
    image=lastname_input_image
)
lastname_input = Entry(
    bd=0,
    bg="#28272E",
    highlightthickness=0,
    fg="#d5d5d5",
    insertbackground="#d5d5d5",
    justify='center',
    font=("Montserrat Regular", 14 * -1)
)
lastname_input.place(
    x=424.0,
    y=209.0,
    width=205.0,
    height=30.0
)

# ----- E-mail - TextBox ----- #
email_input_image = PhotoImage(
    file=relative_to_assets("register/email_input.png"))
email_input_bg = canvas.create_image(
    399.5,
    308.0,
    image=email_input_image
)
email_input = Entry(
    bd=0,
    bg="#28272E",
    highlightthickness=0,
    fg="#d5d5d5",
    insertbackground="#d5d5d5",
    justify='center',
    font=("Montserrat Regular", 14 * -1)
)
email_input.place(
    x=297.0,
    y=292.0,
    width=205.0,
    height=30.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("register/image_2.png"))
image_2 = canvas.create_image(
    398.0,
    56.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("register/image_3.png"))
image_3 = canvas.create_image(
    274.0,
    109.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("register/image_4.png"))
image_4 = canvas.create_image(
    527.0,
    109.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("register/image_5.png"))
image_5 = canvas.create_image(
    527.0,
    193.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("register/image_6.png"))
image_6 = canvas.create_image(
    403.0,
    276.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("register/image_7.png"))
image_7 = canvas.create_image(
    275.0,
    193.0,
    image=image_image_7
)
window.resizable(False, False)
window.mainloop()
