# Integrate HTML with FLASK
# HTTP verb GET and POST

from flask import Flask, redirect, url_for, render_template, request
# WSGI APPLICATION
app2 = Flask(__name__)


@app2.route('/')
def home():
    return render_template('result.html')


@app2.route('/success/<int:score>')
def success(score):
    r = ""
    if score > 25:
        r = 'pass'
    else:
        r = 'fail'
    return render_template('marksheet.html', result=r)


@app2.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is" + str(score)


# Building URL dynamically
# thus when we enter result/score value it will catch the string as success or fail and that particular function is being run.
@app2.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks > 25:
        result = 'success'
    else:
        result = "fail"
    return redirect(url_for(result, score=marks))


@app2.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        language = float(request.form['language'])
        total_score = (science+maths+language)

    res = ""
    if total_score >= 25:
        res = 'success'
    else:
        res = 'fail'

    # so that the score is in the form of integer
    return redirect(url_for(res, score=total_score))


if __name__ == '__main__':
    app2.run(debug=True)
