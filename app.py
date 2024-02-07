from flask import Flask, render_template, request # импортируем класс Flask, функцию render_template и request
import sqlite3 # импортируем модуль sqlite3

app = Flask(__name__) # создаем объект класса Flask

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/todo')
def todo():
    username = request.args.get('username')
    return render_template('todo_list.html', username=username)

if __name__ == '__main__':
    app.run(debug=False)
