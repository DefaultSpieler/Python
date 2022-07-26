alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encrypted = ""
decoded = ""

def encrypt():
	
	for i in text:
		pos = alphabet.index(i)
		new_pos = pos + shift
		global encrypted
		encrypted += alphabet[new_pos]
	print("-----------------------------------")
	print(encrypted)
	print("-----------------------------------")


def decode():
	encrypted
	for i in encrypted:
		pos = alphabet.index(i)
		new_pos = pos - shift
		global decoded
		decoded += alphabet[new_pos]
	print("-----------------------------------")
	print(f"The decoded message is {decoded}")
	print("-----------------------------------")

print("Welcome to Caesar Cipher")
print("-----------------------------------")
text = input("Type your message:\n").lower()
print("-----------------------------------")
shift = int(input("Type the shift number:\n"))
print("-----------------------------------")
encrypt()
print("-----------------------------------")
option = input("DO you wish to decode the mesaage? Press yes to decode \n")
if option == "yes":
	print("-----------------------------------")
	decode()
	print("-----------------------------------")
