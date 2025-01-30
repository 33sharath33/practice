from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []  # A simple in-memory list to store tasks

@app.route('/')
def home():
    return render_template('home.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    if task_content:
        tasks.append(task_content)
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

