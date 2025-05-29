from helper import cli
import os
import json

def findContact():
	while True:
		cli.clear()
		print("--FIND CONTACT MENU--")
		print("Input 0 to back to menu")

		# Check if the contact storage exist
		path = os.path.join(os.getcwd(), "storage/contact.json")
		if not os.path.exists(path):
			print("No contact found, please add contact first")
			return
		
		contactName = input("Please enter the contact name to find : ")
		contactName = contactName.strip()
		if contactName == "":
			print("Contact name cannot be empty")
			return
		
		if contactName == "0":
			return
		
		with open(path, "r") as file:
			contacts = file.read()
			contacts = json.loads(contacts)

			matches = [c for c in contacts if c.get("name", "").lower() == contactName.lower()]
			if matches:
				print("Contacts found:")
				for contact in matches:
					print("Name :", contact["name"])
					print("Number :", contact["number"])
			else:
				print("Contact not found.")

			choice = input("Find another contact? (y/n)").strip().lower()
			if choice == "n":
				return
			elif choice != "y":
				print("Invalid input, returning to menu...")
				return
		