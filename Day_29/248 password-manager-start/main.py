import tkinter
from tkinter import messagebox
import sqlite3
from db import *
from random import randint, choice, shuffle
import pyperclip

init()

RED = "#e7305b"
GREEN = "#006400"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generator_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    let = [choice(letters) for char in range(randint(8, 10))]
    sym = [choice(symbols) for char in range(randint(2, 4))]
    num = [choice(numbers) for char in range(randint(2, 4))]
    password_list = let + sym + num

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, string=f"{password}")
    pyperclip.copy(password)

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website and email and password:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nEmail: {email}\nPassword \
                                {password}\nIs it ok to save?")
        if is_ok:
            add_password(website_entry.get(), email_entry.get(), password_entry.get())
            feetback_label.config(text="Пароль\nдобавлен", fg=GREEN)
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
    else:
        feetback_label.config(text="Данные\nне заполнены", fg=RED)
        messagebox.showwarning(title="Данные не заполнены", message="Заполните все данные")


def show_password():
    with sqlite3.connect("passwords.db", check_same_thread=False) as conn:
        cursor = conn.cursor()
        all_passwords = list(cursor.execute("SELECT * FROM passwords"))
        for p in all_passwords:
            print(p)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=30)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
feetback_label = tkinter.Label(text="Заполните поля", fg=GREEN)
feetback_label.grid(column=0, row=0)
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)
# Entries
website_entry = tkinter.Entry(width=50)
website_entry.insert(1, string="")
website_entry.grid(column=1, row=1, columnspan=2, pady=2)
website_entry.focus()
email_entry = tkinter.Entry(width=50)
email_entry.insert(0, string="viktorbezai@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, pady=2)
password_entry = tkinter.Entry(width=32)
password_entry.insert(0, string="")
password_entry.grid(column=1, row=3, columnspan=1, pady=2)
# Buttons
generate_button = tkinter.Button(text="Generate Password", highlightthickness=0, command=generator_password)
generate_button.grid(column=2, row=3, columnspan=1, pady=2)
add_button = tkinter.Button(text="Add", highlightthickness=0, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, ipadx=139, pady=5)
show_button = tkinter.Button(text="Show passwords", highlightthickness=0, command=show_password)
show_button.grid(column=1, row=5, columnspan=2, ipadx=107, pady=5)

window.mainloop()
