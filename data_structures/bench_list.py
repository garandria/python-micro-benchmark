"""
LIST DATA STRUCTURE
"""

import random


def iteration_for(l):
    print("++--endwarmup")
    for i in l:
        i


def iteration_while(l):
    n = len(l)
    i = 0
    print("++--endwarmup")
    while i < n:
        l[i]
        i += 1


def iteration_for_range(l):
    n = len(l)
    print("++--endwarmup")
    for i in range(n):
        l[i]


def iteration_comp(l):
    print("++--endwarmup")
    [i for i in l]


# INSERTION
def insertion_beginning(l, n):
    ins = l[:n].copy()
    print("++--endwarmup")
    for e in ins:
        [e] + l


def insertion_middle(l, n):
    middle = len(l) // 2
    ins = l[:n].copy()
    print("++--endwarmup")
    for e in ins:
        l.insert(middle, e)


def insertion_end(l, n):
    ins = l[:n].copy()
    print("++--endwarmup")
    for e in ins:
        l.append(e)


# RANDOM ACCESS
def random_access(l):
    length = len(l)
    i = random.randint(0, length)
    print("++--endwarmup")
    l[i]


def random_removal(l, n):
    length = len(l)
    r = [random.randint(0, length) for _ in range(n)]
    print("++--endwarmup")
    for i in r:
        l[i]


def clean(l):
    print("++--endwarmup")
    l.clear()


def lpop(l, n):
    print("++--endwarmup")
    for _ in range(n):
        l.pop()


def lextend(l, n):
    ml = l[:n].copy()
    print("++--endwarmup")
    l.extends(ml)
