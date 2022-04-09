from cgitb import text
import tkinter
from unicodedata import category
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
    #grid_forget() oli alguses plaanis, aga see jätab tegelikult mällu alles ja saab taastoota - võib segadust tekitada
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
        self.reload_table()
        self.view_db.delete_button().config(state=DISABLED)
        self.view_db.update_button().config(state=DISABLED)
    
    #sama, mis üleval, aga updateb
    def update_value(self):
        new_word = simpledialog.askstring('Vaheta sõna', 'Sisesta uus sõna: ')
        update = (f'{new_word} ',f'{self.view_db.var.get()}') #paneb kokku execute jaoks õigesse formaati ning lisab juurde db id kirje.
        sql = ''' UPDATE words SET word = ? WHERE id = ?'''
        cur = self.model_db.connection.cursor()
        cur.execute(sql, update)
        self.model_db.connection.commit()
        self.reload_table()
        self.view_db.update_button().config(state=DISABLED)
        self.view_db.delete_button().config(state=DISABLED)
        #print(update)
    
    #lisab kirje andmebaasi 
        
        
    def ask_value (self):
        ask = tkinter.Tk()
        ask.title('Uue sõna lisamine')
        ask.geometry('350x150')
        ask.resizable(0,0)
        global word, cat
        
        wordLabel = Label(ask, text= 'Sisesta uus sõna', pady=5, padx=5)
        wordLabel.grid(row=0, column=0)
        
        word = Entry(ask, width=30)
        word.grid(row=0, column=1)
        
        categoryLabel = Label(ask, text= 'Sisesta sõna kategooria', pady=5, padx=5)
        categoryLabel.grid(row=1, column=0)
        
        cat = Entry(ask, width=30)
        cat.grid(row=1, column=1)
        
        btn2 = Button(ask, text='Sisesta', command=lambda:self.close_ask(ask, word, cat), pady=5,padx=5)
        btn2.grid(row=3, column=1)
        
    def close_ask (self, ask, word, cat):
        self.model_db.insert_value(word, cat)
        ask.destroy()
        self.reload_table()

        
        
        
        
    
    
        
    
        
    
        
   