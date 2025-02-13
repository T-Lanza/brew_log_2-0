import tkinter as tk
from tkinter import ttk
import json
from get_date import get_date
from scrollframe import ScrollableFrame
from search import *
from home import home
from add_recipe import add_recipe

iteration = 1

if iteration < 10:
    iter_str = f"00{iteration}"
if iteration > 9 and iteration < 100:
    iter_str = f"0{iteration}"
if iteration > 99 and iteration < 1000:
    iter_str = f"{iteration}"
if iteration > 1000:
    iteration = 1

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
file_menu.add_command(label="New", command=lambda: add_recipe(root, recipes))
file_menu.add_command(label="Edit", command=lambda: nada())
file_menu.add_command(label=("Print"), command=lambda: nada())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="   File   ", menu=file_menu)

menu_bar.add_command(label="   New    ", command=lambda: add_recipe(root, recipes))

about_menu = tk.Menu(menu_bar, tearoff=False)
about_menu.add_command(label=f"  BrewLog Version {version}  | 2025")
menu_bar.add_cascade(label="   About  ", menu=about_menu)

menu_bar.add_command(label="   Home  ", command=lambda: home(root,
                                                             main_display,
                                                             recipes,
                                                             menu_bar,
                                                             main_label))
menu_bar.add_separator()

# Search Bar
menu_bar.add_command(label="  Search  ", command=nada)

# Main Display
main_label = tk.Label(root, text="Oliver Noodle Brew Logs: ")
main_label.config(font=("Helvetica", 36))
main_label.place(x=25, y=25)

main_display = ScrollableFrame(root)
main_display.config(width=590, height=590)
main_display.place(x=25, y=90)

home(root, main_display, recipes, menu_bar, main_label)

# Test


# Main Loop
root.config(menu=menu_bar)
root.mainloop()