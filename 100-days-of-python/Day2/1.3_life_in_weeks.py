print("Life in Weeks")
curAge = int(input("Enter your current age "))

totalAgeInWeeks = 90 * 52
totalAgeInDays = 90 * 365
totalAgeInMonths = 90 * 12

cAgeInDays = curAge * 365
cAgeInWeeks = curAge * 52
cAgeInMonths = curAge * 12

weeksLeft = totalAgeInWeeks - cAgeInWeeks
daysLeft = totalAgeInDays - cAgeInDays
monthsLeft = totalAgeInMonths - cAgeInMonths

print(f"You have {daysLeft} days left, {weeksLeft} weeks left and {monthsLeft} months left to live")

#-----------------------------------OR ---------------------------------------------------

yearsRemaining = 90 - curAge
monthsRemaining = yearsRemaining * 12
weeksRemaining = yearsRemaining * 52
daysRemaining = yearsRemaining * 365

print(f"You have {daysRemaining} days left, {weeksRemaining} weeks left and {monthsRemaining} months left to live")


