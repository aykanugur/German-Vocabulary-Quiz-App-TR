from tkinter import Tk, Canvas, Button, PhotoImage
import StaticVar
import os
import sys
from tkinter.ttk import Combobox

class Menu(Tk):
    def __init__(self):
        super().__init__()
        self.title("Select Level")
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 217) // 2
        y = (screen_height - 324) // 2
        self.geometry(f'{217}x{324}+{x}+{y}')
        self.units = 1

        def resource_path(relative_path):
            try:
              base_path = sys._MEIPASS
            except Exception:
               base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        self.configure(bg = "#B9B7BD")
        self.canvas = Canvas(
            self,
            bg = "#B9B7BD",
            height = 284,
            width = 217,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_text(
            30.0,
            170.0,
            anchor="nw",
            text="Level(seviye) : {} ".format(StaticVar.courseLevel),
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )
        self.canvas.create_text(
            55.0,
            20.0,
            anchor="nw",
            text="Willkommen",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )
        self.canvas.create_text(
            55.0,
            230.0,
            anchor="nw",
            text="Ünite Seçin",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )
        
        self.button_image_1 = PhotoImage(file=resource_path("Sources/Button_Start.png"))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=self.startTest
        )
        self.button_1.place(
            x=30.0,
            y=50.0,
            width=156.0,
            height=40.0
        )
        self.button_image_2 = PhotoImage(file=resource_path("Sources/DE.png"))
        self.button_image_3 = PhotoImage(file=resource_path("Sources/TR.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=self.change_question_type
        )
        self.button_2.place(
            x=30.0,
            y=100.0,
            width=156.0,
            height=40.0
        )
        units = ["1", "2", "3", "4", "5", "6", "7", "8", "9","10","11","12","13","14"]
        self.comboBox_gender = Combobox(self, state="readonly", values=units)
        self.comboBox_gender.place(x=30, y=270, width=156.0, height=40.0)
        self.comboBox_gender.bind("<<ComboboxSelected>>",self.on_select_units)
        self.comboBox_gender.set(1)

    def on_select_units(self, event):
        StaticVar.unit_int = self.comboBox_gender.get()
    
        
    def startTest(self):
        import Test
        self.withdraw()
        test = Test.Test(parent=self)
        test.protocol("WM_DELETE_WINDOW", lambda: self.openMain(test))
        
    def change_question_type(self):
        if StaticVar.question_type:
            StaticVar.question_type = False
            self.button_2.configure(image=self.button_image_3)
        else:
            StaticVar.question_type = True
            self.button_2.configure(image=self.button_image_2)
    
    def openMain(self, test):
        self.deiconify()
        test.destroy()


        
        