row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

vertical_position = int(position[0])
horizontal_position = int(position[1])

map[horizontal_position - 1][vertical_position - 1] = 'x'
print(f"{row1}\n{row2}\n{row3}")