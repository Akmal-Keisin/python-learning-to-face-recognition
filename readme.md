# Python learning journey toward face reecognition

Hi, this is my learning journey to learning python in order to make a face recognition app. The goals of this journey is make me able to at least make a simple project that implement face comparison. The goals will be indicated as succeed if I'm able to compare two photo of my face and determine it if it's a same person or not.

Here's my learning plan. I made a directory for each phase, each phase including everything that I learn and probably contains a little project to test out my learning.


| Phase   | Hours     | Focus & Achievements                                                 |
| ------- | --------- | -------------------------------------------------------------------- |
| Phase 1 | 0–8 hrs   | Python Setup, Syntax Basics, Variables, Data Types, Functions, Files |
| Phase 2 | 8–18 hrs  | OOP, Modules, Import/Export, pip, Virtual Envs, Third-Party Libs     |
| Phase 3 | 18–28 hrs | NumPy & OpenCV Basics + Working with Images                          |
| Phase 4 | 28–38 hrs | Face Detection with OpenCV, Real-time Camera Input                   |
| Phase 5 | 38–48 hrs | Final Project: Face Recognition App (with GUI or CLI)                |


Here's the breakdown of each phase that I have already done

## 🟢 Phase 1: Python Setup, Syntax Basics, Variables, Data Types, Functions, Files
✅ Installed Python & VSCode (or equivalent) <br>
✅ Learned how to run .py files <br>
✅ Learned Python syntax for: <br>
- Variables, strings, numbers, booleans
- Lists, tuples, dictionaries
- Loops (for, while)
- Conditionals (if, elif, else)
- Basic function definitions
- File I/O (JSON)
✅ Created a mini CRUD project (Contact Management) with JSON storage

## 🟢 Phase 2: OOP, Modules, Import/Export, pip, Virtual Envs, Third-Party Libs
✅ Learned about oop (defining class, create an object, inharitance, encapsulation, polymorphism) <br>
✅ Learned about modules <br>
✅ Learned about virtual environment & pip <br>
- Create virtual environment `python -m venv venv`
- Activate virtual environment in windows `venv\Scripts\activate` and for linux/mac `source venv/bin/activate`
- Install packages from in virtual environment `pip install colorama tabulate`
- Snapshot the installed package to requirements.txt `pip freeze > requirements.txt`
✅ Update mini CRUD project (Contact Management) with OOP paradigm

## Phase 3: Working With Images
✅ Learned about simple opencv-python image operation
- Resize image
- Store image
- Crop image
- Draw on image
- Show image
✅ Created mini project watermarking image