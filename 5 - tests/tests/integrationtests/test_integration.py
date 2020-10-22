import json
import unittest 
import requests

from source.run import app
from source.application import db


class IntegrationTest(unittest.TestCase):
    def test_db(self):
        q = "SELECT 1"
        with app.app_context():
            self.assertEqual(db.session.execute(q).fetchall(), [(1,)])

    def test_api(self):
        url = 'http://localhost/'
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)
        expected = {'hello': 'DevOps'}
        self.assertEqual(expected, res.json())