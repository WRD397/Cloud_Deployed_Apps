from flask import Flask, redirect, url_for
# WSGI APPLICATION
app = Flask(__name__)


@app.route('/')
def home():
    return "Hi there !, welcome you there ! How you doin'"

# so that the score is in the form of integer


@app.route('/success/<int:score>')
def success(score):
    return f"The person has passed and the marks is {score}"


@app.route('/fail/<int:score>')
def fail(score):
    return f"The person has failed and the marks is {score}"


# Building URL dynamically
# thus when we enter result/score value it will catch the string as success or fail and that particular function is being run.
@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks > 25:
        result = 'success'
    else:
        result = "fail"
    return redirect(url_for(result, score=marks))


if __name__ == '__main__':
    app.run(debug=True)
