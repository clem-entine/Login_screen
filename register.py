from tkinter import Button, Entry, Label, StringVar, Toplevel
from tkinter import *

global username
global password
global username_entry
global password_entry

def register():
    register_screen=Tk()
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
# variables
    
    username = StringVar()
    password = StringVar()
 
# user's instruction
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    
# username label
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
 
# username entry
    
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
   
# password label
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    
# password entry
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    
    Label(register_screen, text="").pack()
    
# register button
    Button(register_screen, text="Register", width=10, height=1, bg="blue").pack()

    def new_func():
      global main_screen
 
Button(text="Register", height="2", width="30", command=register).pack()
def register_user():
 
# username and password
    username_info = username.get()
    password_info = password.get()
 
# file in write mode
    file = open(username_info, "w")
 
# username and password information into file
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)    
   
    Label(register_user, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    Button(register_user, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 