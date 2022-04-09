import sqlite3

# TODO: mõned asjad, mis peaks olema model_db, on hoopis controller_dbs
class Model_db:
    def __init__(self):
        self.db_name = 'words.db'
        self.connection = sqlite3.connect(self.db_name)
        
    def insert_value(self, word,cat):
        word = word.get()
        category = cat.get()
        #print(word, category)
        value = (f'{word}',f'{category}')
        #value = ('lambikas')
        sql = ''' INSERT INTO words(word,category)
              VALUES(?,?) '''
        cur = self.connection.cursor()
        cur.execute(sql, value)
        self.connection.commit()
        