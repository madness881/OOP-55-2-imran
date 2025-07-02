import sqlite3

connect = sqlite3.connect("users1.db")
cursor = connect.cursor()


def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    fio VARCHAR(100) NOT NULL,
    age INTEGER NOT NULL,
    )
''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS gradef (
        greadid INTEGER PRIMARY KEY AUTOINCREMENT,
        userid INTEGER
        subject VARCHAR(100) NOT NULL,
        grades INTEGER NOT NULL,
        FOREIGN KEY(userid) REFERENCES users(userid)
    )
                   
''')
    connect.commit()

    create_table()


def add_user(fio, age):
    cursor.execute('INSERT INTO users(fio, age) VALUES (?, ?)', (fio, age))
    connect.commit()
    print(f'Пользователь {fio} добавлен')



def add_grade(userid, subject, grades):
    cursor.execute(
        'INSERT INTO grades(userid, subject, grades) VALUES (?, ?, ?)',
        (userid, subject, grades)
    )

def get_users_with_grades():
    cursor.execute('''
    SELECT users.fio,grades.subject,grades.grades
    FROM users RIGHT JOIN grades ON users.userid = grades.userid
    ''')

    rows = cursor.fetchall()
    for i in rows:
        print(f'FIO:{i[0]}, subject:{i[1]}, grades:{i[2]}')

get_users_with_grades()

#AVG() -srednee
#MIN() - MIN
#MAX() - MAX

# def get_avg_age():
#     cursor.execute('SELECT AVG(age) FROM users')
#     avg_age = cursor.fetchall() #fetchone()
#
#     print(avg_age)
#
# get_avg_age()


def create_view_young_users():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS yong_users AS
        SELECT fio,age
        FROM users
        WHERE age <= 30
    ''')

