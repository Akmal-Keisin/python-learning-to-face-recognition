from helper import cli
import os
import json

def findContact(load_contacts):
	while True:
		cli.clear()
		print("--FIND CONTACT MENU--")
		print("Input 0 to back to menu")

		contacts = load_contacts()
		if len(contacts) == 0:
			print("No contact found, please add contact first")
			return

		contactName = input("Please enter the contact name to find : ")
		contactName = contactName.strip()
		if contactName == "":
			print("Contact name cannot be empty")
			return
		
		if contactName == "0":
			return
		
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
		