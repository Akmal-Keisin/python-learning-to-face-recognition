from helper import cli
from colorama import Fore, Style
from tabulate import tabulate
import os
import json

def findContact(load_contacts):
	while True:
		cli.clear()
		print("--FIND CONTACT MENU--")
		print("INPUT 0 TO BACK TO MENU")
		print("Please enter the contact name to find (case insensitive):")

		contacts = load_contacts()
		if len(contacts) == 0:
			print(Fore.RED + "No contacts found." + Style.RESET_ALL)
			print("Returning to menu...")
			return

		contactName = input("Please enter the contact name to find : ")
		contactName = contactName.strip()
		if contactName == "":
			print(Fore.RED + "Contact name cannot be empty." + Style.RESET_ALL)
			print("Returning to menu...")
			return
		
		if contactName == "0":
			return
		
		matches = [c for c in contacts if c.get("name", "").lower() == contactName.lower()]
		if matches:
			print(Fore.GREEN + "Contacts found :" + Style.RESET_ALL)
			print(tabulate(matches, headers="keys", tablefmt="grid"))
		else:
			print(Fore.RED + "No contacts found with that name." + Style.RESET_ALL)

		choice = input("Find another contact? (y/n) ").strip().lower()
		if choice == "n":
			return
		elif choice != "y":
			print(Fore.RED + "Invalid choice, returning to menu..." + Style.RESET_ALL)
			return
		