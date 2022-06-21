from datetime import timedelta, datetime


def delete_if_time(db, sql, enteruserlogin, enteruserpassword):
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
