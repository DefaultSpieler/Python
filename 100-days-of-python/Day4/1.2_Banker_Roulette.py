#Banker Roulette
import random

namesAsCSV = input("Give me everybody's names, separated by comma. ")
names = namesAsCSV.split(", ")

length = len(names)
genRan = names[random.randint(0,length - 1)]

print(f"{genRan} is going to buy the meal today!")
