import os
import sys
from pathlib import Path
from random import random
from tkinter import Canvas, Button, Toplevel, messagebox
import sqlite3
import random
import StaticVar

class Test(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.degerler = []
        self.old_questions = []
        self.dogru = 0
        self.yanlis = 0
        if StaticVar.question_type:
            self.question_int = 0
            self.answer_int = 1
        else:
            self.question_int = 1
            self.answer_int = 0
            
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"/Sources/Test")
        self.title("0 DOGRU 0 YANLIS")
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 324) // 2
        y = (screen_height - 283) // 2
        self.question_list = []
        self.geometry(f'{324}x{283}+{x}+{y}')
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)    
        self.canvas = Canvas(
            self,
            bg = "#B9B7BD",
            height = 283,
            width = 324,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)
        
        self.question =self.canvas.create_text(
            115.0,
            18.0,
            anchor="nw",
            text="ABHOLEN",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )
        self.button_1 = Button(
            self,
            background="#EEEDE7",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command= lambda : self.answering_the_question(self.button_1.cget("text"),self.question_list),
            text="test"
        )
        self.button_1.place(
            x=90.0,
            y=47.0,
            width=144.0,
            height=31.0
        )
        self.button_2 = Button(
            self,
            background="#EEEDE7",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command= lambda : self.answering_the_question(self.button_2.cget("text"),self.question_list),
            text="test"
        )
        self.button_2.place(
            x=90.0,
            y=95.0,
            width=144.0,
            height=31.0
        )
        self.button_3 = Button(
            self,
            background="#EEEDE7",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command= lambda : self.answering_the_question(self.button_3.cget("text"),self.question_list),
            text="test"
        )
        self.button_3.place(
            x=90.0,
            y=142.0,
            width=144.0,
            height=31.0
        )
        self.button_4 = Button(
            self,
            background="#EEEDE7",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command= lambda : self.answering_the_question(self.button_4.cget("text"),self.question_list),
            text="test"
        )
        self.button_4.place(
            x=90.0,
            y=190.0,
            width=144.0,
            height=31.0
        )
        self.getRandomQuestion()
        self.changeTheQuestion()
        
        
    def getRandomQuestion(self):
        
        while True:
            skip = True
            next_question= random.choice(data)
            if next_question in self.old_questions:
                skip = False
            if skip:
                self.question_list.append(next_question)
                self.old_questions.append(next_question)
                break
                
        x = 0
        
        while True:

            if x == 3 : break

            while True:
                skip = True
                current_question = random.choice(data)
                current_question_Tr = current_question[self.answer_int]
                for question in self.question_list:
                    if current_question_Tr == question[self.answer_int]:
                        skip = False
                        break
                if skip:
                    break
            self.question_list.append(current_question)
            x = x + 1
            
    def changeTheQuestion(self):
        
        de_question = self.question_list.copy()
        button_list = [self.button_1,self.button_2,self.button_3,self.button_4]
        for button in button_list:
            current_question = random.choice(de_question)
            de_question.remove(current_question)
            button.configure(text=current_question[self.answer_int])
        self.canvas.itemconfig(self.question,text="{}".format(self.question_list[0][self.question_int]))
        self.center_text()
            
    def answering_the_question(self,text,question_list):
        if text == question_list[0][self.answer_int]:
            print("dogru")
            self.dogru = self.dogru + 1
        else:
            for question in question_list:
                if question[self.answer_int] == text:
                    print("Senin seçimin {} {} \n dogru cevap : {}".format(text,question[self.question_int],question_list[0][self.answer_int]))
                    self.yanlis = self.yanlis + 1
                    self.show_warning("Senin seçimin {} = {} \n dogru cevap : {}".format(text,question[self.question_int],question_list[0][self.answer_int]))
                    
        self.title("{} DOGRU {} YANLIS".format(self.dogru,self.yanlis))
        if (self.dogru + self.yanlis) == 10:
            self.show_warning("DOGRU SAYIN : {} \n YANLIS SAYIN : {}".format(self.dogru,self.yanlis))
            self.destroy()
            self.parent.deiconify()
        self.question_list.clear()
        self.getRandomQuestion()
        self.changeTheQuestion()
    def center_text(self):
        bbox = self.canvas.bbox(self.question)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        new_x = (324 - text_width) // 2
        new_y = (50 - text_height) // 2
        self.canvas.coords(self.question, new_x, new_y)
        
    def show_warning(self, uyari):
        messagebox.showwarning("Yanlış", uyari)

def resource_path(relative_path):
    
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")  

    return os.path.join(base_path, relative_path)



if StaticVar.courseLevel == "A2":
    
     con = sqlite3.connect(resource_path("Sources/A2.db"))
     cur = con.cursor()
else:
    con = sqlite3.connect("A1.db")
    cur = con.cursor()

cur.execute("SELECT * FROM A{}".format(StaticVar.unit_int))
data = cur.fetchall()
con.close()
    
    



