class Entity():
    def __init__(self, sound):
        self.sound = sound

    def play(self, sound):
        return self.sound
    

class EQ(Entity):
    def __init__(self, eqed):
        self.eqed = eqed

    def play(self):
        return "EQ[{}]".format(self.eqed.play)
