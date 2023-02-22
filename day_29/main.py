import random
import json
from string import ascii_letters, digits, punctuation

from tkinter import Label
from tkinter import Button
from tkinter import Tk
from tkinter import Entry
from tkinter import PhotoImage
from tkinter import Canvas
from tkinter import messagebox
from tkinter import END

WAY_TO_EMAIL = "D://100_days_of_code//day_29//email.txt"
WAY_TO_PHOTO = "D://100_days_of_code//day_29//logo.png"
WAY_TO_JSON = "D://100_days_of_code//day_29//data.json"
WHITE = 'white'
FONT = ("Courier", 10, 'bold')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    my_password = []
    my_password += [random.choice(ascii_letters) for _ in range(8)]
    my_password += [random.choice(digits) for _ in range(4)]
    my_password += [random.choice(punctuation) for _ in range(2)]
    random.shuffle(my_password)

    password_entry.insert(0, "".join(my_password))


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    webiste = website_entry.get().title()
    email = username_entry.get()
    password = password_entry.get()

    d = {
        'email': email,
        'password': password
    }
    new_data = {}
    new_data[webiste] = d

    if webiste == "" or password == "":
        messagebox.askokcancel(
            title="Are you sure",
            message="You didn't write website or password"
        )
    else:
        try:     
            with open(WAY_TO_JSON, "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open(WAY_TO_JSON, "w") as data_file:
                # Updating old data with new data
                json.dump(new_data, data_file)
        else:
            data.update(new_data)
            
            with open(WAY_TO_JSON, "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# --------------------------- SEARCH ----------------------------------#
def search():
    webiste = website_entry.get().title()
    email = username_entry.get()
    # No data file found
    try:
        with open(WAY_TO_JSON, 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.askokcancel(
            title='Error',
            message="File not found error"
        )
    else:
        if webiste in data.keys():
            if email in data[webiste].values():
                messagebox.askokcancel(
                    title=webiste,
                    message=f"Your password is {data[webiste]['password']}"
                )
        else:
            messagebox.askokcancel(
                title=webiste,
                message=f"There are no details for {webiste} exists."
            )

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20, bg='white')
window.minsize(width=400, height=400)

canvas = Canvas(
    width=250,
    height=250,
    bg=WHITE,
    highlightthickness=0
)

logo_png = PhotoImage(file=WAY_TO_PHOTO)
canvas.create_image(125, 100, image=logo_png)
canvas.grid(column=1, row=0)

# LABEL
website_label = Label(text="Website", bg=WHITE, font=FONT)
website_label.grid(column=0, row=1)

user_name_label = Label(text="Email/Username", bg=WHITE, font=FONT)
user_name_label.grid(column=0, row=2)

password_label = Label(text="Password", bg=WHITE, font=FONT)
password_label.grid(column=0, row=3)

# ENTRY
website_entry = Entry(highlightthickness=2, width=31)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(highlightthickness=2, width=50)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, 'asilbek02@gmail.com')

password_entry = Entry(highlightthickness=2, width=31)
password_entry.grid(column=1, row=3)


# BUTTON
generate_password_button = Button(text="Generate password", width=15, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=42, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)
window.mainloop()

