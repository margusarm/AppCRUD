from textwrap import fill
from tkinter import *
from tkinter.simpledialog import askstring
from Model_db import *

class View_db(Tk):
    
    def __init__(self, controller_db):
        super().__init__()
        self.model_db = Model_db()
        self.controller_db = controller_db
        #main window
        self.minsize(250, 400) #sellest väiksemaks ei saa akent teha
        self.resizable(True, True)
        self.title('Words CRUD')
        
        #frames & canvases | tegin canvastega selle pärast, et leidsin mõnusama viisi, kuidas aken käitub, kui teda suurendada
        self.first_frame = self.frame_1()
        #self.second_frame = self.frame_2() #see on disabletud selle pärast, et hetkel kadus selle vajadus ära, aga veel ära ei kustuta, võib paranduse käigus vaja minna
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
        return canvas
    
    def buttons_canvas(self):
        canvas = Canvas(self.first_frame)
        canvas.place(relx=0.5, rely=1.0, anchor=S) #all keskel
        return canvas
        
    def view_values(self): # TODO #4 andmetest vaja võtta ka veeru pealkirjad ja teine veerg
        #!!!! vaata mingi samamoodi nagu on Entry ja Button on ka Canvas, sellega saab vast kõik keskele
        set = self.model_db.connection.execute('select id,word from words')
        bi = 0
        self.i = 0
        self.var = IntVar() #siin oli vahepeal vaja meetodi väliseks teha, aga see vajadus langes ära. hetkel jätan nii, palju ei muutu
        self.set=set.fetchall() # peab vahepeal fetchall tegema, muidu teine for loop ei tööta (tühi)
        for value in self.set:
            #print(value[0])
            self.rb = Radiobutton(self.r_canvas, variable = self.var, value=value[0], 
                                   command=lambda:self.controller_db.view_button_id())  # siin tehakse radiobutton, mille külge pannakse var'ga db võetud id, 
                                                                                        #valides toimub controllerisse selle id saatmine
            self.rb.grid(row=bi, column=0)
            bi += 1
        
        for r in self.set:   #for loop nimetuste lugemiseks ja kuvamiseks
            self.e = Entry(self.r_canvas, bd=0, bg='#F1F1F1', justify=CENTER)
            self.e.grid(row=self.i, column=1)
            self.e.insert(END,r[1])
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
        b = Button(self.b_canvas, text='Delete', command=lambda:self.controller_db.delete_value(), state=DISABLED)
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
        

       

    
        
    

    