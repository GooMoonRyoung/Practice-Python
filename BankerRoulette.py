import random

names_string = input('Give me everyone name seperated by a comma. ')
names = names_string.split(', ')
total_people = len(names) 
result = round(random.random() * total_people)

loser = names[result]
print(f'{loser} is going to be paying for the meal.')

