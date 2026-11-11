import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    pd_box.delete(0, tkinter.END)
    pd_box.insert(0, f"{password}")

    pyperclip.copy(password)

# ---------------------------- SEARCH ------------------------------- #

def search():
    website_input = wb_box.get().title()
    try:
        with open("data.json") as file:
                data = json.load(file)
                message = data[website_input]
                messagebox.showinfo(title = website_input, message=f"Website : {website_input}\n"
                                                                   f"Email : {message['email']}\n"
                                                                   f"Password : {message['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No websites found.")
    except KeyError:
        messagebox.showinfo(title="Error", message="No details for the website exist.")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def checker(user_answer):
    with open("data.json") as file:
        data = json.load(file)
        for key in data:
            if user_answer in data:
                prompt = messagebox.askyesno(title=user_answer,
                                            message=f"You have already an account on {user_answer}."
                                            f"\nWould you like change the old account information with new one? ")
                if prompt:
                    return False
                else:
                    return True
            else:
                return False
def save():
    website_input = wb_box.get().title()
    email_input = em_box.get()
    password_input = pd_box.get()
    new_data = {website_input : {
        "email" : email_input,
        "password" : password_input
    }

    }
    if len(website_input) == 0 or len(email_input) == 0 or len(password_input) == 0:
        messagebox.showinfo(title="Oooops", message="Please make sure you haven't left any field empty.")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            if not checker(website_input):
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4),
        finally:
            wb_box.delete(0, tkinter.END)
            pd_box.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager GUI")
window.config(padx=50, pady=50)
canvas = tkinter.Canvas(width=200, height=190)


img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=img)
canvas.grid(column=1, row=0)

#LABELS

website_label = tkinter.Label(text="Website :")
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Username :")
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password :")
password_label.grid(column=0, row=3)

#ENTRY BOXES

wb_box = tkinter.Entry()
wb_box.grid(column=1, row=1, columnspan=1, sticky="EW")
wb_box.focus()

em_box = tkinter.Entry()
em_box.grid(column=1, row=2, columnspan=2, sticky="EW")
em_box.insert(0, "ozgur@gmail.com")

pd_box = tkinter.Entry()
pd_box.grid(column=1, row=3, sticky="EW")

#BUTTONS

gen_button = tkinter.Button(text="Generate Password", command=generator)
gen_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", command=save)
add_button.grid(column=1,row=4, columnspan=2, sticky="EW")

search_button = tkinter.Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
