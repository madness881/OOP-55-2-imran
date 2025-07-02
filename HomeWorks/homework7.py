import sqlite3
from datetime import datetime

conn = sqlite3.connect('notes.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS notes (
    title TEXT,
    content TEXT,
    priority INTEGER,
    created_at DATE
)
''')
conn.commit()

def add_note(title, content, priority):
    date_now = datetime.now().date()
    cursor.execute(
        'INSERT INTO notes(title, content, priority, created_at) VALUES (?, ?, ?, ?)',
        (title, content, priority, date_now)
    )
    conn.commit()
    print('Заметка добавлена!')

def get_all_notes():
    cursor.execute('SELECT rowid, * FROM notes')
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print('Таблица пуста.')

def update_note(rowid, new_title):
    cursor.execute(
        'UPDATE notes SET title = ? WHERE rowid = ?',
        (new_title, rowid)
    )
    conn.commit()
    print('Заметка обновлена!')

def delete_note(rowid):
    cursor.execute(
        'DELETE FROM notes WHERE rowid = ?',
        (rowid,)
    )
    conn.commit()
    print('Заметка удалена!')



add_note("Встреча", "Созвон с командой", 2)
get_all_notes()
update_note(1, "Обновлённая встреча")
delete_note(1)

conn.close()