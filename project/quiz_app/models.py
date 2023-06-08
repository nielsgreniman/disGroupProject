# write all your SQL queries in this file.
from quiz_app import conn
import random


def create_Player(name, decade):
    cur = conn.cursor()
    sql = """
    INSERT INTO Players(player_name,decade)
    VALUES (%s,%s)
    """
    cur.execute(sql, (name,decade))
    conn.commit()
    cur.close()

def Player_Exists(name,decade):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Players
    WHERE player_name = %s AND decade = %s
    """
    cur.execute(sql, (name, decade))
    result = cur.rowcount > 0
    cur.close()
    return result


def update_Players_Score(name, decade, score):
    cur = conn.cursor()
    sql = """
    UPDATE Players
    SET score = %s
    WHERE player_name = %s AND decade = %s
    """
    cur.execute(sql, (score,name, decade))
    conn.commit()
    cur.close()
    
def get_player_score(name,decade):
    cur = conn.cursor()
    sql = """
    SELECT score FROM Players
    WHERE player_name = %s AND decade = %s
    """
    cur.execute(sql, (name, decade,))
    myvar = cur.fetchone()
    cur.close()
    return myvar[0]

def create_quiz(name,decade):
    endDecade = str(int(decade) + 10)
    cur = conn.cursor()

    sql = """
    DO $$
    DECLARE
      new_quiz_id INTEGER;
      movie_question_pair RECORD;
      question_counter INTEGER := 1;
    BEGIN
      -- Insert a new quiz and get its ID
      INSERT INTO Quizzes (player_id) VALUES (
	  (SELECT player_id FROM Players WHERE player_name = %s
            AND decade = %s
        )
	  ) RETURNING quiz_id INTO new_quiz_id;

      -- Loop through the selected movie-question pairs
      FOR movie_question_pair IN (
        WITH movie_selection AS (
          SELECT movie_id
          FROM Movies
          WHERE movies.year >= %s AND movies.year < %s
          ORDER BY RANDOM()
          LIMIT 5
        ),
        question_selection AS (
          SELECT movie_selection.movie_id, Questions.question_id
          FROM movie_selection, Questions
        )
        SELECT *
        FROM question_selection
        ORDER BY RANDOM()
        LIMIT 5
      )
      LOOP
        -- Insert each question into the Player_Questions table
        INSERT INTO Player_Questions (quiz_id, question_id, question_number, movie_id)
        VALUES
        (new_quiz_id, movie_question_pair.question_id, question_counter, movie_question_pair.movie_id);

        -- Increase the question_counter by 1
        question_counter := question_counter + 1;
      END LOOP;

      -- RETURN new_quiz_id;
    END $$;
    SELECT currval('quizzes_quiz_id_seq');
    """

    cur.execute(sql, (name,decade,decade,endDecade))
    quiz_id = cur.fetchone()
    conn.commit()
    cur.close()
    if quiz_id:
        return quiz_id
    else:
        return []


def get_question(quiz_id, question_number):
    cur = conn.cursor()

    sql = """
    SELECT pq.question_number, q.question, m.title
    FROM Player_Questions pq
    JOIN Questions q ON pq.question_id = q.question_id
    JOIN Movies m ON pq.movie_id = m.movie_id
    WHERE pq.quiz_id = %s AND pq.question_number = %s;
    """

    cur.execute(sql, (quiz_id, question_number))
    questions = cur.fetchone()

    cur.close()
    if questions:
        return questions
    else:
        return []


def get_correct_answer(quiz_id, question_number):
    cur = conn.cursor()
    # Retrieve the correct answer from the Movies table
    sql = """
    SELECT m.movie_id, q.question, q.movie_attribute
    FROM Player_Questions pq
    JOIN Questions q ON pq.question_id = q.question_id
    JOIN Movies m ON pq.movie_id = m.movie_id
    WHERE pq.quiz_id = %s AND pq.question_number = %s;
    """
    cur.execute(sql, (quiz_id, question_number))
    question_data = cur.fetchone()

    if not question_data:
        return False
    else:
        movie_id = question_data[0]
        question = question_data[1]
        movie_attribute = question_data[2]

        sql = f"SELECT {movie_attribute} FROM Movies WHERE movie_id = %s;"
        cur.execute(sql, (movie_id,))
        correct_answer = cur.fetchone()

    cur.close()

    if correct_answer:
        return correct_answer
    else:
        return []
