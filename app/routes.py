from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app
from app.forms import LoginForm
from app.models import User

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
@app.route("/admin/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route("/admin/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route("/admin/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
