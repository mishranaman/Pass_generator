#importing Library
from tkinter import *
import random, string
import pyperclip

#Initializing Window 

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Passwords by Naman")

#Creating Tittles
Label(root, text = 'Generate New Password' , font ='Helvetica 15 bold').pack()
Label(root, text ='Made by Naman', font ='Times 15').pack(side = BOTTOM)


#Choose Length
pass_label = Label(root, text = 'Choose length of password', font = 'Helvetica 10').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()

#The core function to generate password
pass_str = StringVar()

def Generator():
    password = ''

    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+ random.choice(string.punctuation) + random.choice(string.ascii_lowercase) + random.choice(string.digits) 
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

#Button for generating password
Button(root, text = "Generate the Password" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()

#function for copying the generating password
def Copy_password():
    pyperclip.copy(pass_str.get())

#button to copy password
Button(root, text = 'Copy', command = Copy_password).pack(pady=5)

#loop for running program
root.mainloop()