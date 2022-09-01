number = int(input("Which number would you like to check?"))
number = number.round()
if (number % 2) == 0:
    print("The number you have entered in an even number.")
else:
    print("The number you have entered in an odd number.")
