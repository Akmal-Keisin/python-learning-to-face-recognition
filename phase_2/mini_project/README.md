# Mini CRUD Contact Management Project

This is a simple command-line CRUD (Create, Read, Update, Delete) application for managing contacts, built as part of a Python learning journey. It demonstrates basic Python concepts, file I/O with JSON, and modular code organization.

## Features
- Add a new contact
- List all contacts
- Find a contact by name
- Remove a contact
- Data is stored in a JSON file for persistence

## Project Structure
```
mini-project/
  main.py                # Entry point for the CLI app
  businessLogic/         # Business logic for CRUD operations
    addContactLogic.py
    findContactLogic.py
    listContactLogic.py
    removeContactLogic.py
  helper/                # CLI helper functions
    cli.py
  storage/               # JSON storage for contacts
    contact.json
```

## How to Run

1. Open a terminal and navigate to this directory:
   ```powershell
   cd phase_1/mini-project
   ```
2. Run the application:
   ```powershell
   python main.py
   ```

## Requirements
- Python 3.10 or higher
- No external dependencies required

## Notes
- All contact data is saved in `storage/contact.json`.
- The code is modular for easier learning and maintenance.

---
Feel free to explore, modify, and use this project as a learning resource!
