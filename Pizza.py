print("Welcome to the Python Pizza Delivery")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
total = 0 
sp = 15
mp = 20
lp = 25
spep = 2
pep = 3
cheese = 1

if size == "S":
    total += sp
    if add_pepperoni == "Y":
        total += spep
elif size == "M":
    total += mp
    if add_pepperoni == "Y":
        total += pep
else:
    total += lp
    if add_pepperoni == "Y":
        total += pep

if extra_cheese == "Y":
    total += cheese


print (f"Your final bill is: ${total}.")