import tkinter as tk



root = tk.Tk()

login_entry = tk.Entry(root)
login_entry.grid(row = 0, column = 1)

register_entry = tk.Entry(root)
register_entry.grid(row = 1, column = 1)


root.mainloop()