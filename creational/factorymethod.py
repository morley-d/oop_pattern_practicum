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


class Creator:
    @staticmethod
    def Factory(type):
        if type == "Effect":
            return EffectPlugin()
        elif type == "Synph":
            return SynphPlugin()
        return None
