
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ("Times News Roman", 10, "bold")
# ---------------------------------- PASSWORD GENERATOR ---------------------------------


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbol + password_numbers

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password_generated = "".join(password_list)
    password_entry.insert(0, password_generated)

    # to be able to copy it
    pyperclip.copy(password_generated)
# ---------------------------------- SAVE PASSWORD ---------------------------------


def save():
    website_input = website_entry.get().title()
    email_input = email_user_entry.get()
    password_input = password_entry.get()
    new_data = {
        website_input: {
            "email": email_input,
            "password": password_input

        }
    }

    if len(website_input) == 0 and len(password_input) == 0:
        messagebox.showerror(title="Missing Website", message="Please make sure you have not left any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving the updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------------- FIND PASSWORD ---------------------------------

def find_password():
    web = website_entry.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No such file found")
    else:
        if web in data:
            email = data[web]["email"]
            password_key = data[web]["password"]
            messagebox.showinfo(title=web, message=f"email: {email}\nPassword: {password_key}")
        else:
            messagebox.showerror(title="Not Available", message=f"The website '{web}' does not exist")

# ---------------------------------- UI SETUP ---------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# put image
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo2.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# website label
website = Label(text="Website: ", font=FONT)
website.grid(row=1, column=0)

# email/username label
email_user = Label(text="Email/Username: ", font=FONT)
email_user.grid(row=2, column=0)

# password label
password = Label(text="Password: ", font=FONT)
password.grid(row=3, column=0)

# website_entry
website_entry = Entry(width=36)
website_entry.focus()
website_entry.grid(row=1, column=1)

# email/username entry
email_user_entry = Entry(width=55)
email_user_entry.insert(0, "oliviaakabs@gmail.com")
email_user_entry.grid(row=2, column=1, columnspan=2)

# password entry
password_entry = Entry(width=36)
password_entry.grid(row=3, column=1)

# password generate button
generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2)

# add password button
add_password = Button(text="Add", width=46, command=save)
add_password.grid(row=4, column=1, columnspan=2)

# search button
search = Button(text="Search", width=13, command=find_password)
search.grid(row=1, column=2)

# website_input = website_entry.get()
# email_input = email_user_entry.get()
# password_input = password_entry.get()
window.mainloop()