# set FLASK_APP=app.py
# set FLASK_ENV=development
# python -m flask run

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
