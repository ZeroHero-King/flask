from flask import Flask, render_template, request # импортируем класс Flask, функцию render_template и request
import sqlite3 # импортируем модуль sqlite3

app = Flask(__name__) # создаем объект класса Flask

@app.route('/')
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        if user:
            return render_template('todo_list.html', username=username)
        else:
            return render_template('login.html')
    return render_template('index.html')

@app.route('/login')
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        if user:
            return render_template('todo_list.html', username=username)
        else:
            return render_template('login.html')
    return render_template('login.html')

@app.route('/register')
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        conn.close()
        return render_template('todo_list.html', username=username)
    return render_template('register.html')

@app.route('/todo')
def todo():
    if request.method == 'POST':
        task = request.form['task']
        username = request.form['username']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (task, username) VALUES (?, ?)', (task, username))
        conn.commit()
        conn.close()
        return render_template('todo_list.html', username=username)
    username = request.args.get('username')
    return render_template('todo_list.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
