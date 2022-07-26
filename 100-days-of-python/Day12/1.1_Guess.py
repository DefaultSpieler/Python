import random

#welcome part
wel = """

     __                 _                                           _                                          
  /\ \ \_   _ _ __ ___ | |__   ___ _ __    __ _ _   _  ___  ___ ___(_)_ __   __ _    __ _  __ _ _ __ ___   ___ 
 /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|  / _` | | | |/ _ \/ __/ __| | '_ \ / _` |  / _` |/ _` | '_ ` _ \ / _ \
/ /\  /| |_| | | | | | | |_) |  __/ |    | (_| | |_| |  __/\__ \__ \ | | | | (_| | | (_| | (_| | | | | | |  __/
\_\ \/  \__,_|_| |_| |_|_.__/ \___|_|     \__, |\__,_|\___||___/___/_|_| |_|\__, |  \__, |\__,_|_| |_| |_|\___|
                                          |___/                             |___/   |___/                                                                                                                          
"""
print("Welcome to ")
print(wel)



#input for level selection
level = input("Choose a difficulty level. Type easy or hard ")

# generating number between 1 - 100
num = random.randint(0, 100)
print(num)


def guess():
	# assigns the number of attempts according to the difficulty decided by the user
	if level == "easy":
		attempts = 10
	elif level == "hard":
		attempts = 5
	else:
		return "Enter a valid input"
	print(f"Attempts {attempts}")
	
	remain = attempts
	# loop checking the guess
	for i in range(1, attempts):
		guess = int(input("Make a guess"))
		remain -= 1
		if guess < num :
			print("Too Low")
		elif guess > num :
			print("Too high")
		elif guess == num :
			print("You made it")
			print(f"Attempts remaining {remain} ")
			break
		else:
			print("-----------")

guess()
