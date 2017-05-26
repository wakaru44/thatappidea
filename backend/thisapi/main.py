
from flask import Flask, url_for, render_template, request, \
    redirect, abort, session, g, flash, Markup
from thisapi import app


@app.route('/event', defaults={"path": ""})
@app.route('/event/<path:whatever>')
def event_listener(whatever):
    app.logger.info(whatever)
    """
    a sample method of a catch-all path
    """
    return "You went to {0}".format(whatever)


@app.route('/')
def index():
    return "You are at the homepage!"


@app.route('/redirect-to-<function>')
def pointless_redirect(function=None):
    return redirect(url_for(function))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']


@app.route('/login', methods=['GET', 'POST'])
def login_handler():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_user_in(request.form['username'])
        else:
            error = "Invalid username/password!"
    return render_template('login.html', error=error)
