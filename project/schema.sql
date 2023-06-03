CREATE TABLE IF NOT EXISTS Players(
	player_id SERIAL PRIMARY KEY,
	player_name varchar(60),
	decade varchar(6),
	score INTEGER
);



CREATE TABLE IF NOT EXISTS Questions(
	question_id SERIAL PRIMARY KEY,
	question varchar(255),
	movie_attribute varchar(255)	
);


CREATE TABLE IF NOT EXISTS Quizzes(
	quiz_id SERIAL PRIMARY KEY,
	player_id INTEGER,
	FOREIGN KEY (player_id) REFERENCES Players (player_id)
);


CREATE TABLE IF NOT EXISTS Player_Questions(
	pq_id SERIAL PRIMARY KEY,
	quiz_id INTEGER,
	question_id INTEGER,
	question_number INTEGER,
	movie_id TEXT,
	FOREIGN KEY (quiz_id) REFERENCES Quizzes (quiz_id),
	FOREIGN KEY (question_id) REFERENCES Questions (question_id),
	FOREIGN KEY (movie_id) REFERENCES Movies (movie_id)
);

