#Average Height

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total = 0
length = 0

for height in student_heights:
    total = height + total
    length = length + 1

print(f"The total is {total}")
print(f"The length is {length}")

# --for average --

average = total / length

print(f"The average is {average}")

#High Score

student_score= input("Input a list of student score ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

maxi = 0

for score in student_score:
    if maxi < score:
        maxi = score
print(f"The highest score is: {maxi}")

#Adding Even Numbers

total = 0
for number in range(2, 101, 2):
    total += number
    print(number)
print(total)

#The FizzBuzz Job Interview Question

for num in range(1, 101):
    if  num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 == 0:
        print("fizz")
    else:
        print(num)

#Project - Create a Password Generator