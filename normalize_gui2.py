from tkinter import *

root = Tk()
root.title("ugurun dünyasi")

T = Text(root, height=10, width=70,bg="lightpink").pack()
def callback():
    
    print("Cliccck!!!")
    

mButton = Button(root,text="Normalize", fg='white',bg='green',command=callback).pack()

T2 = Text(root, height=10, width=70,bg="lightgreen").pack()


ment=StringVar() 




#T.insert(END, quote)

mainloop()