class Animal:
	def __init__(self, name):
		self.__name = name  # private attribute

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	def speak(self):
		raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
	def speak(self):
		return f"{self.get_name()} says Woof!"

class Cat(Animal):
	def speak(self):
		return f"{self.get_name()} says Meow!"

my_dog = Dog("Buddy")
print(my_dog.speak())

my_cat = Cat("Angela")
print(my_cat.speak())

# Encapsulation in action:
my_dog.set_name("Max")
print(my_dog.speak())