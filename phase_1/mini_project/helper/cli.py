import os
import platform

def clear():
    """Clears the command-line interface."""
    system = platform.system()
    if system == "Windows":
        os.system('cls')
    elif system == "Linux" or system == "Darwin":
        os.system('clear')
    else:
        print("Operating system not supported to clear CLI.")
