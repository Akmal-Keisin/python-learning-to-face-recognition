class Dog:
	# __init_ is a special method that initializes the object
	# It is called when an object of the class is created
	def __init__(self, name, type):
		self.name = name
		self.typ = type

	# Methods are functions defined inside a class
	# They can be called on an object of the class
	def bark(self):
		print(f"{self.name} is barking!")

	def identify(self):
		print(f"This is {self.name}, a {self.typ} dog.")

my_dog = Dog("Martha", "Chihuahua")
my_dog.bark()