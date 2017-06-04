
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request, \
    redirect, abort, session, g, flash, Markup
from thisapi import app
from helpers import *


@app.route('/')
def index():
    return "You are at the homepage of this API™!"


@app.route('/v1/get_party', defaults={"requestpath": ""})
@app.route('/v1/get_party.<path:requestpath>')
def get_party(requestpath= None):
    """
    Retrieve the party for the given id.
    """
    # use the given party id to retrieve existing data if any
    # If the party doesn't exist, it will return an empty one
    requested_id = request.args['pid']
    if validate_pid(requested_id) is  None:
        redirect(url_for("index"))
    party_content = retrieve_party(requested_id)

    return render_output(data=party_content, oformat=requestpath)


@app.route('/v1/add_vid', defaults={"requestpath":""}, methods=["PUT"])
@app.route('/v1/add_vid.<path:requestpath>', methods=["PUT"])
def add_vid(requestpath=None):
    """
    Add a video to the end of the playlist. It should support put/post and for
    get return method not allowed
    """
    new_vid = validate_v(request.args["new_vid"])
    pid = validate_pid(request.args["party_id"])
    if pid is None or new_vid is None:
        redirect(url_for('index'))
    video = get_vid_info(new_vid)
    party_data = retrieve_party(pid)
    party_data["videos"].append(video) #TODO: check if this is in fact mutable.
    party_content = json.dumps(party_data)
    return render_output(data=party_data, oformat=requestpath)
    return render_template('json.html', data=party_content)


@app.route('/redirect-to-<function>')
def pointless_redirect(function=None):
    return redirect(url_for(function))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/upload', methods=['POST'])
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
