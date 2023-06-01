# write all your SQL queries in this file.
from quiz_app import conn
import random



def select_Movies(decade):
    cur = conn.cursor()
    endDecade = str(int(decade) + 9)
    sql = """
    SELECT * FROM Movies
    WHERE Year BETWEEN %s AND %s
	ORDER BY RANDOM()
	LIMIT 5    """
    cur.execute(sql, (decade,endDecade))
    movies = cur.fetchone() if cur.rowcount > 0 else None;
    cur.close()
    return movies


def create_User(name):
    cur = conn.cursor()
    sql = """
    INSERT INTO Users(name)
    VALUES (%s)
    """
    cur.execute(sql, (name))
    conn.commit()
    cur.close()

def check_User_Exists(name):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Users
    WHERE name = %s
    """
    cur.execute(sql, (name))
    result = cur.rowcount > 0
    cur.close()
    return result

def update_User_Score(name,score):
    cur = conn.cursor()
    sql = """
    UPDATE Users
    SET score = %s
    WHERE name = %s
    """
    cur.execute(sql, (score,name))
    conn.commit()
    cur.close()


def select_random_question():
    cur = conn.cursor()
    sql = """
    SELECT question FROM Questions
    ORDER BY RANDOM()
	LIMIT 1
    """
    cur.execute(sql)
    random_question = cur.fetchone() if cur.rowcount > 0 else None;
    return random_question






def get_random_movies(n):
    random.sample(range(10), n)
