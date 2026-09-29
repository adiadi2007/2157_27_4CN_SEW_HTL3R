# Metadaten
__author__ = 'Adi Velagic'
__example__ = "SEW4/01/1"
__date__ = "24.09.2026"
__version__ = "1.0"
__license__ = "GNU GPLv3"
__status__ = "Released"

import doctest


def is_palindrom(s: str) -> bool:
    """
        >>> is_palindrom("otto")
        True
        >>> is_palindrom("haus")#
        False
        >>> is_palindrom("abca")
        False
    """
    return s == s[::-1]


def is_palindrom_sentence(sentence: str) -> bool:
    """
            >>> is_palindrom_sentence("Was it a car or a cat I saw?")
            True
            >>> is_palindrom_sentence("Hallo, Ich heisse Adi")
            False
            >>> is_palindrom_sentence("Madam, I'm Adam")
            True
        """
    a = ""
    for i in sentence:
        if i.isalnum():
            a += i.upper()
    return is_palindrom(a)


def palindrom_product(x) -> int | float:
    """
        >>> palindrom_product(1000000)
        906609
        >>> palindrom_product(100000)
        99999
    """
    big = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            p = i * j
            if x > p > big and is_palindrom(str(p)):
                big = p
    return big


def to_base(number: int, base: int) -> str:
    """
    :param number: Zahl im 10er-Syste,
    :param base: Zielsystem (maximal 36)
    :return: Zahl im Zielsystem als String
    >>> to_base(1234,16)
    '4D2'
    >>> to_base(3646,16)
    'E3E'
    """
    num = ""
    index = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while number != 0:
        num = index[number % base] + num
        number //= base
    return num



def get_dec_hex_palindrom(x):
    """
        >>> get_dec_hex_palindrom(354)
        353
        >>> get_dec_hex_palindrom(353)
        11
    """
    for i in range(x-1, 0, -1):
        if is_palindrom(str(i)) and is_palindrom(to_base(i, 16)):
            return i

if __name__ == "__main__":
    doctest.testmod()
