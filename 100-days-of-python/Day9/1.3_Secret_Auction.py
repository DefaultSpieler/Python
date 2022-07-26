from os import system

logo =  '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("-------------")
print("Welcome to Secret Auction")

counter = 0
bid = {}

def clear():
  _ = system('cls')

def takeInput():
  global counter
  counter += 1
  temp = {}
  print("-------------")
  temp["name"] = input("Enter your name : ")
  print("-------------")
  temp["amt"] = int(input("Enter your amount : "))
  print("-------------")
  bid[counter] = temp

def findBig():
  chk = 0
  name = ""
  for i in bid:
    if bid[i]["amt"] > chk:
      chk = bid[i]["amt"]
      name = bid[i]["name"]
  print(f"The highest bid was by {name} and the amount was {chk}")

while True:
  takeInput()
  choice = input("Are there any other bidders ? yes or no ")
  print("-------------")
  if choice == "yes":
    clear()
    continue
  elif choice == "no":
    clear()
    findBig()
    break;
  else:
    print("ENTER A VALID CHOICE")
