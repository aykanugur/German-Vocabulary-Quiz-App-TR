import Start
import StaticVar
import Menu

start = Start.Start()
start.mainloop()

if StaticVar.courseLevel is not None:
    menu = Menu.Menu()
    menu.mainloop()