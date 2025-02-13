import random
import string


def id_digits():
    
    id_string = []

    for i in range(5):
        check = random.randint(1,3)
        if check == 1:
            char = str(random.randint(0, 9))
            id_string.append(char)
        if check == 2:
            char = random.choice(string.ascii_lowercase)
            id_string.append(char)
        if check == 3:
            char = random.choice(string.ascii_uppercase)
            id_string.append(char)

    random.shuffle(id_string)

    return "".join(id_string)
