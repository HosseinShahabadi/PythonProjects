from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
from PasswordGenerator import PasswordGenerator
import os, pyperclip

DEFAULT_USERNAME = None # Default username; change this to customize the default user experience.

# ---------------------------- CRYPTOGRAPHY ---------------------------- #
# Function to generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    load_key()

# Function to load the key
def load_key():
    global key, cipher
    key = open("secret.key", "rb").read()

    # Create the Fernet cipher object
    cipher = Fernet(key)

# Function to encrypt a message
def encrypt_message() -> str:
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    if website == '' or email == '' or password == '':
        messagebox.showinfo(title='Oops!', message='Please ensure that all required fields are filled out.')
        return
    
    is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\n'
                                                  f'Email/Username: {email}\nPassword: {password}\nIs it correct?')
    if not is_ok:
        return

    with open('data.txt') as file:
        encrypted_data = file.read()
    if encrypted_data:
        data = decrypt_message(encrypted_data)
    else:
        data = ''
    data += (website + ', ' + email + ', ' + password + '\n')
    encoded_message = data.encode()
    encrypted_message = cipher.encrypt(encoded_message)
    with open('data.txt', mode='w') as file:
        file.write(encrypted_message.decode())
    entry_website.delete(0, END)
    entry_password.delete(0, END)

# Function to decrypt a message
def decrypt_message(encrypted_message: str=None) -> str:
    if encrypted_message == None:
        with open('data.txt') as file:
            data = file.read()
            if data:
                print(decrypt_message(data))
    else:
        encrypted_message = encrypted_message.encode()
        decrypted_message = cipher.decrypt(encrypted_message)
        return decrypted_message.decode()

if not os.path.exists("data.txt"):
    with open('data.txt', mode='w') as file:
        file.write('')
if not os.path.exists("secret.key"):
    print("Key file not found. Generating a new key...")
    generate_key()

load_key()

# ---------------------------- PASSWORD GENERATOR ---------------------- #
def generatePassword():
    password = PasswordGenerator.generatePassword()
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title('PyPassword Manager')
window.config(padx=50, pady=50)
window.resizable(0, 0)

img = PhotoImage(file='password.png')
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1, pady=20)

# Labels
label_website = Label(text='Website:', anchor='e', width=20)
label_website.grid(row=1, column=0)
label_email = Label(text='Email/Username:', anchor='e', width=20)
label_email.grid(row=2, column=0)
label_password = Label(text='Password:', anchor='e', width=20)
label_password.grid(row=3, column=0)

# Entries
entry_website = Entry(width=51)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()
entry_email = Entry(width=51)
entry_email.grid(row=2, column=1, columnspan=2)
if DEFAULT_USERNAME:
    entry_email.insert(0, DEFAULT_USERNAME)
entry_password = Entry(width=32)
entry_password.grid(row=3, column=1)

# Buttons
btn_generatepassword = Button(text='Generate Password', width=14, padx=2, command=generatePassword)
btn_generatepassword.grid(row=3, column=2)
btn_add = Button(text='Add', width=42, padx=5, command=encrypt_message)
btn_add.grid(row=4, column=1, columnspan=2)
btn_readdata = Button(text='Read Data', width=42, padx=5, command=decrypt_message)
btn_readdata.grid(row=5, column=1, columnspan=2)


window.mainloop()
