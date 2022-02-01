from tkinter import *


def clickEventListner():    
    myLabel = Label(root, text="Hello there").pack()
        

root = Tk()

myButton = Button(root, text = "Click me!", command=clickEventListner).pack()

root.mainloop() 