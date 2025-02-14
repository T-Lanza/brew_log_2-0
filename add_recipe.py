import tkinter as tk
from tkinter import ttk
from get_date import get_date_num, get_date_id
import json
from constants import *
from id_digits import id_digits
from home import home
from scrollframe import ScrollableFrame

with open('DATA/recipes.json', 'r') as file:
    recipes = json.load(file)

def get_id(name):
    date = get_date_id()
    name_id = name[:3].upper()

    return f"{date}{name_id}{id_digits()}"


def submit(ingredients, 
           name_entry, 
           start_entry, 
           style_dropdown, 
           og_entry, 
           yeast_entry, 
           notes_entry,
           recipes):
    recipe = {
        "id": get_id(name_entry.get()),
        "name": name_entry.get(),
        "style": style_dropdown.get(),
        "status": "Fermenting",
        "og": og_entry.get(),
        "fg": og_entry.get(),
        "start_date": start_entry.get(),
        "bottle_date": "",
        "yeast": yeast_entry.get(),
        "ingredients": ingredients,
        "notes": [],
    }

    added_notes = notes_entry.get("1.0", tk.END)
    recipe_notes = {
        "date": get_date_num(),
        "note": added_notes
    }
    recipe["notes"].append(recipe_notes)

    recipes.append(recipe)

    with open('DATA/recipes.json', 'w') as file:
        json.dump(recipes, file, indent=4)
    


def add_ingredient(amount, format, entry, window, i_list):
    qty = str(amount.get())
    measure = str(format.get())
    item = str(entry.get())

    ingredient = {
        "qty": qty,
        "measure": measure,
        "item": item
    }

    i_list.append(ingredient)

    pane = tk.Label(window.content_frame, font=("Helvetica", 12))
    pane.config(text=f"{qty}{measure} {item}", justify="left")
    pane.config(padx=5, pady=5, bg="white")
    pane.pack(side="top")

    amount.delete(0, tk.END)
    format.set("")
    entry.delete(0, tk.END)


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
    ingredients = []
    print(ingredients)
    # Make new window
    window = tk.Frame(root)
    window.config(width=800, height=590, bd=5, relief="sunken")
    window.pack_propagate(False)
    window.place(x=710, y=90)

    title = tk.Label(window, text="New Brew Addition: ")
    title.config(font=("Helvetica", 24))
    title.place(x=10, y=10)

    # Farce
    farce = tk.Frame(window)
    farce.config(width=500, height=590)
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
    start_entry.insert(0, get_date_num())
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
    
    # OG Section
    og_label = tk.Label(window, text="OG (Original Gravity): ")
    og_label.config(font=("Helvetica", 12))
    og_label.place(x=10, y=199)

    og_entry = tk.Entry(window, bd=2, relief="sunken")
    og_entry.config(font=("Helvetica", 12), width=9)
    og_entry.place(x=198, y=196)

    # Yeast Section
    yeast_label = tk.Label(window, text="Yeast: ")
    yeast_label.config(font=("Helvetica", 12))
    yeast_label.place(x=10, y=232)

    yeast_entry = tk.Entry(window, bd=2, relief="sunken")
    yeast_entry.config(font=("Helvetica", 12), width=9)
    yeast_entry.place(x=198, y=229)

    # Add Notes Section
    notes_label = tk.Label(window, text="Preliminary Notes: ")
    notes_label.config(font=("Helvetica", 12))
    notes_label.place(x=10, y=265)

    notes_entry = tk.Text(window, width=30, height=15, bd=2, relief="sunken")
    notes_entry.config(bg="white", font=("Helvetica", 12), wrap="word")
    notes_entry.place(x=7, y=298)

    # Ingredients
    add_ingredients_label = tk.Label(farce, text="Add Ingredients: ")
    add_ingredients_label.config(font=("Helvetica", 12))
    add_ingredients_label.place(x=25, y=67)

    qty_input = tk.Entry(farce, bd=2, relief="sunken")
    qty_input.config(font=("Helvetica", 12), width=3)
    qty_input.place(x=25, y=94)

    measure_dropdown = ttk.Combobox(farce, values=MEASURES)
    measure_dropdown.config(width=5)
    measure_dropdown.place(x=65, y=95)

    ingredient_entry = tk.Entry(farce, bd=2, relief="sunken")
    ingredient_entry.config(font=("Helvetica", 12), width=35)
    ingredient_entry.insert(0, "Enter Ingredient here....")
    ingredient_entry.place(x=125, y=94)

    ingredient_list = ScrollableFrame(farce)
    ingredient_list.config(width=445, height=440)
    ingredient_list.place(x=25, y=123)

    add_ingredients_button = tk.Button(farce, text="+", font=("Helvetica", 12))
    add_ingredients_button.config(command=lambda: add_ingredient(qty_input,
                                                                 measure_dropdown,
                                                                 ingredient_entry,
                                                                 ingredient_list,
                                                                 ingredients))
    add_ingredients_button.place(x=450, y=90)

    # Submit Button
    submit_button = tk.Button(farce, text="Submit")
    submit_button.config(font=("Helvetica", 12), command=lambda: submit(ingredients,
                                                                        name_entry,
                                                                        start_entry,
                                                                        style_dropdown,
                                                                        og_entry,
                                                                        yeast_entry,
                                                                        notes_entry,
                                                                        recipes))
    submit_button.place(x=25, y=12)
