import tkinter as tk

root = tk.Tk()
root.title('Learning coding')
# root.iconbitmap('calculator_ico.ico')

frame = tk.LabelFrame(root, text="This is a frame", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = tk.Button(frame, text="CLICK HERE").pack()

root.mainloop() 