from pycaptcha.recaptcha.audio_handler.audio_data import AudioFile
from pycaptcha.recaptcha.audio_handler.recognizer import Recognizer


class SpeechToText:

    def __init__(self):

        self.recognizer = Recognizer()


    def load_file(self, audio_file):

        with AudioFile(audio_file) as source:
            audio = self.recognizer.record(source)

        #self.recognizer.recognize_google(audio, language=)