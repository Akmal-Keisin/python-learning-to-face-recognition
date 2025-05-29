# This is a simple contact management project.
# This project should able to :
# - Add contact
# - Get the contact list
# - Find a contact

from businessLogic import addContactLogic, findContactLogic, listContactLogic, removeContactLogic
from helper import cli

def main():
	while True:
		cli.clear()
		print("--CONTACT MANAGEMENT APP--")
		print("Please input the number to select the menu : ")
		print("Input 0 to exit")
		print("1. Add Contact")
		print("2. List Contact")
		print("3. Find Contact")
		print("4. Remove Contact")

		selectedMenu = input("Please enter the menu number : ")
		selectedMenu = selectedMenu.strip()

		try:
			selectedMenu = int(selectedMenu)
		except:
			print("The menu number should be a number")
			continue

		if selectedMenu == 1:
			addContactLogic.addContact()
		elif selectedMenu == 2:
			listContactLogic.listContact()
		elif selectedMenu == 3:
			findContactLogic.findContact()
		elif selectedMenu == 4:
			removeContactLogic.removeContact()
		elif selectedMenu == 0:
			print("Good Bye")
			return
		else:
			print("The menu number is not in the list")

main()