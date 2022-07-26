# Functions with output


def my_format(f_name, l_name):
	if f_name == "" and l_name == "":
		return "Enter a valid input"
	fName = f_name.title()
	lName = l_name.title()
	return f"Result : {fName} {lName}"

my_format(input("Enter your first name "), input("Enter your last name "))
