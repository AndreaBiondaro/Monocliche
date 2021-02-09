import random
import string


class Utils:

    @staticmethod
    def random_string(size: int) -> str:
        """
        Generates a string of variable size, the created string is composed of ascii letters and numbers
        """
        return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(size))
