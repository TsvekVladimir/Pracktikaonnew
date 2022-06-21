from gui.gui import tk, root
from excel.excel import excel


class Userinfo(object):
    def __init__(self, login, password, fio, work, number, money):
        self.login = login
        self.password = password
        self.fio = fio
        self.work = work
        self.number = number
        self.money = money


def datab_update(db, sql, enteruserlogin, enteruserpassword):
    userlogin = enteruserlogin.get()
    userpassword = enteruserpassword.get()
    sql.execute("SELECT date FROM students WHERE login = ? AND password = ?", (userlogin, userpassword))
    tk.Label(text='Логин ').grid(row=21, column=0)
    tk.Label(text='Пароль ').grid(row=22, column=0)
    tk.Label(text='ФИО ').grid(row=23, column=0)
    tk.Label(text='Место Работы ').grid(row=24, column=0)
    tk.Label(text='Номер ').grid(row=25, column=0)
    tk.Label(text='ЗП').grid(row=26, column=0)
    newlg = tk.Entry(root)
    newlg.grid(row=21, column=1)
    newps = tk.Entry(root)
    newps.grid(row=22, column=1)
    newfio = tk.Entry(root)
    newfio.grid(row=23, column=1)
    newwk = tk.Entry(root)
    newwk.grid(row=24, column=1)
    newnumb = tk.Entry(root)
    newnumb.grid(row=25, column=1)
    newzp = tk.Entry(root)
    newzp.grid(row=26, column=1)
    tk.Button(root, text='Изменить данные',
              command=lambda: update(db, sql, userlogin, userpassword,
                                     Userinfo(newlg.get(), newps.get(), newfio.get(), newwk.get(),
                                     newnumb.get(), newzp.get()))).grid(row=51, column=1)


def update(db, sql, userlogin, userpassword, Userinfo):
    sql.execute("""UPDATE students SET login = ? WHERE login = ? AND password = ?""",
                (Userinfo.login, userlogin, userpassword))
    sql.execute("""UPDATE students SET password = ? WHERE login = ? AND password = ?""",
                (Userinfo.password, Userinfo.login, userpassword))
    sql.execute("""UPDATE students SET fio = ? WHERE login = ? AND password = ?""",
                (Userinfo.fio, Userinfo.login, Userinfo.password))
    sql.execute("""UPDATE students SET rabota = ? WHERE login = ? AND password = ?""",
                (Userinfo.work, Userinfo.login, Userinfo.password))
    sql.execute("""UPDATE students SET number = ? WHERE login = ? AND password = ?""",
                (Userinfo.number, Userinfo.login, Userinfo.password))
    sql.execute("""UPDATE students SET zp = ? WHERE login = ? AND password = ?""",
                (Userinfo.money, Userinfo.login, Userinfo.password))
    tk.Label(root, text='Запись успешно изменена!').grid(row=99, column=1)
    for value in sql.execute(f"SELECT * FROM students WHERE login = '{Userinfo.login}'"
                             f"AND password = '{Userinfo.password}'"):
        tk.Label(root, text=value).grid(row=66, column=1)
        db.commit()
    excel()
