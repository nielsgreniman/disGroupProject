#####################
### About the app ###
#####################

Players select a decade, and will then recive five question about movies from that decade. The questions are
randomly generated and can relate to 
	-the release year
	-the cast members
	-the director
	-the IMDB ranking
A correct answer is awarded with one point - yelding a maximum of five points. 
The data used for the quiz is the 250 highest ranked movies on IMDB, collected as a .csv file from IMDB's own webpage.

###################
### E/R diagram ###
###################

We made a E/R diagram before implementing our database. As we implemented our database and flask application, we 
gradually moved away from our initially design idea for the database. Once we had our application working, we 
recreated our E/R diagram so that it fitted our final design. But we faced a problem: Our final design does not 
translate very well to a E/R diagram. In particular: the relation 'player_questions' is connected to two entities 
AND a relation. Having two relations next to each other seems to be bad practice (or at least unusual). 

Lesson learned for the group: Make a more thorough initial design. And if we deviate from that design during 
implementation, make sure that the new design follows the convension of an E/R diagram and a good design.

The E/R diagram is located in the 'project' folder.

######################################
### How to compile and run the app ###
######################################

# disGroupProject
Movie quiz created in Flask

# Install packages in the original environment.
pip install -r requirements.txt (or pip3 install -r requirements.txt)

# Activate the self-contained environment (Linux/macOS)
source .venv/bin/activate

# Set an environment variable for FLASK_APP
export set FLASK_APP=webapp

# Set up database
Create a database 'movieProject' in PostgreSQL and run the three sql files listed below. Before you do,
note that 'movie.csv' is located in the 'project' folder. Also, remember to update the path in the last 
line in the file 'import_movie_from_sql.sql' - it is the path to 'movie.csv'. Finally, note that if you 
have problems running 'import_movie_from_sql.sql', you should check out the last section of this text file.

Here are the sql files to run. They are placed in 'project/sql_files':
    - import_movie_from_sql.sql
    - schema.sql
    - schema_ins.sql

# Update password
Change the password in the file __init__.py located in the 'quiz_app' folder.

# Run webapp
Navigate into the quiz_app folder, then launch the program using
python -m flask run (or python3 -m flask run)

# Open default browser to rendered page
http://127.0.0.1:5000/

###

# Alternative to running 'import_movie_from_sql.sql' (only relevant if running the file causes troubles)
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

Then, run the following in the terminal ('PSQL tool' in pgadmin). Remember to change the path.

	\copy Movies FROM '/home/kristian/Desktop/movies.csv' DELIMITER ',' CSV HEADER;
