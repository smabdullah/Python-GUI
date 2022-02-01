import tkinter as tk

root = tk.Tk()
root.title('Simple Calculator')
one = tk.StringVar()

e = tk.Entry(root, width=50, borderwidth=3)
e.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

def button_click(arg):
    current = e.get() + arg
    e.delete(0, "end")
    e.insert(0, current)

def button_clear():
    e.delete(0, "end")

def button_operation(icon, operation):
    global op
    op = operation
    if op == 'div':
        first_arg = float(e.get())
    else:
        first_arg = int(e.get())
    e.delete(0, "end")
    e.insert(0, str(first_arg) + icon)

def button_equal():
    if op == 'add':
        args = e.get().split('+')
        res = int(args[0].strip()) + int(args[1].strip())
    elif op == 'sub':
        args = e.get().split('-')
        res = int(args[0].strip()) - int(args[1].strip())
    elif op == 'mul':
        args = e.get().split('*')
        res = int(args[0].strip()) * int(args[1].strip())
    elif op == 'div':
        args = e.get().split('/')
        res = float(args[0].strip()) / float(args[1].strip())
    e.delete(0, "end")
    e.insert(0, str(res))
    


# buttons = []
# for num in range(10):
#     buttons.append(tk.Button(root, text=str(num), padx=40, pady=20, command=lambda: button_click(str(num))))

button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click('1'))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click('2'))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click('3'))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click('4'))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click('5'))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click('6'))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click('7'))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click('8'))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click('9'))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click('0'))
button_add = tk.Button(root, text="+", padx=39, pady=20, command=lambda: button_operation(' + ', 'add'))
button_equal = tk.Button(root, text="=", padx=92, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=83, pady=20, command=button_clear)
button_sub = tk.Button(root, text="-", padx=40, pady=20, command=lambda: button_operation(' - ', 'sub'))
button_mul = tk.Button(root, text="*", padx=39, pady=20, command=lambda: button_operation(' * ', 'mul'))
button_div = tk.Button(root, text="/", padx=39, pady=20, command=lambda: button_operation(' / ', 'div'))

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)

root.mainloop() 