from flask import Flask
from flask import render_template
from flask import request, url_for, redirect, session
from datetime import datetime
from . import app

app.secret_key = "super secret key"

@app.route("/", methods = ['GET', 'POST'])
def home():
    noNameError = False
    if request.method == 'POST':
        name = request.form.get('name')
        decade = request.form.get('decade')
        if not name:
            noNameError = True
        else:
            session["name"] = name
            session["decade"] = decade
            return redirect(url_for('quiz'))
    return render_template("home.html", error=noNameError)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route('/quiz')
def quiz():
    name = session.get("name")
    decade = session.get("decade")
    return render_template('quiz.html', name=name, decade=decade)

if __name__ == '__main__':
    app.run(debug=True)