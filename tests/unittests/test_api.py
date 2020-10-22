import json
import datetime
import unittest 
from unittest.mock import patch

from source.run import app
from source.models import RawData
from source.application import db


class ApiTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(1, 1)


    def test_index(self):
        res = app.test_client().get('/')
        self.assertEqual(res.status_code, 200)
        expected = {'hello': 'DevOps'}
        self.assertEqual(expected, json.loads(res.get_data(as_text=True)))


    @patch('flask_sqlalchemy._QueryProperty.__get__')
    def test_read(self, queryMock):
        queryMock\
        .return_value.all\
        .return_value = [
            RawData(ins_datetime="Orario di test", raw_data="{\"partecipanti\": \"2\"}")
        ]
        
        res = app.test_client().get('/read')

        self.assertEqual(res.json, {
            "data": [
                {
                "ins_datetime": "Orario di test",
                "raw_data": "{\"partecipanti\": \"2\"}"
                }
            ]
        })

    def test_insert(self):
        old = db.session.commit
        db.session.commit = db.session.flush
        test_json = {'ins_datetime': 'orario di test', 'raw_data': 'test_data'}
        res = app.test_client().post('/insert', json=test_json)
        self.assertEqual(res.json, {'data': test_json})
        db.session.commit = old