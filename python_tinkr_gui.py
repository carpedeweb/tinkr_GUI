
from tkinter import *

def main_account_screen():
    main_screen = Tk()  # creates the GUI window
    main_screen.geometry("300x250") # creates the dimensions for GUI windwo
    main_screen.title("User Login") # sets title of GUI login window

# creating form labeling
    Label(text="Choose to Login or Register", bg="blue", width="300", height="2", font=("Calibri", 12)).pack()
    Label(text="").pack()

# creates the login button
    Button(text="Login", height="2", width="30").pack()
    Label(text="").pack()

# creates the register button
    Button(text="Register", height="2", width="30").pack()


    main_screen.mainloop()  # starts the GUI


    main_account_screen()   # call the main_account_screen()