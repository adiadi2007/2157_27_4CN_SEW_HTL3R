# Metadaten
__author__ = 'Adi Velagic'
__example__ = "SEW4/01/2"
__date__ = "24.09.2026"
__version__ = "1.0"
__license__ = "GNU GPLv3"
__status__ = "Released"

import doctest
def M(n):
    if n <= 100:
        n = M(M(n+11))
    else:
        n -= 10
    return n

if __name__ == "__main__":
    from time import time
    t0 = time()
    m_list = []
    for n in range(200):
        m_list.append(M(n))
    m_dict = {}
    for n in range(0, 200):
        m_dict[n] = M(n)

    print(time() - t0)
    print(M(50))
    print(M(90))
    print(M(100))
    print(M(150))
    print(M(200))
    doctest.testmod()
