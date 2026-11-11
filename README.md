# Password Manager GUI

A desktop password manager with a graphical interface, written in Python with Tkinter. It lets you generate strong passwords, save them together with the website and email/username, and look them up later.

## Demo

<!-- Drag and drop 

https://github.com/user-attachments/assets/f9efc7ac-8766-4291-b866-f14028a29588

your demo.mp4 here while editing this file on github.com -->

## Features

- Simple graphical interface built with Tkinter
- Random strong password generator
- Save website, email/username and password entries
- Search for a saved entry by website name
- Data stored locally in a JSON file

## Requirements

- Python 3.8 or newer
- Tkinter (included with the standard Python installers for Windows and macOS)

## Run locally

```bash
git clone https://github.com/jivasnider/Password-Manager-GUI.git
cd Password-Manager-GUI
python main.py
```

On macOS/Linux you may need to use `python3 main.py` instead.

The data file (`data.json`) is created automatically the first time you save a password.

## Project structure

```
Password-Manager-GUI/
├── main.py        # GUI and application logic
├── logo.png       # Logo shown in the window
└── .gitignore     # Keeps personal data files out of the repo
```

## Security note

This is a learning project. Passwords are stored locally in a plain-text JSON file and are **not encrypted**, so don't use it to store real passwords. Your data file is excluded from the repository through `.gitignore`.

## What I learned

- Building a GUI with Tkinter (layout, entries, buttons, message boxes)
- Generating random passwords with Python's `random` module
- Reading and writing JSON files, and handling errors with `try`/`except`
- Keeping sensitive files out of version control with `.gitignore`
