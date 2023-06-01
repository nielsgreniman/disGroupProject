from flask import render_template
from flask import request, url_for, redirect, session
from datetime import datetime
from . import app
import quiz_app.models

@app.route("/", methods = ['GET', 'POST'])
def home():
    session.clear()
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

@app.route("/finish/", methods = ['GET', 'POST'])
def finish():
    name = session.get("name")

    if not name:
        return render_template("home.html", error=False)

    if request.method == 'POST':
        decade = request.form.get('decade')
        finish = request.form.get('finish')
        if not finish:
            session["decade"] = decade
            return redirect(url_for('quiz'))
        else:
            return render_template("home.html", error=False)

    return render_template("finish.html")

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

@app.route('/quiz',  methods = ['GET', 'POST'])
def quiz():
    quiz_number = 1
    name = session.get("name")
    decade = session.get("decade")
    if request.method == 'POST':
        quiz_number = request.form.get('quiz_number', type=int)
        if quiz_number is not None:
            try:
                quiz_number = int(quiz_number) + 1
            except ValueError:
                return "Quiz number should be an integer."
        else:
            return "No quiz number received."
    if quiz_number == 6:
        return render_template("finish.html")
    if name and decade:
# Her skal der nu ske følgende:
# Funktion der skriver navn ned i databasen
# DONE VIA MODULS.PY

# Der loopes 5 gange, ét for hvert spørgsmål
# Hvis i > 5 så slut => redirect til slutside.
# Slutside kan så enten gå til quiz-side eller til home-side
# DONE

# Fem film væælges tilfældig fra databasen hørende til det rigtige årti
# Lav funktion dertil
# DONE VIA SQL - MODULS.PY

# Scoren opdateres for hvert spørgsmål
# Lav funktion dertil

# Next-knappen sender information om, hvilket spørgsmål
# der er det næste i ræækken, dvs. variablen "i"
# DONE

            chosen_movie = "test"
            quiz_question = "Which year did the following movie first appear?"
            return render_template(
                                    'quiz.html',
                                    name=name,
                                    decade=decade,
                                    highscore="x/y",
                                    quiz_question=quiz_question,
                                    quiz_number=quiz_number,
                                    chosen_movie=chosen_movie)
    else:
        return render_template("home.html", error=False)



if __name__ == '__main__':
    app.run(debug=True)