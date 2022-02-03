import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('Learning coding')

filename = filedialog.askopenfilename(title="Select a fil")
print(filename)


root.mainloop() 