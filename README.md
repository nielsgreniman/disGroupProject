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
Remember to correct the path in the last line in the file import_movie_from_sql.sql to point to the movie.csv file

Change the information in the file __init__.py corresponding to the database name and password.

# Run webapp
Navigate into the quiz_app folder, then launch the program using
python -m flask run (or python3 -m flask run)

# Open default browser to rendered page
http://127.0.0.1:5000/

