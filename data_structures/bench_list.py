import random
REPET = 100000

def iteration_for(l):
    # ok
    print("++--endwarmup")
    for _ in range(REPET):
        for j in l:
            j

def iteration_while(l):
    # ok
    n = len(l)            
    print("++--endwarmup")
    for _ in range(REPET):
        j = 0
        while j < n:
            l[j]
            j += 1

def iteration_for_range(l):
    # ok
    n = len(l)
    print("++--endwarmup")
    for _ in range(REPET):
        for j in range(n):
            l[j]

def comp(l):
    # ok
    print("++--endwarmup")
    for _ in range(REPET):
        [k for k in l]


def create_beginning(slice_to_insert):
    # ok
    print("++--endwarmup")
    for _ in range(REPET):
        l = []
        for e in slice_to_insert:
            l.insert(0, e)

def create_end(slice_to_insert):
    # ok
    print("++--endwarmup")
    for _ in range(REPET):
        l = []
        for e in slice_to_insert:
            l.append(e)
        
def insertion_beginning(l, slice_to_insert):
    # ok
    tmp = [l.copy() for _ in range(REPET)]
    print("++--endwarmup")
    for i in range(REPET):
        ml = tmp[i]
        for e in slice_to_insert:
            ml.insert(0, e)

def insertion_beginning_concat(l, slice_to_insert):
    tmp = [l.copy() for _ in range(REPET)]
    print("++--endwarmup")
    for i in range(REPET):
        ml = tmp[i]
        for e in slice_to_insert:
            ml = [e] + ml
            
def insertion_middle(l, slice_to_insert):
    # ok
    middle = len(l) // 2
    tmp = [l.copy() for _ in range(REPET)]
    print("++--endwarmup")
    for i in range(REPET):
        ml = tmp[i]
        for e in slice_to_insert:
            ml.insert(middle, e)

def insertion_end(l, slice_to_insert):
    # ok
    tmp = [l.copy() for _ in range(REPET)]
    print("++--endwarmup")
    for i in range(REPET):
        ml = tmp[i]
        for e in slice_to_insert:            
            ml.append(e)


def insertion_end_concat(l, slice_to_insert):
    # ok
    tmp = [l.copy() for _ in range(REPET)]
    print("++--endwarmup")
    for i in range(REPET):
        ml = tmp[i]
        for e in slice_to_insert:            
            ml = ml + [e]

    
def random_access(l, n):
    # ok
    length = len(l) - 1
    indext = [random.randint(0, length) for _ in range(n)]
    tmp = [l.copy() for _ in range(REPET)]
    print("++--endwarmup")
    for i in range(REPET):
        ml = tmp[i]
        for e in indext:
            ml[e]


def access_in_list(l, n):
    indext = l.copy()
    print("++--endwarmup")
    for i in range(REPET):
        for e in indext:
            if e in l:
                e

def access_in_set(l, n):
    indext = l.copy()
    print("++--endwarmup")
    for i in range(REPET):
        s = set(l)
        for e in indext:
            if e in s:
                e


def random_removal(l, n):
    # ok
    length = len(l) - 1
    r = [l[random.randint(0, length)] for _ in range(n)]
    tmp = [l.copy() for _ in range(REPET)]
    print("++--endwarmup")
    for i in range(REPET):
        ml = tmp[i]
        for e in r:
            ml.remove(e)

def clean(l):
    # ok
    tmp = [l.copy() for _ in range(REPET)]
    print("++--endwarmup")
    for i in range(REPET):
        tmp[i].clear()


def my_pop(l, n):
    # ok
    tmp = [l.copy() for _ in range(REPET)]
    print("++--endwarmup")
    for i in range(REPET):
        ml = tmp[i]
        for _ in range(n):
            ml.pop()


def my_extend(l, n):
    # ok
    ml = l[:n].copy()
    tmp = [l.copy() for _ in range(REPET)]
    print("++--endwarmup")
    for i in range(REPET):
        tmp[i].extend(ml)


def modify_comprehension(l):
    print("++--endwarmup")
    for _ in range(REPET):
        [x * 10 * 100 * 1000 for x in l]

def modify_map_lambda(l):
    tmp = [l.copy() for _ in range(REPET)]
    print("++--endwarmup")
    for i in range(REPET):
        list(map(lambda x: x * 10 * 100 * 1000, tmp[i]))

def fct(x):
    return x * 10 * 100 * 1000
        
def modify_map_fct(l):
    tmp = [l.copy() for _ in range(REPET)]
    print("++--endwarmup")
    for i in range(REPET):
        list(map(fct, tmp[i]))

def modify_loop(l):
    n = len(l)
    print("++--endwarmup")
    for _ in range(REPET):
        i = 0
        while i < n:
            l[i] = l[i] * 10 * 100 * 1000
            i += 1
