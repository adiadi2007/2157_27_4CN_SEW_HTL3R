# Metadaten
__author__ = 'Adi Velagic'
__example__ = "SEW4/01/2"
__date__ = "24.09.2026"
__version__ = "1.0"
__license__ = "GNU GPLv3"
__status__ = "Released"

import doctest


def collatz(n) -> int:
    """
            >>> collatz(19)
            58
            >>> collatz(1)
            4
    """
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1  #
    return n

def collatz_sequence(number: int) -> List[int]:
    """
    >>> collatz_sequence(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    """
    ergb = [number]
    while number != 1:
        number = collatz(number)
        ergb.append(number)
    return ergb


def longest_collatz_sequence(n: int) -> Tuple[int, int]:
    """
    >>> longest_collatz_sequence(100)
    (97, 119)
    """
    erg = ()
    big = 0
    for i in range(1, n + 1):
        a_laenge = len(collatz_sequence(i))
        if a_laenge > big:
            big = a_laenge
            erg = i

    return erg, big


if __name__ == "__main__":
    doctest.testmod()
