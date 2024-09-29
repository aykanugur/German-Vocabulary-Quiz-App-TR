from tkinter import Tk, Canvas, Button, PhotoImage
import StaticVar
import sys
import os

class Start(Tk):
    def __init__(self):
        super().__init__()
        self.title("Select Level")
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 440) // 2
        y = (screen_height - 179) // 2
        self.geometry(f'{440}x{179}+{x}+{y}')


        def resource_path(relative_path):
            try:
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)
        
        self.canvas = Canvas(
        self,
        bg = "#B9B7BD",
        height = 179,
        width = 440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_text(
        150.0,
        21.0,
        anchor="nw",
        text="Select your level",
        fill="#000000",
        font=("Inter Bold", 20 * -1)
        )

        self.canvas.create_text(
        150.0,
            56.0,
            anchor="nw",
            text="Seviyenizi Secin",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
             )
        self.button_image_1 = PhotoImage(file=resource_path("Sources/Button_A2.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=self.A2
            
        )
        button_1.place(
            x=227.0,
            y=90.0,
            width=160.0,
            height=41.0
        )
        self.button_image_2 = PhotoImage(file=resource_path("Sources/Button_A1.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=self.A1
        )
        button_2.place(
            x=59.0,
            y=90.0,
            width=160.0,
            height=41.0
        )
    def A1(self):
        StaticVar.courseLevel = "A1"
        self.destroy()
    def A2(self):
        StaticVar.courseLevel = "A2"
        self.destroy()
        







