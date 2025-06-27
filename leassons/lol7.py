import sqlite3

# A4 - бумага
connect = sqlite3.connect("users.db")
# Рука с карандашом
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        fio VARCHAR (100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()
# CRUD - Create - Read - Update - Delete

def add_user(fio, age, hobby):
    cursor.execute(
        'INSERT INTO users(fio, age, hobby) VALUES (?,?,?)',
        (fio, age, hobby)
    )
    connect.commit()
    print("user created!!")

# def add_user(fio, age, hobby):
#     cursor.execute(
#         f'INSERT INTO users(fio, age, hobby) VALUES ("{fio}","{age}","{hobby}")',
#     )
#     connect.commit()
#     print("user created!!")

# add_user('Ardager Kartanbekov', 26, "Дрыхнуть")

def get_all_users():
    cursor.execute('SELECT * FROM users')

    users = cursor.fetchall()

    print(f"All users!!! ")
    for i in users:
        print(f"FIO: {i[0]}, AGE: {i[1]} HOBBY: {i[2]}")

# get_all_users()

# Update

def update_user(fio, rowid):
    cursor.execute(
        'UPDATE users SET fio = ? WHERE rowid = ?',
        (fio, rowid)
    )
    # cursor.execute(
    #     f'UPDATE users SET fio = "{fio}" WHERE rowid = "{rowid}"'
    # )
    connect.commit()
    print("User updated!!!")

update_user("my row 5", 5)

def delete_user(rowid):
    cursor.execute('DELETE FROM users WHERE rowid = ?', (rowid,))
    connect.commit()
    print('user deleted!!!')


# delete_user(3)
