from tkinter import *
from creational.singleton import Singleton
import eqswindows


class Window(Tk, Singleton):
    def init(self):
        print("calling from init")
        super().__init__()

        self.button = Button(self, text='open eqs window', command=self.create_window_eqs)
        self.button.pack(expand=True)

    def create_window_eqs(self):
        global extraWindow
        extraWindow = eqswindows.Extra()

    def __init__(self):
        print("calling from __init__")
