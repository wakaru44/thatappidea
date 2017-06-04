# -*- conding: utf-8 -*-

import os
import tempfile
import unittest
import thisapi  # This is imported thanks to the magic in __init__
import json

class ThisApiTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fp, thisapi.app.config["DATABASE"]= tempfile.mkstemp()
        thisapi.app.config['TESTING'] = True
        self.app = thisapi.app.test_client()
        with thisapi.app.app_context():
            thisapi.init_db()

    def tearDown(self):
        os.close(self.db_fp)
        os.unlink(thisapi.app.config["DATABASE"])


class TestRootPath(ThisApiTestCase):
    def test_simple_get(self):
        rv = self.app.get("/")
        assert "You are at the homepage" in rv.data


class TestGetPartyEndpoint(ThisApiTestCase):
    def setUp(self):
        super(TestGetPartyEndpoint, self).setUp()
        # create a fake party
        self.pid="647050"
        self.party_data = {
                'partyid':self.pid,
                "videos":[
                    {"v":"ZZZZ","title":"papayas"},
                    {"v":"AAAA","title":"bananas"},
                ]
        }
        create = self.app.put("add_vid", self.party_data)

    def test_a_new_party_is_empty(self):
        """test a new party returns an empty party"""
        rv = self.app.get("/v1/get_party.json?pid=999999")
        print rv.data
        assert json.loads(rv.data) is not None
        assert len(json.loads(rv.data)["videos"]) == 0

    def test_a_json_request_returns_valid_json(self):
        """a json request returns valid json"""
        pid="647050"
        rv = self.app.get("/v1/get_party.json?pid={0}".format(pid))
        assert pid in rv.data
        assert json.loads(rv.data) is not  None
        assert len(json.loads(rv.data)) != 0

    def test_an_html_request_returns_html(self):
        """test a new party returns an empty json"""
        pid="647050"
        rv = self.app.get("/v1/get_party?pid={0}".format(pid))
        assert pid in rv.data
        self.assertRaises(ValueError, json.loads, rv.data)

class TestPutPartyEndpoint(ThisApiTestCase):
    def setUp(self):
        super(TestPutPartyEndpoint, self).setUp()

    def test_a_valid_pid_returns_a_party_with_the_vid_in_last(self):
        """a valid pid returns a party with the video"""
        pid="647050" # this is our demo party
        vidid="newvideolink"
        rv = self.app.put("/v1/add_vid.json?new_vid={0}&party_id={1}".format(vidid,pid))
        #rv = self.app.post("/v1/add_vid",data=dict(nev_vid=vidid,party_id=pid))
        print "data"
        print rv.data
        print "status"
        print rv.status
        assert "200" in rv.status
        assert pid in rv.data
        assert "newvideolink" in rv.data
        assert len(json.loads(rv.data)["videos"]) > 1
        vid = {"v":"newvideolink", "title":"{0} title".format(vidid)}
        assert json.loads(rv.data)["videos"][-1] == vid

    def test_an_invalid_pid_returns_error(self):
        """an invalid pid returns the demo party"""
        pid="WhatTheFuck!!!"
        vidid="newvideolink"
        rv = self.app.put("/v1/add_vid.json?new_vid={0}&party_id={1}".format(vidid,pid))
        print rv.data
        print rv.status
        assert "647050" in rv.data



if __name__=="__main__":
    unittest.main()
