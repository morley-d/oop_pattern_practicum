from tkinter import *
from creational.singleton import Singleton
import eqswindows
import footerwindow
import converterwindow
import decoratorwindow
import renderwindow


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
        self.button = Button(self, text='decorator', command=self.create_decorator)
        self.button.pack(expand=True)
        self.button = Button(self, text='facade', command=self.create_export_window)
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

    def create_decorator(self):
        global extraWindow
        extraWindow = decoratorwindow.Extra()

    def create_export_window(self):
        global extraWindow
        extraWindow = renderwindow.Extra()

    def __init__(self):
        print("calling from __init__")
