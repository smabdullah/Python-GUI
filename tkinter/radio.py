import tkinter as tk

root = tk.Tk()
root.title('Learning coding')
# root.iconbitmap('calculator_ico.ico')

value = tk.IntVar()
value.set(0)

def choose(num):
    tk.Label(root, text=str(num)).pack()
    value.set(num)

for num in range(10):
    tk.Radiobutton(root, text= f'Option {num}', variable=value, value=num, command= lambda: choose(value.get())).pack(anchor=tk.W)



root.mainloop() 