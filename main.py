from excel import excel
from database import db, sql
from gui import root, enteruserlogin, enteruserpassword
import tkinter as tk
from getuserdata import getentrytwo
from registration import reg

tk.Button(root, text="Войти",
          command=lambda: getentrytwo(db, sql, enteruserlogin, enteruserpassword)).grid(row=2, column=0)

tk.Button(root, text="Пройдите регистрацию",
          command=lambda: reg(db, sql, enteruserlogin, enteruserpassword)).grid(row=3, column=0)
excel(sql)
root.mainloop()