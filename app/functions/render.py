import os
from tkinter import *

from functions.buttons import ButtonsEvent
from utils.constant import Constant


class Render:
    def __init__(self, app: dict, buttons: ButtonsEvent):
        self.app = app
        self.buttons = buttons

    # def __logo(self):
    #     path = os.getcwd()
    #     img = PhotoImage(file=f'{path}/app/assets/Mondev.png', width=100, height=147)
    #     render = Label(self.app, image=img)
    #     render.grid(row=0)

    def rendering_one(self):
        # self.__logo()
        msg_one = Label(
            self.app,
            text='Para começar, preciso que você digite o nome de usuario do GITHUB.',
            fg=Constant.foreground,
            bg=self.app.cget('bg')
        )
        msg_two = Label(
            self.app,
            text='Você deve digitar APENAS o nome de usuario. EX: Rocketseat, netlify:',
            fg=Constant.foreground,
            bg=self.app.cget('bg')
        )
        msg_one.grid(column=0, row=1, padx=10)
        msg_two.grid(column=0, row=2, padx=10)

        value = Entry(self.app, width=25)
        value.grid(column=0, row=3, padx=10, pady=(35, 2))

        btn_ok = Button(
            self.app,
            text='Procurar',
            command=lambda: self.buttons.btn_search(value, self.app, self.rendering_two),
            borderwidth=0,
            bg=Constant.pink
        )
        btn_ok.grid(column=0, row=4)

    def rendering_two(self):
        # self.__logo()
        msg = Label(
            self.app,
            text='Digite, APENAS o nome, do arquivo que sera salvo em (.csv e .json):',
            fg=Constant.foreground,
            bg=self.app.cget('bg')
        )
        msg.grid(column=0, row=1)

        value = Entry(self.app, width=25)
        value.grid(column=0, row=3, padx=10, pady=(35, 2))

        btn = Button(
            self.app,
            text='Salvar',
            command=lambda: self.buttons.btn_save(value, self.app),
            borderwidth=0,
            bg=Constant.pink
        )
        btn.grid(column=0, row=4)