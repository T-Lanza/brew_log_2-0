STYLES = {
    "wine": ["Red Wine", "White Wine", "Sparkling Wine", "Fruit Wine"],
    "mead": ["Sack Mead", "Dry Mead", "Session Mead", "Melomel", "Metheglin"],
    "beer": ["Ale", "Lager", "Hydromel", "Cider", "Perry"],
    "booze": ["Whisky", "Brandy", "Rum", "Mezcal", "Vodka"]
}

print("")
print("Styles of Alcohol: ")
print("----------------------")
for style in STYLES:
    print(style)

print("")
print("Varieties of Alcohol: ")
print("----------------------")
for style in STYLES:
    for variety in STYLES[style]:
        print(variety)