from textwrap import fill
from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import askstring
from turtle import bgcolor
from Model_db import *

class View_db(Tk):
    
    def __init__(self, controller_db):
        super().__init__()
        self.model_db = Model_db()
        self.controller_db = controller_db
        #main window
        self.minsize(300, 200) #sellest väiksemaks ei saa akent teha
        self.resizable(True, True)
        self.title('Words CRUD')
        
        #frames & canvases | tegin canvastega selle pärast, et leidsin mõnusama viisi, kuidas aken käitub, kui teda suurendada
        self.first_frame = self.frame_1()
        self.second_frame = self.frame_2() #see on disabletud selle pärast, et hetkel kadus selle vajadus ära, aga veel ära ei kustuta, võib paranduse käigus vaja minna
        self.r_canvas = self.results_canvas()
        self.b_canvas = self.buttons_canvas()
        
        #widgets
        self.view_values()
        
        #buttons
        self.delete_button()
        self.update_button()
        self.insert_button()
        
    def main(self):
        self.mainloop()
        
    def frame_1(self):
        frame = Frame(self)
        frame.pack(expand = True, fill='both', pady=10)
        return frame
    
    def frame_2(self):
        frame = Frame(self)
        frame.pack(expand = True, fill='both', pady=10)
        return frame
    
    def results_canvas(self):
        canvas = Canvas(self.first_frame)
        canvas.place(relx=0.5, anchor=N)
        #scrollbar ei saand tööle, siin õpetus, kuidas peaks saama: https://stackoverflow.com/questions/7727804/tkinter-using-scrollbars-on-a-canvas
        v_scroll = ttk.Scrollbar(self.first_frame, orient='vertical', command=canvas.yview)
        v_scroll.pack(side='right',fill='y')
        canvas.config(yscrollcommand=v_scroll.set)
        
        return canvas
    
    def buttons_canvas(self):
        canvas = Canvas(self.first_frame)
        canvas.place(relx=0.5, rely=1.0, anchor=S) #all keskel
        return canvas
        
    def view_values(self):
        set = self.model_db.connection.execute('select id,word,category from words')
        #keys = list(map(lambda x: x[0], set.description)) #võtab päringust välja tulba pealkirjad
        keys = [description[0] for description in set.description] #alternatiivne meetod sql päringust pealkirjade võtmiseks, tundub lihtsam meelde jätta
        bi = 1
        self.i = 1
        self.var = IntVar() #siin oli vahepeal vaja meetodi väliseks teha, aga see vajadus langes ära. hetkel jätan nii, palju ei muutu
        self.set=set.fetchall() # peab vahepeal fetchall tegema, muidu teine for loop ei tööta (tühi)
        # TODO #6 kogu see aken peab olema selline, et ei saaks klikkida mujal, kui rb ja nupud
        self.heading_word = Entry(self.r_canvas,relief=RAISED, bg='#F1F1F1', justify=CENTER)
        self.heading_word.grid(row=0,column=1)
        self.heading_word.insert(END,keys[1].capitalize())
        self.heading_category = Entry(self.r_canvas,relief=RAISED, bg='#F1F1F1', justify=CENTER)
        self.heading_category.grid(row=0,column=2)
        self.heading_category.insert(END,keys[2].capitalize())
        
        
        for value in self.set:
            #print(value[0])
            self.rb = Radiobutton(self.r_canvas, variable = self.var, value=value[0], 
                                   command=lambda:self.controller_db.view_button_id())  # siin tehakse radiobutton, mille külge pannakse var'ga db võetud id, 
                                                                                        #valides toimub controllerisse selle id saatmine
            self.rb.grid(row=bi, column=0)
            bi += 1
        
        for r in self.set:   #for loop nimetuste lugemiseks ja kuvamiseks
            self.e = Entry(self.r_canvas, bd=0, bg='#F1F1F1', justify=CENTER)
            self.e2= Entry(self.r_canvas, bd=0, bg='#F1F1F1', justify=CENTER)
            self.e.grid(row=self.i, column=1)
            self.e2.grid(row=self.i, column=2)
            self.e.insert(END,r[1])
            self.e2.insert(END,r[2])
            self.i += 1

        #selle jätan siia praegu alles, sest on hea koodijupp, millega saab teha mitme tulbaga tabelit.
        ''''
            for j in range(len(value)):     
                e = Entry(self.first_frame, bd=0, justify=CENTER)
                e.grid(row=i, column=j+1, sticky=NSEW) # siin peab columnile +1 panema, sest muidu läheb eelmises for loopis tehtud buttoni peale
                e.insert(END, value[j])
            i += 1
        '''
    def delete_button(self):
        b = Button(self.b_canvas, text='Delete', command=lambda:self.controller_db.delete_value(), state=DISABLED) # Delete ja Update peavad alguses olema disabletud, sest kui radiobutton pole valitud, pole midagi kustutada
        b.grid(row=0, column=0, padx = 5, pady = 5)
        return b
        
    def update_button(self):
        b = Button(self.b_canvas, text='Update', command=lambda:self.controller_db.update_value(), state=DISABLED)
        b.grid(row = 0, column = 1, padx = 5, pady = 5)
        return b
        
    def insert_button(self):
        b = Button(self.b_canvas, text='Insert', command=lambda:self.controller_db.insert_value())
        b.grid(row = 0, column = 2, padx = 5, pady = 5)
        return b
        

       

    
        
    

    