Important note! - The process described is used to prepare app via Windows CMD. All commands assume you have CMD already opened.

1. We create a separate directory for our project then move into newly created folder.
	mkdir FlaskApp
	cd FlaskApp

2. Now we start virtual environment using python.
	py -3 -m venv venv

3. Activate the new environment.
	venv\Scripts\activate
4. Install Flask.
	pip install Flask
5. Create Hello_world.py file in your editor, the contents should be as follows:
	from flask import Flask

	app = Flask(__name__)

	@app.route("/")
	def hello_world():
    		return "<p>Hello, World!</p>"

6. Save the file to FlaskApp folder.
7. Declare Hello_world.py as flask app.
	set FLASK_APP=Hello_world.py
8. Run Flask app.
	flask run
9. Copy the url address and paste it into your browser to test
10. Save list of installed packages to text file.
	pip freeze > requirements.txt
