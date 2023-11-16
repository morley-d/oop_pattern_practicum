from tkinter import IntVar, Label, Toplevel, Checkbutton
from structural.decorator import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Rendering')
        self.geometry('200x700')
