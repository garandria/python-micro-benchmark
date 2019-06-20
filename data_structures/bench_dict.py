import random

REPET = 100000

def insertion(l):
    print("++--endwarmup")
    for _ in range(REPET):
        d = dict()
        for k in l:
            d[k] = k

def comp(l):
    print("++--endwarmup")
    for _ in range(REPET):
        {k: k for k in l}

def iteration_key(d):
    print("++--endwarmup")
    for _ in range(REPET):
        for k in d:
            k

def iteration_kv(d):
    print("++--endwarmup")
    for _ in range(REPET):
        for k, v in d.items():
            (k, v)
         
         
def not_in(d, n):
    print("++--endwarmup")
    for _ in range(REPET):
        for _ in range(n):
            try:
                d[None]
            except KeyError:
                pass


def not_in_fct(d, n):
    print("++--endwarmup")
    for _ in range(REPET):
        for _ in range(n):
            if None in d:
                None

def in_fct(d, n):
    tmp = [e for e in d][:n]
    print("++--endwarmup")
    for _ in range(REPET):
        for e in tmp:
            if e in d:
                e

def in_error(d, n):
    tmp = [e for e in d][:n]
    print("++--endwarmup")
    for _ in range(REPET):
        for e in tmp:
            try:
                d[e]
            except KeyError:
                pass
    
def random_access(d, n):
    ml = [k for k in d]
    length = len(ml)
    keys = [ml[random.randint(0, length)] for _ in range(n)]
    print("++--endwarmup")
    for _ in range(REPET):
        for k in keys:
            d[k]


def random_removal(d, n):
    # ok
    l = list(d)
    length = len(l) - 1
    r = [l[random.randint(0, length)] for _ in range(n)]
    tmp = [d.copy() for _ in range(REPET)]
    print("++--endwarmup")
    for i in range(REPET):
        md = tmp[i]
        for e in r:
            del md[e]
            
