from helper import cli
import os
import json

def removeContact():

	path = os.path.join(os.getcwd(), "storage/contact.json")

	# Check if the contact storage exist
	if not os.path.exists(path):
		print("No contact found, please add contact first")
		return
	
	message = ""
	while True:
		cli.clear()
		print("--REMOVE CONTACT MENU--")
		
		if message != "":
			print(message)
			message = ""

		with open(path, "r") as file:
			contacts = file.read()
			contacts = json.loads(contacts)

			if len(contacts) == 0:
				print("No contact found, please add contact first")
				return
			
			print("Contacts:")
			for i, contact in enumerate(contacts):
				print(f"{i + 1}. {contact['name']} - {contact['number']}")

			contactName = input("Please enter the contact name to remove (or 0 to cancel): ")
			contactName = contactName.strip()
			if contactName == "0":
				return
			
			if contactName == "":
				message = "Contact name cannot be empty"
				continue
			
			# Find the contact to remove
			contactFound = False
			for i, contact in enumerate(contacts):
				if contact["name"].lower() == contactName.lower():
					contactFound = True
					del contacts[i]
					break
			
			if not contactFound:
				message = f"Contact '{contactName}' not found"
				continue

			# Save the updated contacts back to the file
			with open(path, "w") as file:
				file.write(json.dumps(contacts))

			message = f"Contact '{contactName}' has been removed successfully"
			continue
		
