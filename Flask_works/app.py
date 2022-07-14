from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# to initialize the app. Flask is a class and app is just a variable here
app = Flask(__name__)

# initializing SQL Alchemy. It basicaly allows us to change databases in Python
# detailed about 'SQLALCHEMY_DATABASE_URI' : https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
# detail about 'SQLALCHEMY_TRACK_MODIFICATIONS' =  https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

# removed the temp part as we want the batabse to form here only, and then changed the name from test.db to todo.db
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# we now will define the database schema through building a class


class Todo(db.Model):
    Serial_no = db.Column(db.Integer, primary_key=True)
    Todo_Title = db.Column(db.String(200), nullable=False)
    # nullable = False means it can't be null
    desc = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.serial_no} - {self.Title}"


# adding a decorator 'routes'. routes basically add the endpoints, ie. below method is  basically brings you to the home page.


@app.route("/")
def home_page():
    return render_template('index2.html')

# Let's create another endpoint...


@app.route("/Products")
def products():
    return "Hii, these are all my products"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
