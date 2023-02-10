from tkinter import *
from register import *

main_screen=Tk()
main_screen.geometry('100x150')  
main_screen.title('Login Form ')

#Form label
Label(text="Login or Register",bg="hotpink",width="25",height="2",font=("Calibri",13)).pack()


#login button
Button( text="Login", height="2",width="30").pack() 


#register button
Button(text="register", height="2", width="30", command=register).pack()

main_screen.mainloop() 

 

