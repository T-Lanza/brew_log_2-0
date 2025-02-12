from get_date import get_date_id, get_date_num

iteration = "001"

recipe = {
    "start": get_date_num(),
    "name": "honningdrom",
    "id": ""
}

name_id = recipe["name"][0:3].upper()

full_id = f"{get_date_id()}{name_id}-{iteration}"

print(full_id)