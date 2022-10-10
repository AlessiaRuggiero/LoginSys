import tkinter as tk
from tkinter import messagebox
import pymongo

# Manage database
client = pymongo.MongoClient('mongodb://localhost:27017')
login_db = client["login_db"]
login_credentials = login_db["login_credentials"]


def login():
    if login_credentials.count_documents({
        '$and': [
            {'username': {'$eq': username_entry.get()}},
            {'password': {'$eq': password_entry.get()}}]
    }) > 0:
        messagebox.showinfo(title='Success', message='Successful login.')
    else:
        messagebox.showinfo(title='Error', message='Login error!')


# Window configuration
window = tk.Tk()
window.title("Login Screen")
window.geometry('480x440+500+250')
window.configure(bg='grey10')
frame = tk.Frame(bg='grey10')
frame.pack()

# Widgets creation
login_label = tk.Label(frame, text="Login", bg='grey10', fg='cyan', font=('Cooper Black', 30, 'bold'))
username_label = tk.Label(frame, text="Username:", bg='grey10', fg='cyan', font=('Arial', 15))
username_entry = tk.Entry(frame)
password_label = tk.Label(frame, text="Password:", bg='grey10', fg='cyan', font=('Arial', 15))
password_entry = tk.Entry(frame, show="*")
login_button = tk.Button(frame, text="Login", bg='cyan', fg='grey10', font=('Arial', 15), command=login)

# Widget placement
login_label.grid(row=0, column=3, pady=30)
username_label.grid(row=1, column=2)
username_entry.grid(row=1, column=3, pady=15)
password_label.grid(row=2, column=2)
password_entry.grid(row=2, column=3, pady=15)
login_button.grid(row=3, column=3, pady=30)

window.mainloop()
