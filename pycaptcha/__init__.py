__title__ = "pycaptcha"
__version_info__ = ('1', '0', '0')
__version__ = ".".join(__version_info__)
__author__ = "Christian Bierschneider"
__email__ = "christian.bierschneider@web.de"
__license__ = "MIT"

import os

from pycaptcha.captcha import Captcha
from pycaptcha.wordcaptcha import WordCaptcha
from pycaptcha.mathcaptcha import MathCaptcha


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
