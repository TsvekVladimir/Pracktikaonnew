from excel import excel
from database import db, sql
from gui import root, enteruserlogin, enteruserpassword
import tkinter as tk
from getuserdata import login
from registration import registration

tk.Button(root, text="Войти",
          command=lambda: login(db, sql, enteruserlogin, enteruserpassword)).grid(row=2, column=0)

tk.Button(root, text="Пройдите регистрацию",
          command=lambda: registration(db, sql, enteruserlogin, enteruserpassword)).grid(row=3, column=0)
excel(sql)
root.mainloop()
