from tkinter import *
import os

def register():
    main_screen = Tk ()
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    # set text variables
    username = StringVar()
    password = StringVar()

    # set label for user's instructions
    Label(register_screen, text="Please enter details below", bg='orange').pack()
    Label(register_screen, text="").pack()
    
    # set username label
    username_label = Label(register_screen, text="Username * ")
    username_label.pack()

    # set username entry
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    # set a password label
    password_label = Label(register_screen, text="Password * ")
    password_label.pack()

    # set password entry
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    Label(register_screen, text="").pack()

    # set register button
    Button(register_screen, text="Regsiter", width="10", height="1", bg='red').pack()


    # add command=register in button widget
    Button(text="Register", height="2", width="30", command=register).pack()


    # username info and password
    username_info = password.get()
    password_info = password.get()

    # open file in write mode using 'w'
    file = open("username_info.txt", "a")

    # Write username and password information into file
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    # set a label for showing succes information on screen

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
   

    # add command = register

    Button(register_screen, text="Register", width=10, height=1, bg="red", command = register).pack()
register()