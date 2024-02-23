import sqlite3

# Функции для работы с базой данных
def get_db_connection():
    conn = sqlite3.connect('database/users.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

def create_user(username, email, password):
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_user_by_username_and_password(username, password):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
    conn.close()
    return user

def create_task(task_content, user_id):
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO tasks (task, user_id) VALUES (?, ?)', (task_content, user_id))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_user_by_id(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    return user

def get_tasks_by_user_id(user_id):
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks WHERE user_id = ?', (user_id,)).fetchall()
    conn.close()
    return tasks

def db_complete_task(task_id, user_id):
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET completed = 1 WHERE id = ? AND user_id = ?', (task_id, user_id))
    conn.commit()
    conn.close()

def db_delete_task(task_id, user_id):
    conn = get_db_connection()
    try:
        conn.execute('DELETE FROM tasks WHERE id = ? AND user_id = ?', (task_id, user_id))
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        conn.close()