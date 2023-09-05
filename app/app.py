from tkinter import *

from functions.buttons import ButtonsEvent
from functions.save_file import SaveFile
from functions.render import Render

app = Tk()
app.title('Automação GitHub')
app.resizable(width=False, height=False)
app.geometry('450x300+100+100')


files = SaveFile()
buttons = ButtonsEvent(files)
render = Render(app, buttons)


render.rendering_one()


app.mainloop()