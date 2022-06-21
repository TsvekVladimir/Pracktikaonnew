import tkinter as tk

root = tk.Tk()
root.geometry("600x900+100+100")
root.title('Программа для студентов')

tk.Label(root, text="Login: ").grid(row=0, column=0)
tk.Label(root, text="Password: ").grid(row=1, column=0)

enteruserlogin = tk.Entry(root)
enteruserpassword = tk.Entry(root)
enteruserlogin.grid(row=0, column=1)
enteruserpassword.grid(row=1, column=1)
