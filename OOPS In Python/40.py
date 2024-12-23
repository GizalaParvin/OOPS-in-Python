from tkinter import Tk, colorchooser

def choose_color():
    color = colorchooser.askcolor()[1]
    print(f"Selected color: {color}")
window = Tk()
choose_color()
window.mainloop()



#Another Method

import tkinter as tk
from tkinter import colorchooser

def choose_color():
    color_code = colorchooser.askcolor(title="Choose a color")
    if color_code:
        color_label.config(text=f"Selected Color: {color_code[1]}", bg=color_code[1])

root = tk.Tk()

color_button = tk.Button(root, text="Choose Color", command=choose_color)
color_button.pack(pady=20)

color_label = tk.Label(root, text="Selected Color: None", bg="white", width=30)
color_label.pack(pady=20)

root.mainloop()



