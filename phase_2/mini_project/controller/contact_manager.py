import os
import json

from businessLogic.contact_manager_logics import addContactLogic, findContactLogic, listContactLogic, removeContactLogic

class ContactManager:
	def add_contact(self):
		return addContactLogic.addContact()

	def get_contact(self):
		return listContactLogic.listContact()

	def find_contact(self):
		return findContactLogic.findContact()

	def remove_contact(self):
		return removeContactLogic.removeContact()
