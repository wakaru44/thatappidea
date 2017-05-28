
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request, \
    redirect, abort, session, g, flash, Markup, json
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
    return "You are at the homepage of this API™!"

def retrieve_party(party_id= None):
    """
    Retrieve the party from whatever datastore
    """
    assert party_id is not  None
    party_data = {
            "partyid":party_id,
            "videos":[
                {"v":"ZZZZ","title":"papayas"},
                {"v":"AAAA","title":"bananas"},
            ]
    }
    return party_data


@app.route('/v1/get_party', defaults={"path": ""})
@app.route('/v1/get_party.<path:requestpath>')
def get_party(requestpath= None):
    """
    Retrieve the party for the given id.
    """
    #TODO: This get_party method is just a fake stub
    requested_id = request.args['pid']
    party_data = retrieve_party(requested_id)
    party_content = json.dumps(party_data)
    return render_template('json.html', data=party_content)


@app.route('/v1/add_vid')
def add_vid():
    """
    Add a video to the end of the playlist
    """
    party_data = retrieve_party("XXXX")
    video = {"v":request.params["v"], "title":"FOOBAR"}
    party_data["videos"].append(video) #TODO: check if this is in fact mutable.
    party_content = json.dumps(party_data)
    return render_template('json.html', data=party_content)


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
