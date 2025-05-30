from helper import cli
from tabulate import tabulate
from colorama import Fore, Style
import json
import os

def listContact(load_contacts):
	cli.clear()
	print("--LIST CONTACT MENU--")

	contacts = load_contacts()
	if len(contacts) == 0:
		print(Fore.RED + "No contacts found." + Style.RESET_ALL)
		print("Returning to menu...")
		return

	print(tabulate(contacts, headers="keys", tablefmt="grid"))
	print(Fore.GREEN + "Total contacts: " + str(len(contacts)) + Style.RESET_ALL)
	
	# Check if user want to exit add menu
	choice = input("Input 0 to back to the menu : ")
	if choice.strip() == "0":
		return
	else:
		print(Fore.RED + "Invalid choice, returning to menu..." + Style.RESET_ALL)
		return