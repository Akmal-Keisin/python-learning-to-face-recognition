from helper import cli
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
			message = "Contact name and number cannot be empty"
			continue

		if not contactNumber.isdigit():
			message = "Contact number should only contain digits"
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
			message = "Contact added successfully"
		else:
			message = "Contact name found, updated successfully"

		store_contacts(contacts)