import sqlite3

# TODO: mõned asjad, mis peaks olema model_db, on hoopis controller_dbs
class Model_db:
    def __init__(self):
        self.db_name = 'words.db'
        self.connection = sqlite3.connect(self.db_name)