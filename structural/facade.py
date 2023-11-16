from pathlib import Path

class MP3:
    def process(self):
        print("Processing MP3")
        Path("filenmae.mp3").touch()


class WAV:
    def process(self):
        print("Processing WAV")
        Path("filenmae.wav").touch()


class Data:
    def process(self):
        print("Processing analisys")
        Path("filenmae.dbbs").touch()


class Render:
    def __init__(self):
        self.mp3 = MP3()
        self.wav = WAV()
        self.data = Data()

    def startRendering(self):
        self.mp3.process()
        self.wav.process()
        self.data.process()