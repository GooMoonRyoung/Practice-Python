import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
total_length = nr_letters + nr_symbols + nr_numbers

cont = []
character_count = total_length

for x in range (0, total_length):
    if nr_letters > 0 and nr_symbols > 0 and nr_numbers > 0 and character_count > 0:
        character_count -= 1
        selector = random.randint (1,3)
        if selector == 1:
            nr_letters -= 1
            cont.append(letters[random.randint(0, len(letters) - 1)])
        elif selector == 2:
            nr_numbers -= 1
            cont.append(numbers[random.randint(0, len(numbers) - 1)])
        elif selector == 3:
            nr_symbols -= 1
            cont.append(symbols[random.randint(0, len(symbols) - 1)])
    elif nr_letters > 0 and nr_numbers > 0 and character_count > 0:
        selector = random.randint (1,2)
        if selector == 1:
            nr_letters -= 1
            cont.append(letters[random.randint(0, len(letters) - 1)])
        elif selector == 2:
            nr_numbers -= 1
            cont.append(numbers[random.randint(0, len(numbers) - 1)])
    elif nr_letters > 0 and nr_symbols > 0 and character_count > 0:
        selector = random.randint (1,2)
        if selector == 1:
            nr_letters -= 1
            cont.append(letters[random.randint(0, len(letters) - 1)])
        elif selector == 2:
            nr_symbols -= 1
            cont.append(symbols[random.randint(0, len(symbols) - 1)])
    elif nr_symbols > 0 and nr_numbers > 0 and character_count > 0:
        selector = random.randint (1,2)
        if selector == 1:
            nr_numbers -= 1
            cont.append(numbers[random.randint(0, len(numbers) - 1)])
        elif selector == 2:
            nr_symbols -= 1
            cont.append(symbols[random.randint(0, len(symbols) - 1)])
    elif nr_letters > 0 and character_count > 0:
        cont.append(letters[random.randint(0, len(letters) - 1)])
    elif nr_numbers > 0 and character_count > 0:
        cont.append(numbers[random.randint(0, len(numbers) - 1)])
    elif nr_symbols > 0 and character_count > 0:
        cont.append(symbols[random.randint(0, len(symbols) - 1)])

print("".join(cont))