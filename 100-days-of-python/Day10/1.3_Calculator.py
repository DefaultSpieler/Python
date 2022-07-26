def add(n1, n2):
	return n1 + n2

def sub(n1, n2):
	return n1 - n2

def mult(n1, n2):
	return n1 * n2

def div(n1, n2):
	return n1 / n2

dic = {
	"+" : add,
	"-" : sub,
	"*" : mult,
	"/" : div
}

num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
for i in dic:
	print(i)

op = input("Choose an operation")

for q in dic:
	fun = dic[op]
	ans = fun(num1, num2)

print(ans)