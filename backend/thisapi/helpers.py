# -*- coding: utf-8 -*-

from flask import render_template, Markup, jsonify, json

def retrieve_party(party_id= None):
    """
    Retrieve the party from whatever datastore
    """
    party_data = {
            'partyid':party_id,
            "videos":[]
    }
    #TODO: Remove the mock below for something nicer
    if party_id is None or party_id == "647050":
        party_data = {
                'partyid':"647050",
                "videos":[
                    {"v":"ZZZZ","title":"papayas"},
                    {"v":"AAAA","title":"bananas"},
                ]
        }
    return party_data


def render_output(template= "pretty_json.html", data= None,oformat= "html"):
    """output whatever data comes in, in the format requested"""
    if oformat =="json":
        return jsonify(data)
    else:
        # If nothing said, just output a pretty html json viewer
        return render_template(template, data=data)


def get_vid_info(v= None):
    """Get information (title) of a video from the url"""
    assert v is not  None
    #TODO: this is a fake thing. retrieve info from youtube here
    vid = {
      "v": v,
      "title": "{0} title".format(v)
    }
    #app.logger.debug("This is Fake as Fak")
    return vid


def validate_v(v= None):
    """validate that the v given is legit and not hacky shit"""
    if v.isalnum():
        return v
    else:
        return None


def validate_pid(pid= None):
    """validate that the party id is valid"""
    if pid.isalnum():
        return pid
    else:
        return None
