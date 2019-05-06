

def insertion(l):
    d = dict()
    print("++--endwarmup")
    for k in l:
        dict[k] = k

def comp(l):
    print("++--endwarmup")
    {k: k for k in l}

def iteration_key(d):
    print("++--endwarmup")
    for k in d:
        k

def iteration_kv(d):
    print("++--endwarmup")
    for k, v in d:
        (k, v)

def not_in(d):
    print("++--endwarmup")
    for _ in range(args.extra):
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
