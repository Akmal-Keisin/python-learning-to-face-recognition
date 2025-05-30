from helper import cli
from colorama import Fore, Style
from tabulate import tabulate
import os
import json

def removeContact(load_contacts, store_contacts):
	
	message = ""
	contacts = load_contacts()
	
	if len(contacts) == 0:
		print(Fore.RED + "No contacts found." + Style.RESET_ALL)
		print("Returning to menu...")
		return

	while True:
		cli.clear()
		print("--REMOVE CONTACT MENU--")
		
		if message != "":
			print(message)
			message = ""

		print("Contacts:")
		print(tabulate(contacts, headers="keys", tablefmt="grid"))
		print(Fore.GREEN + "Total contacts: " + str(len(contacts)) + Style.RESET_ALL)

		contactName = input("Please enter the contact name to remove (or 0 to cancel): ")
		contactName = contactName.strip()
		if contactName == "0":
			return
		
		if contactName == "":
			message = Fore.RED + "Contact name cannot be empty" + Style.RESET_ALL
			continue
		
		# Find the contact to remove
		contactFound = False
		for i, contact in enumerate(contacts):
			if contact["name"].lower() == contactName.lower():
				contactFound = True
				del contacts[i]
				break
		
		if not contactFound:
			message = Fore.RED + f"Contact '{contactName}' not found" + Style.RESET_ALL
			continue

		# Save the updated contacts back to the file
		store_contacts(contacts)
		message = Fore.GREEN + f"Contact '{contactName}' removed successfully" + Style.RESET_ALL
		continue
		
