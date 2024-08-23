from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import os,sys
import json
EMAIL = "harishaqimi@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    # can use commented below or just list comprehension above
    # password_list = []
    #
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    # random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")
    pass_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo("Error", "Please enter all fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)
                web_entry.focus()
# ------------------------- FIND PASSWORD -------------------------- #
def find_password():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data Files Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(website, f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo("Error", f"No Details for {website} exist")

# ---------------------------- UI SETUP ------------------------------- #
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)
window_icon = PhotoImage(file=resource_path("logo.png"))
window.iconphoto(False, window_icon)

canvas = Canvas(window, width=200, height=200)
logo_img = PhotoImage(file=resource_path("logo.png"))
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(window, text="Website :")
website_label.grid(column=0, row=1, sticky=W)

email_label = Label(window, text="Email/Username :")
email_label.grid(column=0, row=2, sticky=W)

pass_label = Label(window, text="Password :")
pass_label.grid(column=0, row=3, sticky=W)

web_entry= ttk.Entry(window, width=35)
web_entry.grid(column=1, row=1,sticky=EW)
web_entry.focus()

email_entry= ttk.Entry(window, width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky=EW)
email_entry.insert(0, EMAIL)

pass_entry= ttk.Entry(window, width=21)
pass_entry.grid(column=1, row=3, sticky=EW)

gen_button = ttk.Button(window, text="Generate Password", command=generate_password)
gen_button.grid(column=2, row=3, sticky=EW)

search_button = ttk.Button(window, text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky=EW)

add_button = ttk.Button(window, text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW)

window.mainloop()