'''
Created on Apr 2, 2016

@author: ugur
'''
import sys  
from tkinter import *


myGUI = Tk()

myGUI.geometry('450x450+500+300')
myGUI.title("ugurun dünyasi")


mylabel=Label(text='My Label',fg='red',bg='yellow').pack()


def mHello():
    #mtext=ment.get()
    mtext= ment.get() + " Aslıhan'ı seviyor <3"
    # mlabel1=Label(myGUI,text=mtext).pack()
    text=mtext
    T = Text(myGUI, height=4, width=50,bg="lightpink").pack()
    T.insert(END,text)
   
    return

ment=StringVar()
  
mButton = Button(text="Normalize", command=mHello, fg='white',bg='green').pack()

mEntry= Entry(myGUI,textvariable=ment).pack()



myGUI.mainloop()