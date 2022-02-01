import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
data = tk.StringVar()

e = tk.Entry(root, textvariable=data)
e.insert(0, "Name: ")
e.bind("<FocusIn>", lambda args: e.delete(0, "end"))
e.bind("<FocusOut>", lambda args: e.insert(0, "Name: "))
e.pack()

def clickEventListner():    
    myLabel = tk.Label(root, text=data.get()).pack()

myButton = tk.Button(root, text = "Click me!", command=clickEventListner).pack()

root.mainloop() 