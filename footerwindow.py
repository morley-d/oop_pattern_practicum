from tkinter import *
from creational.factorymethod import *


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Footer bar')
        self.geometry('1280x200')
        self.button = Button(self, text="Drug plugin here", command=self.show_plugins)
        self.button.pack(expand=True)

    def show_plugins(self):
        pass
