import logging

from pycaptcha import Captcha


class MathCaptcha(Captcha):
    """ class MatchCaptcha to solve math captcha
    USAGE:
            math_captcha = MathCaptcha()

    """
    def __init__(self):
        self.logger = logging.getLogger('pycaptcha')
        self.logger.info('Create class MathCaptcha')

    def solve(self):
        """

        :return:
        """
        pass
