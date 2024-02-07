from flask import Flask, render_template, request # импортируем класс Flask, функцию render_template и request
import sqlite3 # импортируем модуль sqlite3

app = Flask(__name__) # создаем объект класса Flask

@app.route('/') # создаем маршрут
def index(): # создаем функцию index для обработки запросов по этому маршруту
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('static/database/database.sqlite3')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        if user:
            return render_template('todo_list.html', username=username)
        else:
            return render_template('login.html')
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST']) # создаем маршрут и указываем методы, которые он принимает на вход

def login(): # создаем функцию login для обработки запросов по этому маршруту
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if verify_user(username, password):
            return render_template('todo_list.html', username=username)
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

def verify_user(username, password):
    conn = sqlite3.connect('static/database/database.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        return True
    else:
        return False

@app.route('/register')
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('static/database/database.sqlite3')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        conn.close()
        return render_template('todo_list.html', username=username)
    return render_template('register.html')

@app.route('/todo')
def todo(): # создаем функцию todo для обработки запросов по этому маршруту
    if request.method == 'POST':
        task = request.form['task']
        username = request.form['username']
        conn = sqlite3.connect('static/database/database.sqlite3')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (task, username) VALUES (?, ?)', (task, username))
        conn.commit()
        conn.close()
        return render_template('todo_list.html', username=username)
    username = request.args.get('username')
    return render_template('todo_list.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
