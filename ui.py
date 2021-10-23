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


def roll_dice(die: int, mod: Entry):
    roll_result = dice.die_roll(die)
    display_result(die, roll_result, mod, roll_result + int(mod.get()))


def display_result(die: int, roll_result: int, mod: Entry, result: int):
    listbox.delete(0, END)
    listbox.insert(END, f'd{die} result:\t [{roll_result} + {int(mod.get())}] = {result}')
    clear_modifier(mod)


def clear_modifier(entry: Entry):
    entry.delete(0, END)
    entry.insert(0, 0)


# Column Labels
Label(frame, text="Quantity").grid(column=2, row=0)
Label(frame, text="Modifier").grid(column=3, row=0)


# die_4
Label(frame, text="D4: ").grid(column=0, row=1)
d4_quantity = Entry(frame, width=4, justify=CENTER)
d4_quantity.grid(column=2, row=1)
d4_quantity.insert(0, 0)

d4_modifier = Entry(frame, width=4, justify=CENTER)
d4_modifier.grid(column=3, row=1)
d4_modifier.insert(0, 0)
d4 = tkinter.Button(frame, text="roll d4", width=5, command=partial(roll_dice, 4, d4_modifier))
d4.grid(column=1, row=1)

# die_6
Label(frame, text="D6: ").grid(column=0, row=2)
d6_quantity = Entry(frame, width=4, justify=CENTER)
d6_quantity.grid(column=2, row=2)
d6_quantity.insert(0, 0)

d6_modifier = Entry(frame, width=4, justify=CENTER)
d6_modifier.grid(column=3, row=2)
d6_modifier.insert(0, 0)
d6 = tkinter.Button(frame, text="roll d6", width=5, command=partial(roll_dice, 6, d6_modifier))
d6.grid(column=1, row=2)

# die_8
Label(frame, text="D8: ").grid(column=0, row=3)
d8_quantity = Entry(frame, width=4, justify=CENTER)
d8_quantity.grid(column=2, row=3)
d8_quantity.insert(0, 0)

d8_modifier = Entry(frame, width=4, justify=CENTER)
d8_modifier.grid(column=3, row=3)
d8_modifier.insert(0, 0)
d8 = tkinter.Button(frame, text="roll d8", width=5, command=partial(roll_dice, 8, d8_modifier))
d8.grid(column=1, row=3)

# die_10
Label(frame, text="D10: ").grid(column=0, row=4)
d10_quantity = Entry(frame, width=4, justify=CENTER)
d10_quantity.grid(column=2, row=4)
d10_quantity.insert(0, 0)

d10_modifier = Entry(frame, width=4, justify=CENTER)
d10_modifier.grid(column=3, row=4)
d10_modifier.insert(0, 0)
d10 = tkinter.Button(frame, text="roll d10", width=5, command=partial(roll_dice, 10, d10_modifier))
d10.grid(column=1, row=4)

# die_12
Label(frame, text="D12: ").grid(column=0, row=5)
d12_quantity = Entry(frame, width=4, justify=CENTER)
d12_quantity.grid(column=2, row=5)
d12_quantity.insert(0, 0)

d12_modifier = Entry(frame, width=4, justify=CENTER)
d12_modifier.grid(column=3, row=5)
d12_modifier.insert(0, 0)
d12 = tkinter.Button(frame, text="roll d12", width=5, command=partial(roll_dice, 12, d12_modifier))
d12.grid(column=1, row=5)

# die_20
Label(frame, text="D20: ").grid(column=0, row=6)
d20_quantity = Entry(frame, width=4, justify=CENTER)
d20_quantity.grid(column=2, row=6)
d20_quantity.insert(0, 0)

d20_modifier = Entry(frame, width=4, justify=CENTER)
d20_modifier.grid(column=3, row=6)
d20_modifier.insert(0, 0)
d20 = tkinter.Button(frame, text="roll d20", width=5, command=partial(roll_dice, 20, d20_modifier))
d20.grid(column=1, row=6)

# ListBox for Output
listbox = tkinter.Listbox(frame, width=25, height=4)
listbox.grid(column=1, columnspan=5, padx=10, pady=10, row=7)

# Exit
exit_button = tkinter.Button(frame, text="Quit", command=root.destroy)
exit_button.grid(column=3, row=10, padx=10, pady=10)


root.mainloop()

