# Not like PHP, JS, Go. In Python, indentation = block

# Conditions
percentage = 100

if percentage < 50:
	print("Grade D")
elif percentage < 70:
	print("Grade C")
elif percentage < 80:
	print("Grade B")
elif percentage < 90:
	print("Grade B+")
elif percentage < 95:
	print("Grade A")
elif percentage <= 100:
	print("Grade A+")
else:
	print("Not a grade")

# For Loops
fruits = ["Banana", "Apple", "Orange"]
for fruit in fruits:
	print(fruit)

# For range() loop
for index in range(5):
	print(index)

# While Loops
age = 10
while age < 20:
	print(age)
	age += 1
