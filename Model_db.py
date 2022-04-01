import sqlite3

class Model_db:
    def __init__(self):
        self.db_name = 'words.db'
        self.connection = sqlite3.connect(self.db_name)