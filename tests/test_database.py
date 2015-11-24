import sys
import os
sys.path.insert(0, os.path.dirname(__file__) + '/../')

import pytest
import database

class TestDatabase:

    def test_one(self):

        db = database.DataBase()
        db.removeAll()

        assert len(db.constraint) == 0
        assert len(db.listRu) == 0