# This is a simple contact management project.
# This project should able to :
# - Add contact
# - Get the contact list
# - Find a contact
# - Remove a contact

from controller.contact_manager import ContactManager
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

		contactManager = ContactManager()
		if selectedMenu == 1:
			contactManager.add_contact()
		elif selectedMenu == 2:
			contactManager.get_contact()
		elif selectedMenu == 3:
			contactManager.find_contact()
		elif selectedMenu == 4:
			contactManager.remove_contact()
		elif selectedMenu == 0:
			print("Good Bye")
			return
		else:
			print("The menu number is not in the list")

main()