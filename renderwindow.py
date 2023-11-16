from tkinter import *
from structural.facade import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Rendering')
        self.geometry('200x700')
        self.button = Button(self, text='Drug plugin here', command=self.show_plugins)
        self.button.pack(expand=True)
    
    def start_rendering(self):
        renderTrack = Render()
        renderTrack.startRendering()
