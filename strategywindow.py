from tkinter import *
from behavioral.observer import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Group')
        self.geometry('640x480')
