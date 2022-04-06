import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#', '%', '&', '*', '+', '(', ')']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password = []
f_pass = ""

t_alpha = int(input("Enter the number of alphabets you want in your password"))
t_sym = int(input("Enter the number of symbols you want in your password"))
t_num = int(input("Enter the number of numbers you want in your password"))

totalNo = t_alpha + t_sym + t_num

for i in range(0, t_alpha):
    ff = random.choice(alphabets)
    password.append(ff)
for i in range(0, t_sym):
    dd = random.choice(symbols)
    password.append(dd)
for i in range(0, t_num):
    ee = random.choice(numbers)
    password.append(ee)

str_pass = "".join(password)
print(f"The unshuffled output is {str_pass}")

random.shuffle(password)
s = "".join(password)
print(f"The shuffled output is {s}")

