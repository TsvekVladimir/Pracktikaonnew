import pandas as pd
from database.database import sql


def excel():
    sql.execute('select * FROM students')
    val = sql.fetchall()
    val = {'Логин': [a_tuple[0] for a_tuple in val], 'Пароль': [a_tuple[1] for a_tuple in val],
           'ФИО': [a_tuple[2] for a_tuple in val], 'Работа': [a_tuple[3] for a_tuple in val],
           'Номер телефона': [a_tuple[4] for a_tuple in val], 'Зарплата': [a_tuple[5] for a_tuple in val]}
    z = pd.DataFrame(val)
    z.to_excel("excel/database.xlsx", sheet_name='Студенты', index_label='id')
    print(val)
