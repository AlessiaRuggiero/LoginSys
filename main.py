import tkinter as tk
from tkinter import messagebox
import pymongo

# Manage database --------------------------------------------------------------
client = pymongo.MongoClient('mongodb://localhost:27017')
login_db = client["login_db"]
login_credentials = login_db["login_credentials"]


def login():
    hide_open_frames()
    login_frame.pack()

    # Check Database for login credentials ------------------------------------
    def access_login():
        if login_exists(username_entry.get(), password_entry.get()):
            login_success = tk.Label(login_frame, text='Successful login!', bg='grey10', fg='green2',
                                     font=('Cooper Black', 15, 'bold'))
            login_success.grid(row=5, column=0, columnspan=2, pady=30)
            login_success.after(2000, root.destroy)
        else:
            login_error = tk.Label(login_frame, text='Incorrect login.', bg='grey10', fg='red',
                                   font=('Cooper Black', 15, 'bold'))
            login_error.grid(row=5, column=0, columnspan=2, pady=30)
            login_error.after(1000, login)

    # Widget creation ----------------------------------------------------------
    login_label = tk.Label(login_frame, text="Login", bg='grey10', fg='cyan', font=('Cooper Black', 30, 'bold'))
    username_label = tk.Label(login_frame, text="Username:", bg='grey10', fg='cyan', font=('Cooper Black', 15))
    username_entry = tk.Entry(login_frame)
    password_label = tk.Label(login_frame, text="Password:", bg='grey10', fg='cyan', font=('Cooper Black', 15))
    password_entry = tk.Entry(login_frame, show="*")
    login_button = tk.Button(login_frame, text="Login", bg='cyan', fg='grey10', font=('Cooper Black', 15),
                             command=access_login)
    register_button = tk.Button(login_frame, text="Don't have an account? Create one.",
                                bg='cyan', fg='grey10', font=('Cooper Black', 10), command=login_registration)

    # Widget placement ---------------------------------------------------------
    login_label.grid(row=0, column=0, columnspan=2, pady=30)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=15)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=15)
    login_button.grid(row=3, column=0, columnspan=2, pady=15)
    register_button.grid(row=4, column=0, columnspan=2)


def login_registration():
    hide_open_frames()
    login_registration_frame.pack()

    # Update database ----------------------------------------------------------
    def register_login():
        # Collect new_login information
        new_login = {'username': new_username_entry.get(), 'password': new_password_entry.get()}

        # Check that new_login does not already exist in the database
        if login_exists(new_login['username'], new_login['password']):
            already_exists_err = tk.Label(login_registration_frame, text='Account already exists.', bg='grey10',
                                          fg='red', font=('Cooper Black', 15, 'bold'))
            already_exists_err.grid(row=4, column=0, columnspan=2, pady=30)
            already_exists_err.after(2000, login_registration)
        else:
            login_db.login_credentials.insert_one(new_login)
            # Check that new_login has been added to the database
            if login_exists(new_login['username'], new_login['password']):
                confirmation_msg = tk.Label(login_registration_frame, text='Account creation successful!', bg='grey10',
                                            fg='green2', font=('Cooper Black', 15, 'bold'))
                confirmation_msg.grid(row=4, column=0, columnspan=2, pady=30)
                confirmation_msg.after(2000, login)

    # Widget creation ----------------------------------------------------------
    login_registration_label = tk.Label(login_registration_frame, text="Account Registration", bg='grey10', fg='cyan',
                                        font=('Cooper Black', 30, 'bold'))
    new_username_label = tk.Label(login_registration_frame, text="Create a username:", bg='grey10', fg='cyan',
                                  font=('Cooper Black', 15))
    new_username_entry = tk.Entry(login_registration_frame)
    new_password_label = tk.Label(login_registration_frame, text="Create a password:", bg='grey10', fg='cyan',
                                  font=('Cooper Black', 15))
    new_password_entry = tk.Entry(login_registration_frame, show="*")
    register_button = tk.Button(login_registration_frame, text="Register", bg='cyan', fg='grey10',
                                font=('Cooper Black', 15), command=register_login)
    login_button = tk.Button(login_registration_frame, text="Already have an account? Login.", bg='cyan', fg='grey10',
                             font=('Cooper Black', 10), command=login)

    # Widget placement ---------------------------------------------------------
    login_registration_label.grid(row=0, column=0, columnspan=2, pady=30)
    new_username_label.grid(row=1, column=0)
    new_username_entry.grid(row=1, column=1, pady=15)
    new_password_label.grid(row=2, column=0)
    new_password_entry.grid(row=2, column=1, pady=15)
    register_button.grid(row=3, column=0, columnspan=2, pady=15)
    login_button.grid(row=4, column=0, columnspan=2)


def hide_open_frames():
    for widget in login_frame.winfo_children():
        widget.destroy()
    login_frame.pack_forget()

    for widget in login_registration_frame.winfo_children():
        widget.destroy()
    login_registration_frame.pack_forget()


def login_exists(usn_entry, pwd_entry):
    if login_credentials.count_documents({
        '$and': [
            {'username': {'$eq': usn_entry}},
            {'password': {'$eq': pwd_entry}}]
    }) > 0:
        return True
    else:
        return False


# Window configuration ---------------------------------------------------------
root = tk.Tk()
root.title("Login Screen")
root.geometry('480x440+500+250')
root.configure(bg='grey10')

# Frames -----------------------------------------------------------------------
login_frame = tk.Frame(root, bg='grey10')
login_registration_frame = tk.Frame(root, bg='grey10')

login()

root.mainloop()
