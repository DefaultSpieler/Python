#BMI 2.0

weight = float(input("Enter your weight"))
height = float(input("Enter your height"))

bmi = weight / height ** 2

if bmi < 18.5:
	print("underweight")
elif bmi < 25:
	print("normal weight")
elif bmi < 30:
	print("overweight")
elif bmi < 35:
	print("obese")
else:
	print("clinically obese")
