from excel.excel import excel
from database.database import db, sql
from gui.gui import root, enteruserlogin, enteruserpassword
import tkinter as tk
from gui.getuserdata import login
from gui.registration import registration

tk.Button(root, text="Войти",
          command=lambda: login(db, sql, enteruserlogin, enteruserpassword)).grid(row=2, column=0)

tk.Button(root, text="Пройдите регистрацию",
          command=lambda: registration(db, sql, enteruserlogin, enteruserpassword)).grid(row=3, column=0)
excel()
root.mainloop()
