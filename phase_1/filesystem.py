# Reading file
with open("files/data.txt", "r") as file:
	contents = file.read()
	print(contents)

# Writing to file
with open("files/output.txt", "w") as file:
	file.write("Hello, file!\nThis is Python writing to this file.")