# -*- conding: utf-8 -*-

import os
import tempfile
import unittest
import thisapi  # dunno how the uck gonna import this

class ThisApiTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fp, thisapi.app.config["DATABASE"]= tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = thisapi.app.test_client()
        with thisapi.app.app_context():
            thisapi.init_db()

    def tearDown(self):
        os.close(self.db_fp)
        os.unlink(thisapi.app.config["DATABASE"])


if __name__=="__main__":
    unittest.main()
