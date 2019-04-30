"""
SET
"""

import random


def insertion(l):
    mset = set()
    print("++--endwarmup")
    for e in l:
        mset.add(e)


def insertion_comp(l):
    print("++--endwarmup")
    {e for e in l}


def iteration(s):
    print("++--endwarmup")
    for e in s:
        e


def random_in(s, n):
    ml = list(s)
    length = len(ml)
    r = [ml[random.randint(0, length)] for _ in range(n)]
    print("++--endwarmup")
    for a in r:
        a in s


def not_in(s, n):
    print("++--endwarmup")
    for _ in range(n):
        None in s

