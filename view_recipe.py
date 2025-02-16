import tkinter as tk
import json

def view_recipe(recipe_id):
    with open('DATA/recipes.json', 'r') as file:
        all_recipes = json.load(file)

    for recipe in all_recipes:
        if recipe["id"] == recipe_id:
            selection = {
                "id": recipe_id,
                "name": recipe["name"],
                "style": recipe["style"],
                "og": recipe["og"],
                "fg": recipe["fg"],
                "start_date": recipe["start_date"],
                "bottle_date": recipe["bottle_date"],
                "yeast": recipe["yeast"],
                "ingredients": recipe["ingredients"],
                "notes": recipe["notes"]
            }

    print(selection["name"])