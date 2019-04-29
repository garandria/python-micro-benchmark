"""
DICTIONNARY
"""

import random

# INSERTION


def insertion(l):
    mdict = dict()
    print("++--endwarmup")
    for i in l:
        mdict[i] = i


def insertion_comp(l):
    print("++--endwarmup")
    {i: i for i in l}


def key_iteration(d):
    print("++--endwarmup")
    for i in d:
        i


def kv_iteration(d):
    print("++--endwarmup")
    for k, v in d:
        (k, v)


def not_in(d, n):
    print("++--endwarmup")
    for i in range(n):
        try:
            d[None]
        except KeyError:
            pass


def random_access(d, n):
    ml = [k for k in d]
    length = len(ml)
    keys = [ml[random.randint(0, length)] for _ in range(n)]
    print("++--endwarmup")
    for k in keys:
        d[k]
