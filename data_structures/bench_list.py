import random


def iteration_for(l):
    print("++--endwarmup")
    for j in l:
        j

def iteration_while(l):
    n = len(l)            
    print("++--endwarmup")
    j = 0
    while j < n:
        l[j]
        j += 1

def iteration_for_range(l):
    n = len(l)
    print("++--endwarmup")
    for j in range(n):
        l[j]

def comp(l):
    print("++--endwarmup")
    [k for k in l]


def insertion_beginning(l, slice_to_insert):
    print("++--endwarmup")
    for e in slice_to_insert:
        l.insert(0, e)


def insertion_middle(l, slice_to_insert):
    middle = len(l) // 2
    print("++--endwarmup")
    for e in slice_to_insert:
        l.insert(middle, e)

def insertion_end(l, slice_to_insert):
    n = len(l)
    print("++--endwarmup")
    for e in slice_to_insert:
        l.append(e)                        

def random_access(l, n):
    length = len(l)
    indext = [random.randint(0, length) for _ in range(n)]
    print("++--endwarmup")
    for e in indext:
        l[e]

def random_removal(l, n):
    length = len(l)
    r = [l[random.randint(0, length)] for _ in range(n)]
    print("++--endwarmup")
    for e in r:
        l.remove(e)

def clean(l):
    print("++--endwarmup")
    l.clear()


def my_pop(l, n):
    print("++--endwarmup")
    for _ in range(n):
        l.pop()


def my_extend(l, n):
    ml = l[:n].copy()
    print("++--endwarmup")
    l.extend(ml)
