#Love Calculator

print("Welcome to Love Calculator")

urName = input("What is your Name? ")
theirName = input("What is their name? ")

combine = urName + theirName
combined = combine.lower()

T = combined.count("t")
R = combined.count("r")
U = combined.count("u")
E = combined.count("e")

totalTrue = T + R + U + E

L = combined.count("l")
O = combined.count("o")
V = combined.count("v")
E = combined.count("e")

totalLove = L + O + V + E

per = int(str(totalTrue) + str(totalLove))


if per >= 90 or per <= 10:
	print(f"Your score is {per}%. You together are like mentos and coke")
elif per >= 40 and per <= 50:
	print(f"Your score is {per}%. You are alright together")
else:
	print(f"Your score is {per}%.")