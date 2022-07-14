from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')

# Let's create another endpoint...


@app.route("/Products")
def products():
    return "Hii, these are all my products"


if __name__ == "__main__":
    app.run(debug=True)
