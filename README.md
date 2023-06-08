# disGroupProject
Movie quiz created in Flask

# Install packages in the original environment.
pip install -r requirements.txt (or pip3 install -r requirements.txt)

# Activate the self-contained environment (Linux/macOS)
source .venv/bin/activate

# Set an environment variable for FLASK_APP
export set FLASK_APP=webapp

# Set up database
Create a database 'movieProject' in PostgreSQL and run the three sql files:
    - import_movie_from_sql.sql
    - schema.sql
    - schema_ins.sql
Please remember to correct the path in the last line in the file 'import_movie_from_sql.sql'.
Also note that if you have problems running 'import_movie_from_sql.sql', see last section of this text file.

# Update password
Change the password in the file __init__.py.

# Run webapp
Navigate into the quiz_app folder, then launch the program using
python -m flask run (or python3 -m flask run)

# Open default browser to rendered page
http://127.0.0.1:5000/

###

# Alternative to running 'import_movie_from_sql.sql' (only relevant if the file causes troubles)
First, create the table using:

	CREATE table Movies(
	rank text,
	movie_id text,
	title text,
	year text,
	link text,
	imbd_votes text,
	imbd_rating text,
	certificate text,
	duration text,
	genre text,
	cast_id text,
	cast_name text,
	director_id text,
	director_name text,
	writer_id text,
	writer_name text,
	storyline text,
	user_id text,
	user_name text,
	review_id text,
	review_title text,
	review_content text,
	PRIMARY KEY (movie_id)
	);

Then, run the following in the terminal ('PSQL tool' in pgadmin). Remeber to change the path.

	\copy Movies FROM '/home/kristian/Desktop/movies.csv' DELIMITER ',' CSV HEADER;
