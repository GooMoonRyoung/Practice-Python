import random 
#Step 1 


word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#chosen_word = random.choice(word_list)
chosen_word = "baboon"

guess = input("Please guess a letter in this random word: ").lower()
counter = 0
for character in chosen_word:
        #guess = input("Please guess a letter in this random word: ").lower()
        if character == guess:
            print('right')
            counter += 1
        else:
            print('wrong')
            counter += 1
    #if counter < 4:
    #else:
    #    print('you lose')
