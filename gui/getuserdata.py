from gui.gui import tk, root
from delete_if_time.deleteiftime import delete_if_time
from gui.data_update import datab_update


def login(db, sql, enteruserlogin, enteruserpassword):
    userlogin = enteruserlogin.get()
    userpassword = enteruserpassword.get()
    sql.execute(f"SELECT login FROM students WHERE login = '{userlogin}' AND password = '{userpassword}'")
    if sql.fetchone() is None:
        tk.Label(root, text="Такой учетной записи не существует!").grid(row=19, column=1)
    else:
        for value in sql.execute(f"SELECT * FROM students WHERE login = '{userlogin}'"
                                 f"AND password = '{userpassword}'"):
            tk.Label(root, text=value).grid(row=13, column=1)
            tk.Button(root, text='Хотите изменить?',
                      command=lambda: datab_update(db, sql, enteruserlogin, enteruserpassword)).grid(row=14, column=1)
            delete_if_time(db, sql, enteruserlogin, enteruserpassword)
