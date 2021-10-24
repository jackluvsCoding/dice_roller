import tkinter
from functools import partial
from tkinter import *
from tkinter import ttk

import dice

# GUI Setup
root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
root.title("Dice Roller 1.0.0")


def roll_dice(die: int, qty: Entry, mod: Entry):
    rolls = []
    roll_total = 0
    for i in range(int(qty.get())):
        roll_result = dice.die_roll(die)
        rolls.append(roll_result)
        roll_total += roll_result
        print(rolls)
    display_result(die, rolls, qty, mod, roll_total + int(mod.get()))


def display_result(die: int, rolls: [], qty: Entry, mod: Entry, result: int):
    listbox.insert(END, f'd{die} result:\t [{rolls} + {int(mod.get())}] = {result}')
    listbox.yview(END)
    clear_quantity(qty)
    clear_modifier(mod)


def clear_modifier(entry: Entry):
    entry.delete(0, END)
    entry.insert(0, 0)


def clear_quantity(entry: Entry):
    entry.delete(0, END)
    entry.insert(0, 1)


def clear_listbox():
    listbox.delete(0, END)


def entry_wrapper(width: int, column: int, row: int, default_insert: int):
    entry = Entry(frame, width=width, justify=CENTER)
    entry.grid(column=column, row=row)
    entry.insert(0, default_insert)
    return entry


def button_wrapper(text: str, width: int, die_type:int, qty: Entry, mod: Entry, column: int, row: int):
    button = Button(frame, text=text, width=width, command=partial(roll_dice, die_type, qty, mod))
    button.grid(column=column, row=row)
    return button


# Column Labels
Label(frame, text="Quantity").grid(column=2, row=0)
Label(frame, text="Modifier").grid(column=3, row=0)


# die_4
Label(frame, text="D4:").grid(column=0, row=1)
d4_quantity = entry_wrapper(width=4, column=2, row=1, default_insert=1)
d4_modifier = entry_wrapper(width=4, column=3, row=1, default_insert=0)
d4_button = button_wrapper('roll d4', width=5, die_type=4, qty=d4_quantity, mod=d4_modifier, column=1, row=1)

# die_6
Label(frame, text="D6:").grid(column=0, row=2)
d6_quantity = entry_wrapper(width=4, column=2, row=2, default_insert=1)
d6_modifier = entry_wrapper(width=4, column=3, row=2, default_insert=0)
d6_button = button_wrapper('roll d6', width=5, die_type=6, qty=d6_quantity, mod=d6_modifier, column=1, row=2)

# die_8
Label(frame, text="D8:").grid(column=0, row=3)
d8_quantity = entry_wrapper(width=4, column=2, row=3, default_insert=1)
d8_modifier = entry_wrapper(width=4, column=3, row=3, default_insert=0)
d8_button = button_wrapper('roll d8', width=5, die_type=8, qty=d8_quantity, mod=d8_modifier, column=1, row=3)

# die_10
Label(frame, text="D10:").grid(column=0, row=4)
d10_quantity = entry_wrapper(width=4, column=2, row=4, default_insert=1)
d10_modifier = entry_wrapper(width=4, column=3, row=4, default_insert=0)
d10_button = button_wrapper('roll d10', width=5, die_type=10, qty=d10_quantity, mod=d10_modifier, column=1, row=4)

# die_12
Label(frame, text="D12:").grid(column=0, row=5)
d12_quantity = entry_wrapper(width=4, column=2, row=5, default_insert=1)
d12_modifier = entry_wrapper(width=4, column=3, row=5, default_insert=0)
d12_button = button_wrapper('roll d12', width=5, die_type=12, qty=d12_quantity, mod=d12_modifier, column=1, row=5)

# die_20
Label(frame, text="D20:").grid(column=0, row=6)
d20_quantity = entry_wrapper(width=4, column=2, row=6, default_insert=1)
d20_modifier = entry_wrapper(width=4, column=3, row=6, default_insert=0)
d20_button = button_wrapper('roll d20', width=5, die_type=20, qty=d20_quantity, mod=d20_modifier, column=1, row=6)

# die_100
Label(frame, text="D100:").grid(column=0, row=7)
d100_quantity = entry_wrapper(width=4, column=2, row=7, default_insert=1)
d100_modifier = entry_wrapper(width=4, column=3, row=7, default_insert=0)
d100_button = button_wrapper('roll d100', width=5, die_type=100, qty=d100_quantity, mod=d100_modifier, column=1, row=7)

# ListBox for Output
listbox = tkinter.Listbox(frame, width=25, height=4)
listbox.grid(column=1, columnspan=5, padx=0, pady=10, row=8, sticky="nsew")
clear_button = tkinter.Button(frame, text="clear", command=partial(clear_listbox), height=4)
clear_button.grid(column=0, row=8)

# Exit
exit_button = tkinter.Button(frame, text="Quit", command=root.destroy)
exit_button.grid(column=3, row=10, padx=10, pady=10)


root.mainloop()

