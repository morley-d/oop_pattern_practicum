class Observable:
    def __init__(self):
        self.observers = []

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)


class Compressor(Observable):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.gane = 0

    @property
    def gain(self):
        return self.gain
    
    @gain.setter
    def setGain(self, value):
        self._gane = value
        self.notify()


class Kick:
    def __init__(self):
        self.name = "Kick"

    def update(self, subject):
        print(f"Kick: Subject {subject.name} has data: gain {subject.setGain}")

    # @property
    # def name(self):
    #     return self.name
