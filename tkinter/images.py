import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title('Learning coding')
root.iconbitmap('calculator_ico.ico')
img = Image.open('tkinter\img.jpg').resize((300,300))

my_img = ImageTk.PhotoImage(img)
my_label = tk.Label(image=my_img)
my_label.pack()



root.mainloop() 