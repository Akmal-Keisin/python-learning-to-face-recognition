from helper import cli
import json
import os

def listContact(load_contacts):
	cli.clear()
	print("--LIST CONTACT MENU--")

	contacts = load_contacts()
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