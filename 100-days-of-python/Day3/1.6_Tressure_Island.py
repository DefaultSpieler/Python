#Project - Treasure island

print("Welcome to Tressue Island.")
print(" Your mission is to find the Tressure")

que = input('You are at a cross road. Where do you want to go ? Type "right" or "left"')

if que == "left":
	print("...")
	que2 = input("Will you swim or wait?")
	if que2 == "swim":
		print("You lose.")
		print("Game Over")
	elif que2 == "wait":
		print("...")
		que3 = input("There are three doors - yellow, green and red. Choose one")
		if que3 == "yellow":
			print("You win. You have the tressure now")
		elif que3 == "green" or que3 == "red":
			print("You lose. Game Over")
elif que == "right":
	print("You lose.")
	print("Game Over")
else:
	print("Input not appropriate")