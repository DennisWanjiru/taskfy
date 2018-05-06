from flask import Flask, redirect, url_for, render_template
from task import Task

app = Flask(__name__)

task = Task('First task', 'The description of this task')
task2 = Task('Second task', 'The description of the second task')
task3 = Task('Third task', 'The description of the third task')

tasks = [task, task2, task3]


@app.route('/')
def root():
    return redirect(url_for('index'))


@app.route('/tasks', methods=["GET"])
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/tasks/<int:task_id>', methods=["GET"])
def get_task(task_id):
    task = [task for task in tasks if task.id == task_id]
    print(task)

    if len(task) == 0:
        return "<h1>404 - Not Found</h1>"
    return render_template('show.html', task=task[0])


if __name__ == '__main__':
    app.run(debug=True)
