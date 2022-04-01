#Pizza Order Practice

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want?S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0

if size =="S":
	price = 15
	if add_pepperoni == "Y":
		price = price + 2
	else:
		price = price
	if extra_cheese == "Y":
		price = price + 1
	else:
		price = price
elif size == "M":
	price = 20
	if add_pepperoni == "Y":
		price = price + 3
	else:
		price = price
	if extra_cheese == "Y":
		price = price + 1
	else:
		price = price
elif size == "L":
	price = 25
	if add_pepperoni == "Y":
		price = price + 3
	else:
		price = price
	if extra_cheese == "Y":
		price = price + 1
	else:
		price = price
else:
	print("Enter a correct value")

print(f"Your final bill is {price}")