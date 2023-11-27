import sqlite3
from tkinter import Tk, Button, Entry, Label, StringVar, messagebox

# Создание базы данных SQLite
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   phone TEXT,
                   email TEXT)''')

# Функции основного функционала
def view_contacts():
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    for contact in contacts:
        print(contact)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    cursor.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))
    conn.commit()
    messagebox.showinfo("Success", "Contact added successfully")

def search_contact():
    name = name_entry.get()
    cursor.execute('SELECT * FROM contacts WHERE name LIKE ?', ('%' + name + '%',))
    contacts = cursor.fetchall()
    for contact in contacts:
        print(contact)

def delete_contact():
    name = name_entry.get()
    cursor.execute('DELETE FROM contacts WHERE name = ?', (name,))
    conn.commit()
    messagebox.showinfo("Success", "Contact deleted successfully")

# Создание графического интерфейса пользователя
root = Tk()
root.title("Phonebook")

name_label = Label(root, text="Name")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

phone_label = Label(root, text="Phone")
phone_label.pack()
phone_entry = Entry(root)
phone_entry.pack()

email_label = Label(root, text="Email")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

view_button = Button(root, text="View Contacts", command=view_contacts)
view_button.pack()

add_button = Button(root, text="Add Contact", command=add_contact)
add_button.pack()

search_button = Button(root, text="Search Contact", command=search_contact)
search_button.pack()

delete_button = Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

root.mainloop()