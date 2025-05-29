from helper import cli
import json
import os

def listContact():
	cli.clear()
	print("--LIST CONTACT MENU--")

	path = os.path.join(os.getcwd(), "storage/contact.json")

	# Check if the contact storage exist
	if not os.path.exists(path):
		print("No contact found, please add contact first")
		return

	with open(path, "r") as file:
		contacts = file.read()
		contacts = json.loads(contacts)
		
		if len(contacts) == 0:
			print("No contact found, please add contact first")

		for i, contact in enumerate(contacts):
			print(f"{i + 1}. {contact['name']} - {contact['number']}")
		
		# Check if user want to exit add menu
		choice = input("Input 0 to back to the menu :")
		if choice.strip() == "0":
			return
		else:
			print("Invalid input, returning to menu...")
			return