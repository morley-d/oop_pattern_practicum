from tkinter import *
from behavioral.observer import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Group')
        self.geometry('640x480')
        self.compressor = Compressor("Compressor")
        self.kick = Kick()
        l = Label(self, text=f"change Gain of the {self.kick.name}")
        l.pack()
        scale = Scale(self, command=self.change_gain, from_=0, to=100)
        scale.pack()

    def change_gain(self, gain = 0):
        self.compressor.attach(self.kick)
        self.compressor.setGain = int(gain)
