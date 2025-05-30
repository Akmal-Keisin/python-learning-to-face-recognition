from helper import cli
from colorama import Fore, Style
import json
import os

def addContact(load_contacts, store_contacts):
	
	message = ""
	while True:
		cli.clear()

		print("--ADD CONTACT MENU--")

		if message != "":
			print(message)
			message = ""

		print("INPUT 0 TO BACK TO MENU")
		
		# Check if user want to exit add menu
		contactName = input("Contact Name : ")
		contactName = contactName.strip()
		if contactName == "0":
			return

		contactNumber = input("Contact Number : ")
		contactNumber = contactNumber.strip()
		if contactNumber == "0":
			return
		
		if contactNumber == "" or contactName == "":
			message = Fore.RED + "Contact name and number cannot be empty" + Style.RESET_ALL
			continue

		if not contactNumber.isdigit():
			message = Fore.RED + "Contact number must be a number" + Style.RESET_ALL
			continue
		
		dictionary = {
			"name": contactName.strip(),
			"number": contactNumber.strip(),
		}

		contacts = load_contacts()
		if len(contacts) == 0:
			store_contacts([dictionary])

		# Check if name already exist, Update if exist
		updateCount = 0
		for i, contact in enumerate(contacts):
			if contact["name"] == dictionary["name"]:
				contacts[i] = dictionary
				updateCount += 1

		if updateCount == 0:
			contacts.append(dictionary)
			message = Fore.GREEN + "Contact name not found, added successfully" + Style.RESET_ALL
		else:
			message = Fore.GREEN + "Contact name found, updated successfully" + Style.RESET_ALL

		store_contacts(contacts)