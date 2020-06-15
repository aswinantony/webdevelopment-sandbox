from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

####For running Flask
# $ export FLASK_APP=hello.py
# $ flask run
# * Running on http://127.0.0.1:5000/
