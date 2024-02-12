import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('static/database/database.sqlite3')
cursor = conn.cursor()

# Создаем таблицу задач
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username INTEGER NOT NULL,
        task TEXT NOT NULL UNIQUE,
        status BOOLEAN NOT NULL,
        FOREIGN KEY (username) REFERENCES users(username)
    )
''')

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
