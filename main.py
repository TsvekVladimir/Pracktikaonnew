from excel import excel
from database import db, sql
from gui import root, enteruserlogin, enteruserpassword
import tkinter as tk
from datetime import timedelta, datetime


def timedel(db, sql, enteruserlogin, enteruserpassword):
    userlogin = enteruserlogin.get()
    userpassword = enteruserpassword.get()
    timedelete = timedelta(1095)
    sql.execute("SELECT date FROM students WHERE login = ? AND password = ?", (userlogin, userpassword))
    a = sql.fetchone()
    a = (" ".join(map(str, a)))
    a = datetime.strptime(a, "%Y-%m-%d").date()
    print(a)
    deltime = a + timedelete
    sql.execute(f"""DELETE FROM students WHERE date = {deltime}""")
    db.commit()


def databupdate(db, sql, enteruserlogin, enteruserpassword):
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

    def update(db, sql, enteruserlogin, enteruserpassword):
        newlogin = newlg.get()
        sql.execute("""UPDATE students SET login = ? WHERE login = ? AND password = ?""",
                    (newlogin, userlogin, userpassword))
        newpassword = newps.get()
        sql.execute("""UPDATE students SET password = ? WHERE login = ? AND password = ?""",
                    (newpassword, userlogin, userpassword))
        newfior = newfio.get()
        sql.execute("""UPDATE students SET fio = ? WHERE login = ? AND password = ?""",
                    (newfior, userlogin, userpassword))
        newwork = newwk.get()
        sql.execute("""UPDATE students SET rabota = ? WHERE login = ? AND password = ?""",
                    (newwork, userlogin, userpassword))
        newnumber = newnumb.get()
        sql.execute("""UPDATE students SET number = ? WHERE login = ? AND password = ?""",
                    (newnumber, userlogin, userpassword))
        newzarplata = newzp.get()
        sql.execute("""UPDATE students SET zp = ? WHERE login = ? AND password = ?""",
                    (newzarplata, userlogin, userpassword))
        tk.Label(root, text='Запись успешно изменена!').grid(row=99, column=1)
        for value in sql.execute(f"SELECT * FROM students WHERE login = '{newlogin}'"
                                 f"AND password = '{newpassword}'"):
            tk.Label(root, text=value).grid(row=66, column=1)
        tk.Button(root, text='Хотите изменить?',
                  command=lambda: databupdate(db, sql, enteruserlogin, enteruserpassword)).grid(row=100, column=1)
        db.commit()
    tk.Button(root, text='Изменить данные',
              command=lambda: update(db, sql, enteruserlogin, enteruserpassword)).grid(row=51, column=1)


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


tk.Button(root, text="Войти",
          command=lambda: getentrytwo(db, sql, enteruserlogin, enteruserpassword)).grid(row=2, column=0)


def reg(db, sql, enteruserlogin, enteruserpassword):
    tk.Label(root, text="Зарегистрируйтесь!").grid(row=4, column=1)
    tk.Label(root, text="Login: ", justify=tk.RIGHT).grid(row=5, column=0)
    newuserlogin = tk.Entry(root)
    newuserlogin.grid(row=5, column=1)
    tk.Label(root, text="Password: ", justify=tk.RIGHT).grid(row=6, column=0)
    newuserpassword = tk.Entry(root)
    newuserpassword.grid(row=6, column=1)
    tk.Label(root, text="Введите ФИО: ", justify=tk.RIGHT).grid(row=7, column=0)
    newuserfio = tk.Entry(root)
    newuserfio.grid(row=7, column=1)
    tk.Label(root, text="Введите место работы: ", justify=tk.RIGHT).grid(row=8, column=0)
    newuserrabota = tk.Entry(root)
    newuserrabota.grid(row=8, column=1)
    tk.Label(root, text="Введите номер телефона: ", justify=tk.RIGHT).grid(row=9, column=0)
    newusernumber = tk.Entry(root)
    newusernumber.grid(row=9, column=1)
    tk.Label(root, text="Введите вашу заработную плату: ", justify=tk.RIGHT).grid(row=10, column=0)
    newuserzp = tk.Entry(root)
    newuserzp.grid(row=10, column=1)

    def getnewdata(db, sql, enteruserlogin, enteruserpassword):
        userlogin = newuserlogin.get()
        userpassword = newuserpassword.get()
        userfio = newuserfio.get()
        userrabota = newuserrabota.get()
        usernumber = newusernumber.get()
        userzp = newuserzp.get()
        sql.execute(f"SELECT login FROM students WHERE login = '{userlogin}' AND password = '{userpassword}'")
        print(userlogin, userpassword)
        if sql.fetchone() is None:
            deta = datetime.now().date()
            sql.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (userlogin, userpassword, userfio, userrabota, usernumber, userzp, deta))
            db.commit()
            tk.Label(root, text="Вы успешно зарегистрировались!")
            for value in sql.execute(f"SELECT * FROM students WHERE login = '{userlogin}'"
                                     f"AND password = '{userpassword}'"):
                tk.Label(root, text=value).grid(row=13, column=1)
                tk.Button(root, text='Хотите изменить?',
                          command=lambda: databupdate(db, sql, enteruserlogin, enteruserpassword))\
                    .grid(row=14, column=1)
        else:
            tk.Label(root, text="Такая запись уже существует вы вошли в учетную запись")
            for value in sql.execute(f"SELECT * FROM students WHERE login = '{userlogin}'"
                                     f"AND password = '{userpassword}'"):
                tk.Label(root, text=value).grid(row=13, column=1)
                tk.Button(root, text='Хотите изменить?',
                          command=lambda: databupdate(db, sql, enteruserlogin, enteruserpassword))\
                    .grid(row=14, column=1)
    tk.Button(root, text="Зарегистрироваться!",
              command=lambda: getnewdata(db, sql, enteruserlogin, enteruserpassword)).grid(row=11, column=1)


tk.Button(root, text="Пройдите регистрацию",
          command=lambda: reg(db, sql, enteruserlogin, enteruserpassword)).grid(row=3, column=0)
root.mainloop()

sql.execute('select * FROM students')
val = sql.fetchall()

print(val)
excel(sql)
