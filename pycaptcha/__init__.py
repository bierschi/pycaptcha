__title__ = "pycaptcha"
__version_info__ = ('1', '0', '0')
__version__ = ".".join(__version_info__)
__author__ = "Christian Bierschneider"
__email__ = "christian.bierschneider@web.de"
__license__ = "MIT"

from pycaptcha.wordcaptcha.word_captcha import WordCaptcha
from pycaptcha.mathcaptcha.math_captcha import MathCaptcha
from pycaptcha.recaptcha.recaptcha import ReCaptcha