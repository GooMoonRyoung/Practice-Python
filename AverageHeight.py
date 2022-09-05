student_heights = input("Input a list of student heights ").split(" ")
totalheight = 0
student_total = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

for height in student_heights:
    totalheight += height

for students in student_heights:
    student_total +=1

print(round(totalheight / student_total))