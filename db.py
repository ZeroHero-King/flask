import sqlite3

# Создаем соединение с базой данных
conn = sqlite3.connect('users.sqlite3')

# Создаем курсор для выполнения операций SQL
cur = conn.cursor()

# Создаем таблицу пользователей (users)
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# Создаем таблицу для списка дел (todo_list), если она нужна
cur.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

# Закрываем курсор и сохраняем изменения в базе данных
cur.close()
conn.commit()

# Закрываем соединение
conn.close()
