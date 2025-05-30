import os
import json

from businessLogic.contact_manager_logics import addContactLogic, findContactLogic, listContactLogic, removeContactLogic

class ContactManager:

	def __init__(self):
		# Ensure the storage directory exists
		storage_dir = os.path.join(os.getcwd(), "storage")
		if not os.path.exists(storage_dir):
			os.makedirs(storage_dir)

		# Ensure the contact file exists
		self.contact_file = os.path.join(storage_dir, "contact.json")
		if not os.path.exists(self.contact_file):
			with open(self.contact_file, 'w') as file:
				json.dump([], file)

	def _store_contacts(self, contacts):
		with open(self.contact_file, 'w') as file:
			json.dump(contacts, file, indent=4)

	def _load_contacts(self):
		with open(self.contact_file, 'r') as file:
			return json.load(file)

	def add_contact(self):
		return addContactLogic.addContact(self._load_contacts, self._store_contacts)

	def get_contact(self):
		return listContactLogic.listContact(self._load_contacts)

	def find_contact(self):
		return findContactLogic.findContact(self._load_contacts)

	def remove_contact(self):
		return removeContactLogic.removeContact(self._load_contacts, self._store_contacts)
