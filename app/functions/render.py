from tkinter import *

from functions.buttons import ButtonsEvent


class Render:
    def __init__(self, app: dict, buttons: ButtonsEvent):
        self.app = app
        self.buttons = buttons

    def rendering_one(self):
        msg_one = Label(
            self.app,
            text='Para começar, preciso que você digite o nome de usuario do GITHUB.'
        )
        msg_two = Label(
            self.app,
            text='Você deve digitar APENAS o nome de usuario. EX: Rocketseat, netlify:'
        )
        msg_one.grid(column=0, row=1, sticky="w")
        msg_two.grid(column=0, row=2, sticky="w")

        value = Entry(self.app, width=20)
        value.grid(column=0, row=3, sticky="w", padx=10, pady=35)

        btn_ok = Button(
            self.app,
            text='Procurar',
            command=lambda: self.buttons.btn_search(value, self.app, self.rendering_two)
        )
        btn_ok.grid(column=0, row=3, sticky='', pady=35)

    def rendering_two(self):
        msg = Label(
            self.app,
            text='Digite, APENAS o nome, do arquivo que sera salvo em (.csv e .json):'
        )
        msg.grid(column=0, row=1, sticky="w")

        value = Entry(self.app, width=20)
        value.grid(column=0, row=3, sticky="w", padx=10, pady=35)

        btn = Button(
            self.app,
            text='Salvar',
            command=lambda: self.buttons.btn_save(value, self.app)
        )
        btn.grid(column=0, row=3, sticky='', pady=35)