from tkinter import *

app = Tk()
app.title('Automação GitHub')
app.resizable(width=False, height=False)
app.geometry('450x300+100+100')


msg_one = Label(app, text='Para começar, preciso que você digite o nome de usuario do GITHUB.')
msg_one.grid(column=0, row=1, sticky="w")

msg_two = Label(app, text='Você deve digitar APENAS o nome de usuario. EX: Rocketseat, netlify:')
msg_two.grid(column=0, row=2, sticky="w")


value = Entry(app, width=20)
value.grid(column=0, row=3, sticky="w", padx=10, pady=35)

btn_ok = Button(app, text='Procurar', height=1, command='')
btn_ok.grid(column=0, row=3, sticky='', pady=35)

app.mainloop()