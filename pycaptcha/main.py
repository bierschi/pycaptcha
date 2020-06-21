from pycaptcha import WordCaptcha, MathCaptcha
from pycaptcha.utils import Logger


def main():

    # set up logger instance
    logger = Logger(name='pycaptcha', level='info', log_folder='/var/log/')
    logger.info("Start application pycaptcha")

    ca = WordCaptcha()
    ca.solve()
    ma = MathCaptcha()
    ma.solve()

if __name__ == '__main__':
    main()
