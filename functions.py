'''1. Write a Python program that finds 
the greatest of three given numbers 
using functions. Pass the numbers as 
arguments.

def find_greatest(a,b,c):
	if a == b and b == c and c == a:
		return "All the values are same"
	elif a > b and a > c:
		return f"{a} is the greatest value"
	elif b > a and b > c:
		return f"{b} is the greatest"
	else:
		return f"{c} is the greatest"

print(find_greatest(10,5,9))

2. Write a Python program using function
that return absolute value of number.

def absolut(a):
	if a < 0:
		return -a
	else:
		return a

print(absolut(5))

3. Write a Python function to sum all 
the numbers in a list.

a = [1,2,4,5,7,8,9,3]
add = 0
def sum_of(a):
	global add
	for item in a:
		add = add + item
	return add

print(sum_of(a))
print(add)

4. Write a Python program to reverse a 
string.

a = [1,2,4,5,7,8,9,3]

def aa(a):
	return a[::-1]

b = lambda a: a[::-1]
print(b(a))

5. Write a Python function to check 
whether a number is in a given range

start = 0
end = 5
num = 1

def check_in(s,e,n):
	if n > s and n < e:
		return True

print(check_in(start, end, num))

6. Write a Python program to print the 
even numbers from a given list.

a = [1,8,7,-6,2,6,9,-8]

def ch(a):
	b = []
	b = [i for i in a if i > 0]
	return b

print(ch(a))

8. Write a Python program that uses 
lambda function to multiply two numbers

a = lambda x,y : x * y

print(a(5,2))

9. Write a Python program that passes 
lambda function as an argument to 
another function to compute the cube 
of a number

a = lambda x : x ** 3
print(a(3))

10.Write a Python program using function 
is_perfect() that returns value 1 if 
the argument passed to it is a perfect 
number and 0 otherwise.

def is_perfect(x):
	add = 0
	for i in range(1,x):
		if x % i == 0:
			add = add + i
	if add == x:
		return 1

print(is_perfect(6))

11.Write a Python program using function 
that accepts an integer between 1 and 
12 to represent the month number and 
displays the corresponding month of the
year. (Exa. If input is 3, then 
output should be MARCH)
--------------------------------------------
38.A lambda function to calculate the sum of 
two numbers

a = lambda x,y : x + y

print(a(2,5))

39.A lambda function to find the bigger number 
in two given numbers

a = lambda x,y : print(x) if x > y else print(y)

a(5,8)

26.A python program to pass a list a list to 
a function and modify it

a = [1,2,4,5,78,9,6,3]

def aa(a):
	a = [i * i for i in a]
	return a

print(aa(a))

29.A python program to understand the use of 
default arguments in a function

def ok(a = 'This is a default parameter'):
	print(a)

ok()

37.A python program to create a lambda function 
that return a square value of a given number

a = lambda x : x ** 2

print(a(3))

21.A function that returns the result of 
addition, subtraction, multiplication and 
division

20.A python program to understand how a function
returns two values

22.A python program to see how to assign a 
function to a variable

def ah(a,b):
	add = a+b
	sub = a-b
	mult = a*b
	div = a/b
	return add, sub, mult, div

z,x,c,v = ah(5,1)
print(z)

27.A python program to understand the positional
arguments of a function

28.A python program to understand the keyword 
arguments of a function

30.A python program to show variable length 
argument and its use

31.A python program to understand keyword 
variable arguments.
def un(a,b,*c):
	print(a)
	print(b)
	print(c)

un(10,12,(20,1),(45))

23.A python program to know how to define a 
function inside another function
def ok():
	print("in ok")
	def not_ok():
		print("In not ok")
	not_ok()

ok()

44. A python program that imports the previous 
python program as module
import temp

temp.pri()

25.A python program to pass an integer to a 
function and modify it

def a(x):
	return x * x

print(a(5))

24.A python program to know how to pass a 
function as parameter to another function
'''
def out():
	def inside(out):
		print(hi)

out()