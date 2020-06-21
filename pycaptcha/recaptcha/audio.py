from pycaptcha.captcha import Captcha
from pycaptcha.recaptcha.audio_handler.audio_data import AudioFile
from pycaptcha.recaptcha.audio_handler.recognizer import Recognizer
from pycaptcha import ROOT_DIR


class AudioRecaptcha(Captcha):

    def __init__(self, language='en-US'):

        self.language = language
        self.recognizer = Recognizer()

    def solve(self):

        # find recaptcha audio button and load file

        # get loaded speech file
        resp_text = self.load_file(audio_file=ROOT_DIR + '/recaptcha/audio_handler/cpu.wav')
        print(resp_text)

        # insert text into input text field

    def load_file(self, audio_file):

        with AudioFile(audio_file) as source:
            audio = self.recognizer.record(source)

        return self.recognizer.recognize_google(audio, language='en-US')
