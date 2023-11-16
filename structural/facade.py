class MP3:
    def process(self):
        print("Processing MP3")


class WAV:
    def process(self):
        print("Processing WAV")


class Data:
    def process(self):
        print("Processing analisys")


class Render:
    def __init__(self):
        self.mp3 = MP3()
        self.wav = WAV()
        self.data = Data()

    def startRendering(self):
        self.mp3.process()
        self.wav.process()
        self.data.process()
