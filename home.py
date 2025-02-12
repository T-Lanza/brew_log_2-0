import tkinter as tk
from tkinter import ttk
from get_date import get_date_num

def nada():
    pass

def get_abv(og, fg):
    if not fg:
        return "TBD"
    else:
        abv = round((og - fg) * 131.25, 1)
        return f"{abv}%"

def home(root, main_display, recipes, menu_bar, main_label):

    a = main_display
    b = menu_bar
    c = main_label

    for widget in root.winfo_children():
        if widget != a and widget != b and widget != c:
            widget.destroy()

    for widget in a.content_frame.winfo_children():
        widget.destroy()
   
    counter = 1
    for recipe in recipes:
        # Create Blurb Frame
        recipe_blurb = tk.Frame(main_display.content_frame)
        recipe_blurb.config(width=590, height=45, bd="5", relief="raised")
        if recipe["style"] == "Red Wine":
            recipe_blurb.config(bg="purple")
        if recipe["style"] == "White Wine":
            recipe_blurb.config(bg="yellow")
        if recipe["style"] == "Sparkling Wine":
            recipe_blurb.config(bg="pink")
        if recipe["style"] == "Fruit Wine":
            recipe_blurb.config(bg="green")
        if recipe["style"] == "Sack Mead":
            recipe_blurb.config(bg="gold")
        if recipe["style"] == "Dry Mead":
            recipe_blurb.config(bg="yellow")
        if recipe["style"] == "Session Mead":
            recipe_blurb.config(bg="yellow")
        if recipe["style"] == "Melomel":
            recipe_blurb.config(bg="gold")
        if recipe["style"] == "Metheglin":
            recipe_blurb.config(bg="gold")
        if recipe["style"] == "Ale":
            recipe_blurb.config(bg="brown")
        if recipe["style"] == "Lager":
            recipe_blurb.config(bg="light brown")
        if recipe["style"] == "Hydromel":
            recipe_blurb.config(bg="yellow")
        if recipe["style"] == "Cider":
            recipe_blurb.config(bg="red")
        if recipe["style"] == "Perry":
            recipe_blurb.config(bg="yellow")
        if recipe["style"] == "Whisky":
            recipe_blurb.config(bg="black")
        if recipe["style"] == "Brandy":
            recipe_blurb.config(bg="orange")
        if recipe["style"] == "Rum":
            recipe_blurb.config(bg="light green")
        if recipe["style"] == "Mezcal":
            recipe_blurb.config(bg="blue")
        if recipe["style"] == "Vodka":
            recipe_blurb.config(bg="light blue")
        recipe_blurb.pack_propagate(False)

        # Recipe Date
        blurb_date = tk.Label(recipe_blurb, text=recipe["start_date"])
        blurb_date.config(font=("Helvetica", 15), width=10, pady=10)
        if counter % 2 != 0:
            blurb_date.config(bg="#E6EDFF")
        else:
            blurb_date.config(bg="white")
        blurb_date.pack(side="left")

        # Recipe Title
        blurb_name = tk.Label(recipe_blurb, text=recipe["name"])
        blurb_name.config(font=("Helvetica", 15), width=18, pady=10)
        if counter % 2 != 0:
            blurb_name.config(bg="white")
        else:
            blurb_name.config(bg="#E6EDFF")
        blurb_name.pack(side="left")

        # Recipe ABV
        blurb_abv = tk.Label(recipe_blurb, text=get_abv(recipe["og"], recipe["fg"]))
        blurb_abv.config(font=("Helvetica", 15), width=7, pady=10)
        if counter % 2 != 0:
            blurb_abv.config(bg="#E6EDFF")
        else:
            blurb_abv.config(bg="white")
        blurb_abv.pack(side="left")

        # Recipe Style
        blurb_style = tk.Label(recipe_blurb, text=recipe["style"])
        blurb_style.config(font=("Helvetica", 15), width=12, pady=10)
        if counter % 2 != 0:
            blurb_style.config(bg="white")
        else:
            blurb_style.config(bg="#E6EDFF")
        blurb_style.pack(side="left")

        # Go to Recipe Button
        blurb_button = tk.Button(recipe_blurb, text=" >> ")
        blurb_button.config(width=3, command=nada)
        blurb_button.pack(side="right")

        # Insert blurb into Display
        recipe_blurb.pack(side="bottom")
        counter += 1