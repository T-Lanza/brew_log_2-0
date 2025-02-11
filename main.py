import tkinter as tk
from tkinter import ttk
import json
from get_date import get_date
from scrollframe import ScrollableFrame
from search import *

version = "2.0.1"

# Initialize the Recipe Log
PATH = "DATA/recipes.json"

with open(PATH, 'r') as file:
    recipes = json.load(file)

# Functions 
def nada():
    pass

# Build Main GUI body
root = tk.Tk()
root.title(f"Oliver Noodle Brew Log | {get_date()}")
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")

# Build Menu 
menu_bar = tk.Menu(root, tearoff=False)

file_menu = tk.Menu(menu_bar, tearoff=False)
file_menu.add_command(label="New", command=lambda: nada())
file_menu.add_command(label="Edit", command=lambda: nada())
file_menu.add_command(label=("Search"), command=lambda: nada())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="   File   ", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=False)
edit_menu.add_command(label="Edit Recipe", command=nada)
edit_menu.add_command(label="Edit Background", command=nada)
menu_bar.add_cascade(label="   Edit   ", menu=edit_menu)

about_menu = tk.Menu(menu_bar, tearoff=False)
about_menu.add_command(label=f"  BrewLog Version {version}  | 2025")
menu_bar.add_cascade(label="   About  ", menu=about_menu)

menu_bar.add_command(label="   Help   ", command=nada)
menu_bar.add_separator()

# Search Bar
menu_bar.add_command(label="  Search  ", command=nada)

# Main Display
main_label = tk.Label(root, text="Oliver Noodle Brew Logs: ")
main_label.config(font=("Helvetica", 36))
main_label.place(x=25, y=25)

main_display = ScrollableFrame(root)
main_display.config(width=350, height=200)
main_display.place(x=25, y=75)

# Main Loop
root.config(menu=menu_bar)
root.mainloop()