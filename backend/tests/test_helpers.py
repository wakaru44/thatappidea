# -*- conding: utf-8 -*-

import json
import unittest
from thisapi import helpers as th

class BT(unittest.TestCase):
    def setUp(self):
        pass

class test_validate(BT):
    def test_a_valid_pid_is_cool(self):
        pid = "647050"
        assert th.validate_pid(pid) == pid
        pid = "123456"
        assert th.validate_pid(pid) == pid
        pid = "AAAAAA"
        assert th.validate_pid(pid) == pid

    def test_an_invalid_pid_returns_none(self):
        pid = "WhatTheFuck!!"
        print th.validate_pid(pid)
        assert th.validate_pid(pid) is None
        pid = "10.="
        assert th.validate_pid(pid) is None


class test_validate_v(BT):
    def test_a_valid_v_is_cool(self):
        """A valid video id is passed."""
        # A better video id format might be required in the future
        v = "aoeu141"
        assert th.validate_v(v) == v

    def test_an_invalid_v_returns_none(self):
        """A video id containing special characters might be h4x0r shit"""
        v = "!]{}"
        assert th.validate_v(v) is None


class test_(BT):
    def test_(self):
        pass
