from tkinter import Tk, Label, Entry, Button, StringVar

def tinkr():

    window = Tk()
    window.geometry("300x250")
    window.title("Account Login")

    l1=Label(window, text="Username:").pack()
    l1_entry=Entry(window, show="", textvariable=StringVar()).pack()
    l2=Label(window, text='Password:').pack()
    t1=Entry(window, show='*', textvariable=StringVar()).pack()
    b1=Button(window, text="Login").pack()

    window.mainloop()
tinkr()
    
