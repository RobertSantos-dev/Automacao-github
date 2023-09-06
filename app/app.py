from tkinter import *

from functions.buttons import ButtonsEvent
from functions.save_file import SaveFile
from functions.render import Render
from utils.constant import Constant


app = Tk()
app.title('Automação GitHub')
app.configure(bg=Constant.background)
app.resizable(width=False, height=False)
app.geometry('500x320+100+100')
app.grid_columnconfigure(0, weight=1)


files = SaveFile()
buttons = ButtonsEvent(files)
render = Render(app, buttons)


render.rendering_one()


app.mainloop()