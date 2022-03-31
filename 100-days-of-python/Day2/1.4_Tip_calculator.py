print("Welcome to the tip calculator")

totalBill = float(input("What was the total bill? "))
per = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
split = float(input("How many people to split the bill? "))

ans = (totalBill * (per / 100)) + totalBill

final = ans / split
print(round(final), 2)