from repository import Data

from flask import Flask, render_template, request, redirect

app = Flask(__name__)
data = Data()

@app.route('/list')
def index():
    todos = data.find_all()
    return render_template('index.html', todos=todos)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    name = request.form.get("newTask")
    todo = {"name": name, "done": False}
    data.add_one(todo)
    return redirect("/list")

@app.route('/drop_todo', methods=['GET'])
def drop_todo():
    id = request.args.get("id")
    data.drop_one(id)
    return redirect("/list")

@app.route('/done_todo', methods=['GET'])
def done_todo():
    id = request.args.get("id")
    todo = data.find_one(id)
    todo[2] = not todo[2]
    data.update_one(todo)
    return redirect("/list")

if __name__ == '__main__':
    app.run(debug=True)
