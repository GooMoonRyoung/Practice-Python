is_male = False
is_tall = True

if is_male and is_tall:
    print("you are a tall male.")
elif is_male and not(is_tall):
    print("you are a short male.")
elif is_tall and not(is_male):
    print ("you are a tall non male")
else:
    print("you neither tall or a male ")