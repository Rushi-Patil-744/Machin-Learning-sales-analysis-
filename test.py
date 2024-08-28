from flask import Flask, redirect, url_for
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Congratulations to all"

@app.route("/success/<int:score>")
def success(score):
    return "He/She is passed and mark is" + str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "He/She is failed and mark is" + str(score)

### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = " "
    if marks<35:
        result="fail"
    else:
        result="success"
    return redirect(url_for(result, score = marks))

if __name__ == '__main__':
    app.run(debug = True)