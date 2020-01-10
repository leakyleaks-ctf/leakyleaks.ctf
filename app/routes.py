from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
        return render_template("index.html")

@app.route("/submit")
def submit():
        return render_template("submit.html", leaks=leaks)

@app.route("/leaks")
def leaks():
        leaks = [
                { 'content' : 'Leak 1',
                    'submitter' : 'Edward Snowden'
                    },
                { 'content' : 'Leak 2',
                    },
                ]
        return render_template("leaks.html", leaks=leaks)
