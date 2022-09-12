#Simple Function 
def greetings():
    print('Hello')
    print('Bon Jour')
    print('Salut')

greetings()


#function that allows input
def greetings_with_name(name):
    print(f'Hello, {name}')
    print(f'How do you do {name}?')
user = input('Please tell me your name: ')
greetings_with_name(user)


#Functions that can take more than 1 input
def greet_with(name, location):
    print(f'Hello, {name}')
    print(f'What is it like in {location}?')
user = input('Please tell me your name: ')
location = input('Please tell me your location: ')
greet_with(location=location, name=user)