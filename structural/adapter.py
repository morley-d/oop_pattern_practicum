from abc import ABCMeta, abstractmethod


class Audio(metaclass=ABCMeta):
    @abstractmethod
    def audioRecord():
        pass


class Midi():
    @abstractmethod
    def midiTrack():
        pass


class AudioTrack(Audio):
    def audioRecord(self):
        print("Audio is playing...")


class MidiTrack(Midi):
    def midiTrack(self):
        print("Midi is playing...")
