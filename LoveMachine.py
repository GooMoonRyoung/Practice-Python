from re import L

print("Welcome to the love calculator")
name1 = input("What is your name? \n" )
name2 = input("What is their name? \n")
name = name1.lower() + name2.lower()
total = 0
true_total = 0
love_total = 0

true_total = name.count("t")
true_total += name.count("r")
true_total += name.count("u")
true_total += name.count("e")
true_total = true_total * 10

love_total = name.count("l")
love_total += name.count("o")
love_total += name.count("v")
love_total += name.count("e")


total = true_total + love_total

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total <= 50 and total >= 40:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")

