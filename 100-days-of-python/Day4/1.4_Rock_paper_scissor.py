#Project - Rock Paper Scissors


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

array = [rock , paper, scissors]


user = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors"))

compIn = int(random.randint(0,2))

print(f"your choice {array[user]}")

print(f"computer's choice {array[compIn]}")

if(user == 0 and compIn == 2):
	print("You win")
elif(user == 0 and compIn == 1 ):
	print("You lose")
elif(user == 1 and compIn == 0):
	print("You win")
elif(user == 1 and compIn == 2):
	print("You lose")
elif(user == 2 and compIn == 0):
	print("You lose")
elif(user == 2 and compIn == 1):
	print("You win")
elif(user == compIn):
	print("Tied")
else:
	print("fedce")
