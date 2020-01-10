from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

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

@app.route("/admin")
@app.route("/admin/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template("login.html", form=form)
