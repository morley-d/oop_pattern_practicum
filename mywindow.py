from tkinter import *
from creational.singleton import Singleton
import eqswindows
import footerwindow
import converterwindow


class Window(Tk, Singleton):
    def init(self):
        print("calling from init")
        super().__init__()
        self.button = Button(self, text='open eqs window', command=self.create_window_eqs)
        self.button.pack(expand=True)
        self.button = Button(self, text='open footer', command=self.create_footer_eqs)
        self.button.pack(expand=True)
        self.button = Button(self, text='converter', command=self.create_converter)
        self.button.pack(expand=True)

    def create_window_eqs(self):
        global extraWindow
        extraWindow = eqswindows.Extra()

    def create_footer_eqs(self):
        global extraWindow
        extraWindow = footerwindow.Extra()
    
    def create_converter(self):
        global extraWindow
        extraWindow = converterwindow.Extra()

    def __init__(self):
        print("calling from __init__")
