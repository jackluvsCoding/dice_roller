from functools import partial
from tkinter import *
from tkinter import ttk

import dice

# GUI Setup
root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
root.title("Dice Roller 1.0.0")


# Column Labels
Label(frame, text="Quantity").grid(column=2, row=0)
Label(frame, text="Modifier").grid(column=3, row=0)


# Dice
Label(frame, text="D4: ").grid(column=0, row=1)
Button(frame, text="roll d4", command=partial(dice.die_roll, 4, 0)).grid(column=1, row=1)
d4_entry = Entry(frame, width=4, justify=CENTER).grid(column=3, row=1)

Label(frame, text="D6: ").grid(column=0, row=2)
Button(frame, text="roll d6", command=partial(dice.die_roll, 6, 0)).grid(column=1, row=2)

Label(frame, text="D8: ").grid(column=0, row=3)
Button(frame, text="roll d8", command=partial(dice.die_roll, 8, 0)).grid(column=1, row=3)

Label(frame, text="D10: ").grid(column=0, row=4)
Button(frame, text="roll d10", command=partial(dice.die_roll, 10, 0)).grid(column=1, row=4)

Label(frame, text="D12: ").grid(column=0, row=5)
Button(frame, text="roll d12", command=partial(dice.die_roll, 12, 0)).grid(column=1, row=5)

Label(frame, text="D20: ").grid(column=0, row=6)
Button(frame, text="roll d20", command=partial(dice.die_roll, 20, 0)).grid(column=1, row=6)


# Exit
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=3, row=10)


root.mainloop()

