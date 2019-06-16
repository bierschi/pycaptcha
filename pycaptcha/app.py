from pycaptcha.wordcaptcha.word_captcha import WordCaptcha
from pycaptcha.mathcaptcha.math_captcha import MathCaptcha
from pycaptcha.recaptcha.audio import AudioRecaptcha
from pycaptcha.recaptcha.image import ImageRecaptcha


def main():
    print("test")
    AudioRecaptcha(language='en-US').solve()


if __name__ == '__main__':
    main()
