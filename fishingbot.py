
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from cProfile import label
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import DISABLED, Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, Scale, Label, StringVar, IntVar


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Azoth Lake - v1.6")
window.geometry("800x400")
window.configure(bg = "#1E1D22")

# ----- Change the ttk style so that ComboBoxes can be modified ----- #
style = ttk.Style()
style.theme_use('alt')

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
background_image = PhotoImage(
    file=relative_to_assets("fishingbot/background.png"))
background = canvas.create_image(
    400.0,
    200.0,
    image=background_image
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

# ----- Instructions - Image ----- #
instructions_image = PhotoImage(
    file=relative_to_assets("fishingbot/instructions.png"))
instructions = canvas.create_image(
    708.0,
    228.0,
    image=instructions_image
)

# ----- Instructions Heading - Image ----- #
instructions_heading_image = PhotoImage(
    file=relative_to_assets("fishingbot/instructions_heading.png"))
instructions_heading = canvas.create_image(
    709.0,
    72.0,
    image=instructions_heading_image
)

# ----- Bot Selection/Back Button - Button ----- #
# -- Define the mouse enter and leave events
def on_enter(e):
    selection_button_image = PhotoImage(file=relative_to_assets("fishingbot/selection_button-active.png"))
    selection_button.config(image=selection_button_image)
    selection_button.image = selection_button_image

def on_leave(e):
    selection_button_image = PhotoImage(file=relative_to_assets("fishingbot/selection_button.png"))
    selection_button.config(image=selection_button_image)
    selection_button.image = selection_button_image

# -- Create the button
selection_button_image = PhotoImage(
    file=relative_to_assets("fishingbot/selection_button.png"))
selection_button = Button(
    image=selection_button_image,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Bot Selection clicked"),
    relief="flat"
)

# -- Place the button
selection_button.place(
    x=473.0,
    y=336.0,
    width=135.0,
    height=32.0
)

# -- Bind the enter + leave events
selection_button.bind("<Enter>", on_enter)
selection_button.bind("<Leave>", on_leave)

# ----- Start Bot Button - Button ----- #
# -- Define the mouse enter and leave events
def on_enter(e):
    start_button_image = PhotoImage(file=relative_to_assets("fishingbot/start_button-active.png"))
    start_button.config(image=start_button_image)
    start_button.image = start_button_image

def on_leave(e):
    start_button_image = PhotoImage(file=relative_to_assets("fishingbot/start_button.png"))
    start_button.config(image=start_button_image)
    start_button.image = start_button_image

# -- Create the button
start_button_image = PhotoImage(
    file=relative_to_assets("fishingbot/start_button.png"))
start_button = Button(
    image=start_button_image,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Start Button clicked"),
    relief="flat"
)

# -- Place the button
start_button.place(
    x=332.0,
    y=336.0,
    width=135.0,
    height=32.0
)

# -- Bind the enter + leave events
start_button.bind("<Enter>", on_enter)
start_button.bind("<Leave>", on_leave)

# ----- Update Bot Button - Button ----- #
# -- Define the mouse enter and leave events
def on_enter(e):
    update_button_image = PhotoImage(file=relative_to_assets("fishingbot/update_button-active.png"))
    update_button.config(image=update_button_image)
    update_button.image = update_button_image

def on_leave(e):
    update_button_image = PhotoImage(file=relative_to_assets("fishingbot/update_button.png"))
    update_button.config(image=update_button_image)
    update_button.image = update_button_image

# -- Create the button
update_button_image = PhotoImage(
    file=relative_to_assets("fishingbot/update_button.png"))
update_button = Button(
    image=update_button_image,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Update Button clicked"),
    relief="flat"
)

# -- Place the button
update_button.place(
    x=190.0,
    y=336.0,
    width=135.0,
    height=32.0
)

# -- Bind the enter + leave events
update_button.bind("<Enter>", on_enter)
update_button.bind("<Leave>", on_leave)

# ----- Total Fish Caught Metric - Label ----- #
Total_input_image = PhotoImage(
    file=relative_to_assets("fishingbot/metric_background.png"))
Total_input = canvas.create_image(
    550.0,
    305.5,
    image=Total_input_image
)

# --- Declare the session fish counter variable
Total_fish = IntVar()

# --- Label/Text settings and output for the Total Fish Integer Variable
Total_input = Label(
    window,
    bg="#28272E",
    highlightthickness=0,
    fg="#ccb377",
    justify='center',
    font=("Montserrat Regular", 14 * -1),
    textvariable=Total_fish
)

# --- Place the label
Total_input.place(
    x=518.0,
    y=293.0,
    width=60.0,
    height=23.0
)

# ----- Total Fish Caught Heading - Image ----- #
total_heading_image = PhotoImage(
    file=relative_to_assets("fishingbot/total_heading.png"))
total_heading = canvas.create_image(
    470.0,
    310.0,
    image=total_heading_image
)

# ----- Session Fish Caught Metric - Label ----- #
session_input_image = PhotoImage(
    file=relative_to_assets("fishingbot/metric_background.png"))
session_input = canvas.create_image(
    355.0,
    305.5,
    image=session_input_image
)

# --- Declare the session fish counter variable
session_fish = IntVar()

# --- Label/Text settings and output for the Session Fish Integer Variable
session_input = Label(
    window,
    bg="#28272E",
    highlightthickness=0,
    fg="#ccb377",
    justify='center',
    font=("Montserrat Regular", 14 * -1),
    textvariable=session_fish
)

# --- Place the label
session_input.place(
    x=323.0,
    y=293.0,
    width=60.0,
    height=23.0
)

# ----- Session Fish Caught Heading - Image ----- #
session_heading_image = PhotoImage(
    file=relative_to_assets("fishingbot/session_heading.png"))
session_heading = canvas.create_image(
    270.0,
    310.0,
    image=session_heading_image
)

# ----- Performance Heading - Image ----- #
performance_heading_image = PhotoImage(
    file=relative_to_assets("fishingbot/performance_heading.png"))
performance_heading = canvas.create_image(
    400.0,
    280.0,
    image=performance_heading_image
)

# ----- Divider - Image ----- #
divider_image = PhotoImage(
    file=relative_to_assets("fishingbot/divider.png"))
divider = canvas.create_image(
    400.0,
    260.0,
    image=divider_image
)

# ----- Logout Input - Textbox ----- #
logout_input_image = PhotoImage(
    file=relative_to_assets("fishingbot/textbox_background.png"))
logout_input = canvas.create_image(
    467.0,
    240.5,
    image=logout_input_image
)
logout_input = Entry(
    bd=0,
    bg="#28272E",
    highlightthickness=0,
    fg="#d5d5d5",
    insertbackground="#d5d5d5",
    justify='center',
    font=("Montserrat Regular", 14 * -1)
)
logout_input.place(
    x=420.0,
    y=230.0,
    width=94.0,
    height=23.0
)

# ----- Repair Key Input - Textbox ----- #
repair_key_input_image = PhotoImage(
    file=relative_to_assets("fishingbot/textbox_background.png"))
repair_key_input_bg = canvas.create_image(
    333.0,
    240.5,
    image=repair_key_input_image
)
repair_key_input = Entry(
    bd=0,
    bg="#28272E",
    highlightthickness=0,
    fg="#d5d5d5",
    insertbackground="#d5d5d5",
    justify='center',
    font=("Montserrat Regular", 14 * -1)
)
repair_key_input.place(
    x=286.0,
    y=230.0,
    width=94.0,
    height=23.0
)

# ----- Logout Heading - Image ----- #
logout_heading_image = PhotoImage(
    file=relative_to_assets("fishingbot/logout_heading.png"))
logout_heading = canvas.create_image(
    467.0,
    210.0,
    image=logout_heading_image
)

# ----- Repair Key Heading - Image ----- #
repairkey_heading_image = PhotoImage(
    file=relative_to_assets("fishingbot/repairkey_heading.png"))
repairkey_heading = canvas.create_image(
    332.0,
    210.0,
    image=repairkey_heading_image
)

# ----- AFK Input - Textbox ----- #
afk_input_image = PhotoImage(
    file=relative_to_assets("fishingbot/textbox_background.png"))
afk_input_bg = canvas.create_image(
    534.0,
    170.5,
    image=afk_input_image
)
afk_input = Entry(
    bd=0,
    bg="#28272E",
    highlightthickness=0,
    fg="#d5d5d5",
    insertbackground="#d5d5d5",
    justify='center',
    font=("Montserrat Regular", 14 * -1)
)
afk_input.place(
    x=487.0,
    y=158.0,
    width=94.0,
    height=23.0
)

# ----- AFK Heading - Image ----- #
afk_heading_image = PhotoImage(
    file=relative_to_assets("fishingbot/afk_heading.png"))
afk_heading = canvas.create_image(
    534.0,
    140.0,
    image=afk_heading_image
)

# ----- Inventory Input - Textbox ----- #
inventory_input_image = PhotoImage(
    file=relative_to_assets("fishingbot/textbox_background.png"))
inventory_input_bg = canvas.create_image(
    400.0,
    170.5,
    image=inventory_input_image
)
inventory_input = Entry(
    bd=0,
    bg="#28272E",
    highlightthickness=0,
    fg="#d5d5d5",
    insertbackground="#d5d5d5",
    justify='center',
    font=("Montserrat Regular", 14 * -1)
)
inventory_input.place(
    x=353.0,
    y=158.0,
    width=94.0,
    height=23.0
)

# ----- Inventory Heading - Image ----- #
inventory_heading_image = PhotoImage(
    file=relative_to_assets("fishingbot/inventory_heading.png"))
inventory_heading = canvas.create_image(
    399.0,
    140.0,
    image=inventory_heading_image
)

# ----- Repair Input - Textbox ----- #
repair_input_image = PhotoImage(
    file=relative_to_assets("fishingbot/textbox_background.png"))
repair_input_bg = canvas.create_image(
    266.0,
    170.5,
    image=repair_input_image
)
repair_input = Entry(
    bd=0,
    bg="#28272E",
    highlightthickness=0,
    fg="#d5d5d5",
    insertbackground="#d5d5d5",
    justify='center',
    font=("Montserrat Regular", 14 * -1)
)
repair_input.place(
    x=219.0,
    y=158.0,
    width=94.0,
    height=23.0
)

# ----- Repair Heading - Image ----- #
repair_heading_image = PhotoImage(
    file=relative_to_assets("fishingbot/repair_heading.png"))
repair_heading = canvas.create_image(
    265.0,
    140.0,
    image=repair_heading_image
)

# ----- Pole Input - Textbox ----- #
pole_input_image = PhotoImage(
    file=relative_to_assets("fishingbot/textbox_background.png"))
pole_input_bg = canvas.create_image(
    534.0,
    100.5,
    image=pole_input_image
)
pole_input = Entry(
    bd=0,
    bg="#28272E",
    highlightthickness=0,
    fg="#d5d5d5",
    insertbackground="#d5d5d5",
    justify='center',
    font=("Montserrat Regular", 14 * -1)
)
pole_input.place(
    x=487.0,
    y=88.0,
    width=94.0,
    height=23.0
)

# ----- Pole Heading - Image ----- #
pole_heading_image = PhotoImage(
    file=relative_to_assets("fishingbot/pole_heading.png"))
pole_heading = canvas.create_image(
    534.0,
    72.0,
    image=pole_heading_image
)

# ----- Freecam Input - Textbox ----- #
freecam_input_image = PhotoImage(
    file=relative_to_assets("fishingbot/textbox_background.png"))
freecam_input_bg = canvas.create_image(
    400.0,
    100.5,
    image=freecam_input_image
)
freecam_input = Entry(
    bd=0,
    bg="#28272E",
    highlightthickness=0,
    fg="#d5d5d5",
    insertbackground="#d5d5d5",
    justify='center',
    font=("Montserrat Regular", 14 * -1)
)
freecam_input.place(
    x=353.0,
    y=88.0,
    width=94.0,
    height=23.0
)

# ----- Freecam Heading - Image ----- #
freecam_heading_image = PhotoImage(
    file=relative_to_assets("fishingbot/freecam_heading.png"))
freecam_heading = canvas.create_image(
    400.0,
    72.0,
    image=freecam_heading_image
)

# ----- Bait Input Background - Image ----- #
bait_input_image = PhotoImage(
    file=relative_to_assets("fishingbot/textbox_background.png"))
bait_input_bg = canvas.create_image(
    265.0,
    100.5,
    image=bait_input_image
)

# ----- Bait Input - ComboBox ----- #
# -- Define the custom styling for the bait combobox
style.map('custom.TCombobox', fieldbackground=[('readonly','#28272E')], foreground=[('readonly','#D5D5D5')], 
selectbackground=[('readonly','#28272E')], background=[('readonly','#28272E')], arrowcolor=[('readonly','#28272E')], 
arrowsize=[('readonly','-1')])

# -- List items for the bait combobox
baits = ["No Bait", "Oytser Bait", "Clam Bait", "Meat Bait", "Firefly Bait", "Woodlouse Bait", "Bread Bait", 
"Electric Eel Bait", "Snail Bait", "Fish Bait", "Glowworm Bait", "Nightcrawler Bait", "Cheese bait"]
bait_list_combo = ttk.Combobox(window, values=baits, state="readonly", font="Montserrat 10", style='custom.TCombobox', cursor="hand2")
bait_list_combo.set("Choose a bait")
bait_list_combo.place(x=209, y=89, width=110)

# ----- Bait Heading - Image ----- #
bait_heading_image = PhotoImage(
    file=relative_to_assets("fishingbot/bait_heading.png"))
bait_heading = canvas.create_image(
    265.0,
    72.0,
    image=bait_heading_image
)

# ----- Casting Power Input - Scale ----- #
cast_power_input=Scale(window, from_=10, to=0, sliderrelief='flat', highlightthickness=0, 
background='#28272E', fg='#D5D5D5', troughcolor='#68676C', activebackground='#D5D5D5', font="Montserrat 10", 
cursor="hand2")
cast_power_input.place(x=130, y=85, width=38, height=280)

# ----- Casting Power Example - Image ----- #
casting_power_image = PhotoImage(
    file=relative_to_assets("fishingbot/casting_power.png"))
casting_power = canvas.create_image(
    58.0,
    228.0,
    image=casting_power_image
)

# ----- Casting Power Heading - Image ----- #
casting_heading_image = PhotoImage(
    file=relative_to_assets("fishingbot/casting_heading.png"))
casting_heading = canvas.create_image(
    83.0,
    75.0,
    image=casting_heading_image
)

# ----- Main Heading - Image ----- #
main_heading_image = PhotoImage(
    file=relative_to_assets("fishingbot/main_heading.png"))
main_heading = canvas.create_image(
    400.0,
    32.0,
    image=main_heading_image
)

window.resizable(False, False)
window.mainloop()