from flask import render_template
from flask import request, url_for, redirect, session
from datetime import datetime
from . import app
from quiz_app.models import create_Player, Player_Exists, update_Players_Score, create_quiz, get_question, get_correct_answer, get_player_score

# Home page. Here the player is asked to write his/her name and the decade they want to quiz about.
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

# Finish page. Here the player is presented a total score and the possibility to play again.
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

# Quiz page. Displayed for each of the five questions. The player can submit an answer and will then
# move on to the next question. The player can also exit the quiz.
@app.route('/quiz',  methods = ['GET', 'POST'])
def quiz():
    name = session.get("name")
    decade = session.get("decade")

    # No access if you have not given name and decade
    if not (name and decade):
        return render_template("home.html", error=False)

    # First question. Her er man blevet redirected fra forsiden - UDEN en post
    if not request.method == 'POST':
        if not Player_Exists(name, decade):
            create_Player(name, decade)
        question_number = 1
        quiz_id = create_quiz(name,decade)[0]
        question = get_question(quiz_id, question_number)
        quiz_question = question[1]
        chosen_movie = question[2]
        # Inilialize player score at zero
        update_Players_Score(name, decade, 0)
        return render_template(
                                'quiz.html',
                                name=name,
                                decade=decade,
                                quiz_question=quiz_question,
                                question_number=question_number,
                                quiz_id=quiz_id,
                                chosen_movie=chosen_movie)

    # Question 2-5
    else:
        answer = request.form.get('answer')
        question_number = request.form.get('question_number', type=int)
        quiz_id = request.form.get('quiz_id', type=int)
        correct_answer = "Error: Unknown"
        if answer is not None:
            # Strip leading and trailing whitespaces from the answer (to easy comparison with correct answer):
            answer = answer.strip()
            # Extract correct answer from database:
            correct_answer = get_correct_answer(quiz_id, question_number)
            # Check player answer. To take spelling mistakes into account, just four
            # characters need to match (in the correct order, though) for answers longer
            # than four characters:
            if correct_answer:
                short_correct_answer = correct_answer[0][:20] + " [...]" if len(correct_answer[0]) > 20 else correct_answer[0]
                if len(short_correct_answer) < 4:
                    is_correct = (answer.lower() == short_correct_answer.lower())
                else:
                    is_correct = any(answer.lower()[i:i+4] in correct_answer[0].lower() for i in range(len(answer) - 3))
                correct_answer = short_correct_answer
            else:
                is_correct = False
                correct_answer =  "Error: Unknown answer"

        else:
            is_correct = False

        # Add point to player if answer is correct
        if is_correct:
            score = get_player_score(name, decade) + 1
            update_Players_Score(name, decade, score)

        # Add one to question number
        if question_number is not None:
            try:
                question_number = int(question_number) + 1
            except ValueError:
                return "Question number should be an integer."
        else:
            return "No question number received."
        if question_number < 6:
            # New question in line
            question = get_question(quiz_id, question_number)
            quiz_question = question[1]
            chosen_movie = question[2]
            return render_template(
                                    'quiz.html',
                                    name=name,
                                    decade=decade,
                                    quiz_question=quiz_question,
                                    question_number=question_number,
                                    quiz_id=quiz_id,
                                    chosen_movie=chosen_movie,
                                    is_correct_answer=is_correct,
                                    correct_answer=correct_answer)
        # Quiz finish after the fifth question
        else:
            return render_template("finish.html",
                                   score=get_player_score(name,decade))

if __name__ == '__main__':
    app.run(debug=True)