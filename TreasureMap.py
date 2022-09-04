row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? "))

if position == 33:
    map[2][2] = 'x'
elif position == 32:
    map[1][2] = 'x'
elif position == 31:
    map[0][2] = 'x'
elif position == 23:
    map[2][1] = 'x'
elif position == 22:
    map[1][1] = 'x'
elif position == 21:
    map[0][1] = 'x'
elif position == 13:
    map[2][0] = 'x'
elif position == 12:
    map[1][0] = 'x'
elif position == 11:
    map[0][0] = 'x'
else:
    print('Your coordinates are invalid')

print(f"{row1}\n{row2}\n{row3}")

