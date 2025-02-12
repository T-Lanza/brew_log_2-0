import tkinter as tk
from get_date import get_date_num, get_date_id
import json

with open('DATA/recipes.json', 'r') as file:
    recipes = json.load(file)


def add_recipe(root, recipes):
    # Make new window
    window = tk.Frame(root)
    window.config(width=300, height=300, bg="blue")
    window.place(x=700, y=90)