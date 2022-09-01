print("Welcome to the rollercoaster!")
age = int(input("What is your age? "))
height = int(input("What is your height in cm? "))
cprice = 5
tprice = 7
aprice = 12
photo_price = 3
total = 0

if height >= 120:
    print ("You can ride the rollercoaster")
    if age < 12:
        print(f"Child tickets are ${cprice}")
        total = cprice
    elif age <= 18:
        print(f"Teenager tickets are ${tprice}")
        total = tprice
    elif age >= 45 and age <= 55:
        print("you are having a mid life crisis and you get to ride for free.")
    else:
        print(f"Adult tickets are ${aprice}")
        total = aprice

    photo = input("Do you want a photo taken? Y or N ")
    if photo == "Y":
        total += photo_price
        print(f"your total will be ${total}")
    print(f"your total will be ${total}")

else:
    print ("You are too short to ride this rollercoaster, sorry")
