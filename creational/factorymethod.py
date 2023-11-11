from abc import ABCMeta, abstractmethod


class Plugin(metaclass=ABCMeta):
    @abstractmethod
    def type():
        raise NotImplemented


class EffectPlugin(Plugin):
    def __init__(self):
        self.type = "Effect"

    def type(self):
        return self.type


class SynphPlugin(Plugin):
    def __init__(self):
        self.type = "Synph"

    def type(self):
        return self.type
