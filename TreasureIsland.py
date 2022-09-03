print("Welcome to Treasure Island. You mission is to find the treasure. ")
p1 = input("Would you like to go left or right? ")
p1.lower()
if p1 == "right":
    print("Game over!")
else:
    print("There is a lake and an island")
    p2 = input("Would you like to wait or swim to the island? ")
    p2.lower()
    if p2 == "swim":
        print("Game Over!")
    else:
        print("you waited for a boat and got to the island")
        p3 = input("There are 3 doors, would you like you open the red, blue, or yellow door? ")
        p3.lower()
        if p3 == "red":
            print("Game Over!")
        elif p3 == "blue":
            print("Game Over!")
        else:
            print("You win!")