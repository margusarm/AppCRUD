from Model_db import *
from View_db import *
from tkinter import simpledialog

class Controller_db:
        
    def __init__(self):
        self.model_db = Model_db()
        self.view_db = View_db(self)
            
    def main(self):
        self.view_db.main() 
    
    
    #annab teada, mis on kirje id andmebaasis ja muudab update ja delete buttoni aktiivseks
    def view_button_id(self): 
        self.view_db.delete_button().config(state=NORMAL)
        self.view_db.update_button().config(state=NORMAL)
        return self.view_db.var.get()
    
    #results canvase pealt kustutatakse kõik ja laetakse andmebaasist uuesti
    def reload_table(self):
        for widgets in self.view_db.r_canvas.winfo_children():
            widgets.destroy()
        self.view_db.view_values()
    
    #võtab id jaoks vajutatud radio buttonile salvestatud id ja kasutab seda andmebaasist kustutamiseks    
    def delete_value(self):
        id = self.view_db.var.get()
        sql = ''' DELETE FROM words WHERE id=?'''
        cur = self.model_db.connection.cursor()
        cur.execute(sql, (id,))
        self.model_db.connection.commit()
        #self.view_db.e.grid_forget() #kustutab aknas sõna
        #self.view_db.rb.grid_forget() #kustutab aknas sõna ees radio buttoni
        #print(id)
        self.reload_table()
    
    #sama, mis üleval, aga updateb
    def update_value(self):
        new_word = simpledialog.askstring('Vaheta sõna', 'Sisesta uus sõna: ')
        update = (f'{new_word} ',f'{self.view_db.var.get()}') #paneb kokku execute jaoks õigesse formaati ning lisab juurde db id kirje.
        sql = ''' UPDATE words SET word = ? WHERE id = ?'''
        cur = self.model_db.connection.cursor()
        cur.execute(sql, update)
        self.model_db.connection.commit()
        self.reload_table()
        #print(update)
    
    #lisab kirje andmebaasi    
    def insert_value(self):
        word = simpledialog.askstring('Uus sõna', 'Sisesta uus sõna: ')
        category = simpledialog.askstring(f'{word}', f'Sisesta kategooria sõnale\n *{word}* ')
        value = (f'{word}',f'{category}')
        #value = ('lambikas')
        sql = ''' INSERT INTO words(word,category)
              VALUES(?,?) '''
        cur = self.model_db.connection.cursor()
        cur.execute(sql, value)
        self.model_db.connection.commit()
        self.reload_table()
        

        
        
        
        
    
    
        
    
        
    
        
   