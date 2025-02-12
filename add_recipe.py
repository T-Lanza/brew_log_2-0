import tkinter as tk
from tkinter import ttk
from get_date import get_date_num, get_date_id
import json
from constants import STYLES

with open('DATA/recipes.json', 'r') as file:
    recipes = json.load(file)

def submit():
    pass


def update_style_dropdown(event, variety_dropdown, style_dropdown):
    selected_variety = variety_dropdown.get()
    if selected_variety in STYLES:
        # Update the style dropdown with the styles for the selected variety
        style_dropdown["values"] = STYLES[selected_variety]
        style_dropdown.set("Select a style")  # Reset the style dropdown
    else:
        # Clear the style dropdown if no valid variety is selected
        style_dropdown["values"] = []
        style_dropdown.set("")

def add_recipe(root, recipes):
    # Make new window
    window = tk.Frame(root)
    window.config(width=800, height=590, bd=2, relief="solid")
    window.pack_propagate(False)
    window.place(x=710, y=90)

    title = tk.Label(window, text="New Brew Addition: ")
    title.config(font=("Helvetica", 24))
    title.place(x=10, y=10)

    # Farce
    farce = tk.Frame(window)
    farce.config(width=500, height=590, bg="green")
    farce.pack(side="right")

    # Name Entry
    name_label = tk.Label(window, text="Name:")
    name_label.config(font=("Helvetica", 12))
    name_label.place(x=10, y=67)

    name_entry = tk.Entry(window, bd=2, relief="sunken")
    name_entry.config(font=("Helvetica", 12), width=24)
    name_entry.place(x=65, y=65)

    # Start Entry
    start_label = tk.Label(window, text="Start Date: ")
    start_label.config(font=("Helvetica", 12))
    start_label.place(x=10, y=100)

    start_entry = tk.Entry(window, bd=2, relief="sunken")
    start_entry.config(font=("Helvetica", 12), width=9)
    start_entry.insert(0, "2023-10-01")  # Placeholder for get_date_num()
    start_entry.place(x=200, y=95)

    # Variety Dropdown
    variety_label = tk.Label(window, text="Variety: ")
    variety_label.config(font=("Helvetica", 12))
    variety_label.place(x=10, y=133)

    varieties = list(STYLES.keys())  # Get the list of varieties
    variety_dropdown = ttk.Combobox(window, values=varieties)
    variety_dropdown.set("Select a Variety")
    variety_dropdown.place(x=110, y=128)
  

    # Style Dropdown
    style_label = tk.Label(window, text="Style: ")
    style_label.config(font=("Helvetica", 12))
    style_label.place(x=10, y=166)

    style_dropdown = ttk.Combobox(window, values=[])
    style_dropdown.set("Select a style")
    style_dropdown.place(x=110, y=163)

    # Bind the <<ComboboxSelected>> event to update_style_dropdown
    variety_dropdown.bind(
        "<<ComboboxSelected>>",
        lambda event: update_style_dropdown(event, variety_dropdown, style_dropdown)
        )

    
    
