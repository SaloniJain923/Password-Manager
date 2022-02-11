from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def search():
    website = website_entry.get().title()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No such data file exists.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exits.")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    numbers_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = letters_list + numbers_list + symbols_list
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def add_data():
    website = website_entry.get().title()
    email = id_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }
    if website_entry.get() == "" or password_entry.get() == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        ok = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered: \n"
                                                                            f"Email: {email}"
                                                                            f"\nPassword: {password}"
                                                                            f"\nIs it ok to save?")

        if ok:
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=300, height=300)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=49)
website_entry.grid(column=1, row=1)
website_entry.focus()

id_label = Label(text="Email/Username:")
id_label.grid(column=0, row=2)
id_entry = Entry(width=68)
id_entry.grid(column=1, row=2, columnspan=2)
id_entry.insert(0, "xyz@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=49)
password_entry.grid(column=1, row=3)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=58, command=add_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
