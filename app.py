from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import create_user, get_user_by_username_and_password, create_task, get_tasks_by_user_id, db_complete_task, db_delete_task

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Маршруты Flask
@app.route('/')
def index():
    if 'user_id' in session:
        user_id = session['user_id']
        # username = session['username']
        tasks = get_tasks_by_user_id(user_id)
        return render_template('todo_list.html', tasks=tasks)
    else:
        return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user_by_username_and_password(username, password)
        if user:
            session['user_id'] = user['id']
            flash('Вы успешно вошли', 'success')
            return redirect(url_for('index'))
        else:
            flash('Неправильное имя пользователя или пароль', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        if create_user(username, email, password):
            flash('Регистрация прошла успешно. Теперь вы можете войти', 'success')
            if confirm_password != password:
                flash('Пароли не совпадают', 'error')
                return render_template('register.html')
            return redirect(url_for('login'))
        else:
            flash('Пользователь с таким именем уже существует', 'error')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Вы успешно вышли', 'success')
    return redirect(url_for('index'))

@app.route('/add_task', methods=['POST'])
def add_task():
    if 'user_id' in session:
        user_id = session['user_id']
        task_content = request.form['task']
        create_task(task_content, user_id)
        flash('Задача успешно добавлена', 'success')
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    if 'user_id' in session:
        user_id = session['user_id']
        db_complete_task(task_id, user_id)
        flash('Задача отмечена как выполненная', 'success')
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'user_id' in session:
        user_id = session['user_id']
        if db_delete_task(task_id, user_id):  # Передаем оба аргумента в функцию delete_task
            flash('Задача успешно удалена', 'success')
        else:
            flash('Ошибка при удалении задачи', 'error')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
