from cgitb import text
from distutils.cmd import Command
from email import message
from importlib.resources import path
from secrets import choice
from tkinter import *
from tkinter import messagebox, filedialog
from numpy import size
from pygame import mixer
from email.message import EmailMessage
from tkinter import font
from tkinter.font import BOLD
from unicodedata import name
import smtplib
import os
import imghdr
import pandas


def myEmail():
    with open("credentials.txt", "r") as m:
        credentialData = m.readline()


def textData():
    with open("message.txt", "r") as n:
        messageData = n.read()

def myPassword():
    with open("credentials.txt", "r") as o:
        data = o.readlines()

def vicEmail():
    with open("victimEmail.txt", "r") as p:
        vic = p.readline()

    
def bomb():
    if (credentialWindow or victimWindow or textWindow) == "":
        messagebox.showerror(("Error", "Fill The Whole Form!!"), parent=screen)
    
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()


        smtp.login('myEmail', 'myPassword')
        

        msg = f"Subject:  {textData}\n"
        smtp.sendmail(myEmail, vicEmail, msg) 














def textWindow():
    def clear3():
        subjectEntryField.delete(0, END)
        textArea.delete(1.0, END)

    def save3():
        if len(subjectEntryField.get()) == 0  or textArea.get("1.0",'end-1c') == "0":
            messagebox.showerror("Error", "Fill The Spaces", parent= windowThree)
        
        else:
            c = open("message.txt", "w")
            c.write("\t\t\t\t\t"+ subjectEntryField.get()+"\n"+ textArea.get(1.0, END))
            c.close()
            message1 = messagebox.showinfo("Information", "Message Typed Succesfully", parent=windowThree)
            c.close()
            windowThree.destroy()
            
            


    windowThree = Toplevel()
    windowThree.title("Text Box")
    windowThree. geometry('700x450+350+90')
    windowThree.config(bg="dodger blue2")
    windowThree.resizable(False, False)


   

    subjectLabelFrame=LabelFrame(windowThree,text='Subject',font=('times new roman',16,'bold'),bd=5,fg='white',bg='dodger blue2')
    subjectLabelFrame.grid(row=2,column=200,padx=10,pady=5)

    subjectEntryField=Entry(subjectLabelFrame,font=('times new roman',18,'bold'),width=30)
    subjectEntryField.grid(row=0,column=0)

    emailLabelFrame=LabelFrame(windowThree,text='Compose Email',font=('times new roman',16,'bold'),bd=5,fg='white',bg='dodger blue2')
    emailLabelFrame.grid(row=20,column=200,padx=20, pady=10)
    
    textArea=Text(emailLabelFrame,font=('times new roman',14,),height=10, width=71)
    textArea.grid(row=1,column=2,padx=2, pady=1)


   

    


    clearButton2 = Button(windowThree, text="CLEAR", bd=2, bg='Maroon', cursor='hand2',activebackground='dodger blue2', 
                    font=("bold", 14), command=clear3).place(x=120, y=350)
    
    doneButton2 = Button(windowThree, text="DONE", bd=2, bg='dark green', cursor='hand2',activebackground='dodger blue2', 
                    font=("bold", 14), command=save3).place(x=430, y=350, )
    
    
    



    



    windowThree.mainloop()








#screen design
screen=Tk()
screen.title("EMAIL SENDER APP")
canvas = Canvas(screen, width=450, height=450)

#window cannot be resized
screen.resizable(0, 0)

#background image and layout
filename = PhotoImage(file = "background.png")
backgroundImage = Label(screen, image=filename)
backgroundImage.place(x=0, y=0, relwidth=1, relheight=1)

#title
titleName = Label(screen, text="EMAIL BOMBER BY\n[KRAEON] ", background="light sea green", font=("Century SchoolBook L", 30, BOLD))
canvas.create_window(227, 50, window=titleName)
canvas.pack()





def credentialWindow():
    def clear1():
        emailField.delete(0, END)
        passwordField.delete(0, END)

    def save1():
        if emailField.get() == "" or passwordField.get() == "":
            messagebox.showerror("Error", "All Fields are Required!", parent=windowOne)
        
        else:
            b = open("credentials.txt", "w")
            b.write(emailField.get()+" | "+ passwordField.get())
            b.close()
            messagebox.showinfo("Information", "Inputted Succesfully", parent=windowOne)
            b.close()
            windowOne.destroy()


    windowOne = Tk()
    windowOne.title("YOUR DETAILS")
    layout = Canvas(windowOne, width=450, height=200)
    layout.config(background="#134943")
    
    #adding the type label for the email
    emailLabel = Label(windowOne, text="Your Email:", background="#134943")

    #adding the type field for the email
    emailField = Entry(windowOne, width=50)

    #adding the type label for the password
    passwordLabel = Label(windowOne, text="Your Password:", background="#134943")

    #adding the type field for the password
    passwordField = Entry(windowOne, width=50, show="*")
    
    #adding both email label and field to the screen
    layout.create_window(60, 20, window=emailLabel)
    layout.create_window(240, 40, window=emailField)

    #adding both password label and field to the screen
    layout.create_window(71, 80, window=passwordLabel)
    layout.create_window(240, 100, window=passwordField)



    #adding the DONE button
    doneButton = Button(windowOne, text="DONE ", background='sea green', font=("Liberation"), command=save1)
    layout.create_window(300, 170, window=doneButton)

    #adding the CLEAR button
    clearButton1 = Button(windowOne, text="CLEAR", background='red', font=("BOLD"), command=clear1)
    layout.create_window(180, 170, window=clearButton1)
    
    windowOne.config(background="#980900")
    windowOne.resizable(False, False)


    
    layout.pack()



    
    

    


def victimWindow():
    def clear2():
        victEmailField.delete(0, END)

    def save2():
        if victEmailField.get() == "" and " ":
            messagebox.showerror("Error", "All Fields are Required!", parent=windowTwo)
        else:
            a = open("victimEmail.txt", "w")
            a.write(victEmailField.get())
            a.close()
            messagebox.showinfo("Information", "Victim Email Inputed Succesfully", parent=windowTwo)
            a.close()
            windowTwo.destroy()


    windowTwo = Tk()
    windowTwo.title("VICTIM EMAIL")
    display = Canvas(windowTwo, width=380, height=180)
    display.config(background="#134943")
    display.pack()

    #adding the email label
    victEmailLabel = Label(windowTwo, text="Victim Email:", background="#134943")
    display.create_window(60, 20, window=victEmailLabel)

    #adding the email field
    victEmailField = Entry(windowTwo, width=50)
    display.create_window(180, 50, window=victEmailField)
    
    #adding the DONE button
    doneButton1 = Button(windowTwo, text="DONE ", background='sea green', font=("Liberation"), command=save2)
    display.create_window(280, 130, window=doneButton1)

    #adding the CLEAR button
    clearButton1 = Button(windowTwo, text="CLEAR", background='red', font=("BOLD"), command=clear2)
    display.create_window(90, 130, window=clearButton1)


    windowTwo.resizable(False, False)
    display.pack()
    
    

def exit():
    result = messagebox.askyesno("Notification", "DO YOU WANT TO QUIT THE APPLICATION?")
    if result:
        screen.destroy()
    else:
        pass

yourCredential = Button(screen, text="ENTER YOUR CREDENTIALS", background='sea green', font=("Liberation",), command=credentialWindow)
canvas.create_window(230, 150, window=yourCredential)


victimEmail = Button(text="ENTER VICTIM'S EMAIL", background='sea green', font=("Liberation"), command=victimWindow)
canvas.create_window(230, 230, window=victimEmail)


textBox = Button(text="CLICK TO IMPORT TEXT", background='sea green', font=("Liberation"), command=textWindow)
canvas.create_window(230, 300, window=textBox)






#adding the SEND button on mainpage
sendButton = Button(screen, text="BOMB!", background='RED',font=("Liberation"), command=bomb)
canvas.create_window(380, 400, window=sendButton)

#adding the EXIT button on mainpage
exitButton = Button(screen, text="EXIT", background='RED', font=("Liberation"), command=exit)
canvas.create_window(80, 400, window=exitButton)




canvas.pack()








 














screen.mainloop()