from abc import ABCMeta, abstractmethod


class Audio(metaclass=ABCMeta):
    @abstractmethod
    def audioRecord():
        pass

class Midi():
    @abstractmethod
    def midiTrack():
        pass