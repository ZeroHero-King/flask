from flask import Flask, render_template, request
app = Flask(__name__)

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
    app.run(debug=True)
