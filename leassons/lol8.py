import sqlite3

connect = sqlite3.connect("users.db")
cursor = connect.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            fio VARCAHR (100) NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades(
            gradeid INTEGER PRIMARY KEY AUTOINCREMENT,
            userid INTEGER,
            subject VARCAHR (100) NOT NULL,
            grade INTEGER NOT NULL,
            FOREIGN KEY (userid) REFERENCES users(userid)
        )
    ''')

    connect.commit()

create_table()


def add_user(fio, age):
    cursor.execute('INSERT INTO users(fio, age) VALUES (?, ?)', (fio, age))
    connect.commit()
    print(f"Пользователь {fio} добавлен")


# add_user('Илья Муромец', 23)
# add_user('John Doe1', 24)
# add_user('John Doe2', 27)
# add_user('John Doe3', 28)
# add_user('John Doe4', 35)
# add_user('John Doe5', 33)


def add_grade(userid, subject, grade):
    cursor.execute(
        'INSERT INTO grades(userid, subject, grade) VALUES (?,?,?)',
        (userid, subject, grade)
    )
    print(f"Оценка добавлена для пользователя с ID {userid}")
    connect.commit()

# add_grade(99, "Алгебре", 5)
# add_grade(1, "Физика", 3)
# add_grade(1, "Химия", 4)

def get_users_with_grades():
    cursor.execute('''
        SELECT users.fio, grades.subject, grades.grade
        FROM users
        LEFT JOIN grades ON users.userid = grades.userid
    ''')
    rows = cursor.fetchall()
    for i in rows:
        print(f"FIO: {i[0]}, SUBJECT: {i[1]}, GRADE: {i[2]}")



# get_users_with_grades()


# AVG() – Среднее значение
# MAX() – Максимальное значение
# MIN() – Минимальное значение  COUNT() SUM()

# def get_avg_age():
#     cursor.execute('SELECT SUM(age) FROM users')
#     avg_age = cursor.fetchone()
#
#     print(avg_age)
#
# get_avg_age()



def create_view_young_users():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS yong_userses AS
        SELECT fio, age
        FROM users
        WHERE age < 25
    ''')
    connect.commit()
    print('Представление young_users создано')

create_view_young_users()

def get_young_users():
    cursor.execute("""
        SELECT * FROM yong_userses
    """)

    users = cursor.fetchall()
    connect.commit()

    print(users)

get_young_users()

def create_view_good_math_students():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS good_math_students AS
        SELECT users.fio, users.age, grades.subject, grades.grade
        FROM users
        JOIN grades ON users.userid = grades.userid
        WHERE grades.subject = "Математика" AND grades.grade >= 4
    ''')
    connect.commit()
    print("Представление good_math_students создано")

def get_from_view_good_math_students():
    cursor.execute('SELECT * FROM good_math_students')
    result = cursor.fetchall()
    connect.commit()
    print(result)


create_view_good_math_students()
get_from_view_good_math_students()
