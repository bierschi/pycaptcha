import logging
from pycaptcha import Captcha


class WordCaptcha(Captcha):
    """ class WordCaptcha to solve word captcha
    USAGE:
            word_captcha = WordCaptcha()

    """
    def __init__(self):
        self.logger = logging.getLogger('pycaptcha')
        self.logger.info('Create class WordCaptcha')

    def solve(self):
        pass

