from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

# Creating SQLAlchemy Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"{self.sno} - {self.title}"


# Home Page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    allTodo = Todo.query.all()
    return render_template("index.html", allTodo=allTodo)


# Update
@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo_update = Todo.query.filter_by(sno=sno).first()
        todo_update.title = title
        todo_update.desc = desc
        db.session.add(todo_update)
        db.session.commit()
        return redirect("/")
    todo_update = Todo.query.filter_by(sno=sno).first()
    return render_template("update.html", todo=todo_update)


# Delete
@app.route('/delete/<int:sno>')
def delete(sno):
    todo_del = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo_del)
    db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
