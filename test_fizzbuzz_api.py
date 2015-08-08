import unittest
import flask
class TestRounting(unittest.TestCase):
    def test_fail(self):
        self.app = app.test_client()
        rv = self.app.get('/')
