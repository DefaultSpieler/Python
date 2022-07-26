n = int(input("Check this number: "))

def prime_checker(number):
	check = True
	for i in range(2,number - 1):
		if number % i == 0:
			check = False
	if check:
		print("prime")
	else:
		print("not prime")


prime_checker(number = n)