from abc import ABC, abstractmethod


class Captcha(ABC):
    """Abstract Class Captcha

    """
    @abstractmethod
    def solve(self):
        pass
