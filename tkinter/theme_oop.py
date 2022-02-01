import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super.__init__()

        self.title("Theme Demo")
        self.geometry("600x400")

        label = tk.Label(self, text='Name: ')
        label.grid(column=0, row=0)

        textbox = tk.Entry(self)
        textbox.grid(column=0, row=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()