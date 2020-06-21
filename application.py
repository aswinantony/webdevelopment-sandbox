from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	headline = "Hello, world! from Python Code" #Variable headline is created
	return render_template("index.html", headline=headline)
	#now here the variable is assigned to the headline attribute in index.html

####For running Flask
# $ export FLASK_APP=hello.py
# $ flask run
# * Running on http://127.0.0.1:5000/