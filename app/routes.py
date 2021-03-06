from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, SubmitForm, DashboardDetailForm, AdminProfileForm
from app.models import User, Submission

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    form = SubmitForm()
    if form.validate_on_submit():
        submission = Submission(
                title = form.title.data,
                submitter = form.submitter.data, 
                submission = form.submission.data,
                publishing_status = "new")
        db.session.add(submission)
        db.session.commit()
        flash('Your leak has been saved and is going to be reviewed. Thank you for leaking with <em>Leakyleaks</em>')
        return redirect(url_for('process'))
    return render_template('submit.html', form=form)

@app.route("/thank_you")
def process():
    return render_template("process.html", leaks=url_for('leaks'))

@app.route("/leaks")
def leaks():
    submissions = Submission.query.filter_by(publishing_status='published').all()
    return render_template("leaks.html", leaks=submissions)

@app.route("/admin")
@login_required
def admin():
    return redirect(url_for('dashboard'))

@app.route("/admin/dashboard", methods=['GET','POST'])
@login_required
def dashboard():
    submissions = Submission.query.all()
    return render_template('dashboard.html', submissions=submissions)

@app.route('/admin/dashboard/<ident>', methods=['GET','POST'])
@login_required
def admin_submission_details(ident):
    submission = Submission.query.filter_by(ident=ident).first_or_404()
    form = DashboardDetailForm()
    if form.validate_on_submit():
        submission = Submission.query.filter_by(ident = ident).first()
        submission.set_status(form.action.data)
        db.session.commit()
        flash('Your leak has been updated.')
        return redirect(url_for('dashboard'))
    return render_template('admin_submission_detail.html', submission=submission, form=form)     

@app.route("/admin/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
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

@app.route("/admin/profile", methods=['GET','POST'])
@login_required
def admin_profile():
    id = current_user.get_id()
    user = User.query.filter_by(id=id).first_or_404()
    form = AdminProfileForm()
    if form.validate_on_submit():
        if form.change_hint.data and user is not None and user.check_password(form.old_password.data):
            user.set_password_hint(form.password_hint.data)
            db.session.commit()
            flash('Your new profile update has been sent to the mainframe for tonight\'s batch processing...')
            return redirect(url_for('admin_profile'))
        elif form.change_password.data and user is not None and user.check_password(form.old_password.data):
            if form.new_password.data == form.new_password2.data:
                user.set_password(form.new_password.data)
                db.session.commit()
                flash('Your new profile update has been sent to the mainframe for tonight\'s batch processing...')
            return redirect(url_for('admin_profile'))
        else:
            flash('There was an error happening, which is not correctly handled. Might want to try again tomorrow.')
        return redirect(url_for('admin_profile'))
    form.password_hint.data = user.get_password_hint()
    return render_template('admin_profile.html', form=form)

