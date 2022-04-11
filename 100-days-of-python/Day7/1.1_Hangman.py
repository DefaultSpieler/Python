# - Hangman Game -------------------------------------------------------
import random

# - variables declaration

# - a list containing all the words
wordlist = ["ardvark", "baboon", "camel"]

# - an empty list where to save the user input
display = []

# - remaninig lives counter
lives = 6

# - a list for the stages of the hangman
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# - to randomly choose a word from the list and to assign it to variable chosenWord
chosenWord = random.choice(wordlist)

# - to assign '_' values to the list called display according to the chosenWord count
for i in range(len(chosenWord)):
	display.append('_')

# - to loop through until the user gets the right answer
while True:
# - to check if any blank spaces are remaining
	if not '_' in display:
		break;
	else:
# - to take input from the user as their answer and assign the value to variable guess
		guess = input("Enter your choice of letter").lower()
# - to loop through the chosenWord variable to find if the user guesses a right alphabet
		for i in range(len(chosenWord)):
			if(guess == chosenWord[i]):
				display[i] = guess
		print(display)
# - counter for lives remaining and to check if the user is out of lives
		if not guess in display:
			lives -= 1
			if lives == 0:
				print("You Lose ")
				break;
# - to print the hangman live according to the lives remaining
		print(stages[lives])

