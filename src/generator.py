from random import randrange, randint, random

MIN = -20
MAX = 20
MAXLENGTH = 10
UNICODEMAX = (2 << 11) - 1


def randomint():
    """
    """
    return randint(MIN, MAX)


def randomfloat():
    """
    """
    return random()


def randomstr():
    """
    """
    res = ""
    for i in range(randrange(MAXLENGTH)):
        c = chr(randrange(UNICODEMAX))
        while not (ord(c) < 128):
            c = chr(randrange(UNICODEMAX))
        res += c
    return res

def randomobj():
    """
    """
    return object
