import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Learning coding')
# root.iconbitmap('calculator_ico.ico')

def popup():
    messagebox.askquestion('Information', 'This is a test')

tk.Button(root, text="POPUP", command= popup).pack()


root.mainloop() 