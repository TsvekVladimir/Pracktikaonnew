from gui import tk, root
from deleteiftime import timedel
from dataupdate import databupdate


def getentrytwo(db, sql, enteruserlogin, enteruserpassword):
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
                      command=lambda: databupdate(db, sql, enteruserlogin, enteruserpassword)).grid(row=14, column=1)
            timedel(db, sql, enteruserlogin, enteruserpassword)