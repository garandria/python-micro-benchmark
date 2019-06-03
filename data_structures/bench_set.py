import random


REPET = 100000

def insertion(l):    
    print("++--endwarmup")
    for _ in range(REPET):
        s = set()
        for e in l:
            s.add(e)

def comp(l):
    print("++--endwarmup")
    for _ in range(REPET):
        {e for e in l}

    
def iteration(s):
    print("++--endwarmup")
    for _ in range(REPET):
        for e in s:
            e

def random_in(s, n):
    ml = list(s)
    length = len(ml) - 1
    r = [ml[random.randint(0, length)] for _ in range(n)]
    print("++--endwarmup")
    for _ in range(REPET):
        for a in r:
            a in s


def not_in(s, n):
    print("++--endwarmup")
    for _ in range(REPET):
        for _ in range(n):
            None in s


def to_set(l):
    print("++--endwarmup")
    for _ in range(REPET):
        set(l)


def random_removal(s, n):
    l = list(s)
    length = len(l) - 1
    r = [l[random.randint(0, length)] for _ in range(n)]
    tmp = [s.copy() for _ in range(REPET)]
    print("++--endwarmup")
    for i in range(REPET):
        ms = tmp[i]
        for e in r:
            ms.remove(e)
