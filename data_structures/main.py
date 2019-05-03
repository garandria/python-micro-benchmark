"""
Main program
"""

import sys
import argparse
import random

MAXSIZE = 10000
EXSIZE = MAXSIZE // 2
REPET = 1000

def main():
    """    """
    parser = argparse.ArgumentParser()
    # size
    parser.add_argument('--size', default=MAXSIZE, type=int)
    # data structure choice
    parser.add_argument('--data-structure', choices=['list', 'set', 'dict'],
                        help='data strcture to do the test on', required=True)
    # types
    parser.add_argument('--type', choices=['integer', 'float', 'str'],
                        help='data type', required=True)
    #
    parser.add_argument('--action', choices=['iteration-for',
                                             'iteration-while',
                                             'iteration-for-range',
                                             'iteration-comp',
                                             'insertion-beginning',
                                             'insertion-middle',
                                             'insertion-end',
                                             'random-access',
                                             'random-removal',
                                             'clean',
                                             'pop',
                                             'extend',
                                             'insertion',
                                             'insertion-comp',
                                             'iteration-key',
                                             'iteration-kv',
                                             'not-in',
                                             'iteration',
                                             'random-in'],
                        help='action to perform on the data structure',
                        required=True)

    # Number of elements to add when adding/deleting from a data structure
    parser.add_argument('--extra', default=EXSIZE, type=int,
                        help='number of extra element to add in the data structure')
    
    args = parser.parse_args()
    
    # LIST
    print("--++beginwarmup")
    if args.data_structure == 'list':
        l = []
        ## TYPE CHECKING
        if args.type == 'integer':
            from data import INTEGERS_L
            l = INTEGERS_L[:args.size].copy()
        elif args.type == 'float':
            from data import FLOAT_L
            l = FLOAT_L[:args.size].copy()
        # else because you have only these choices
        elif args.type == 'str':
            from data import STRING_L
            l = STRING_L[:args.size].copy()
        ## ACTION CHECKING
        if args.action == 'iteration-for':
            print("++--endwarmup")
            for i in range(REPET):
                for j in l:
                    j
                    
        elif args.action == 'iteration-while':
            n = len(l)            
            print("++--endwarmup")
            for i in range(REPET):
                j = 0
                while j < n:
                    l[j]
                    j += 1
                    
        elif args.action == 'iteration-for-range':
            n = len(l)
            print("++--endwarmup")
            for i in range(REPET):
                for j in range(n):
                    l[j]
        elif args.action == 'iteration-comp':
            print("++--endwarmup")
            for i in range(REPET):
                [k for k in l]
        elif 'insertion' in args.action:
            # 
            slice_to_insert = l[:args.extra].copy()
            ins = {i: slice_to_insert.copy() for i in range(REPET)}
            # 
            tmp = {i: l.copy() for i in range(REPET)}
            # 
            if args.action == 'insertion-beginning':
                print("++--endwarmup")
                for i in range(REPET):
                    tmp2 = tmp[i]
                    for e in ins[i]:
                        tmp2.insert(0, e)
            elif args.action == 'insertion-middle':
                middle = len(l) // 2
                print("++--endwarmup")
                for i in range(REPET):
                    instmp = ins[i]
                    tmp2 = tmp[i]
                    for e in instmp:
                        tmp2.insert(middle, e)
            elif args.action == 'insertion-end':
                n = length(l)
                print("++--endwarmup")
                for i in range(REPET):
                    instmp = ins[i]
                    tmp2 = tmp[i]                    
                    for e in instmp:
                        tmp2.append(e)
                        
                ## 
        elif args.action == 'random-acces':
            length = len(l)
            indext = [random.randint(0, length) for _ in range(args.extra)]
            print("++--endwarmup")
            for i in range(REPET):
                for e in indext:
                    l[e]
        elif args.action == 'random-removal':
            length = len(l)
            r = [l[random.randint(0, length)] for _ in range(args.extra)]
            print("++--endwarmup")
            for i in range(REPET):
                for e in r:
                    l.remove(e)
        elif args.action == 'clean':            
            tmp = {i: l.copy() for i in range(REPET)}
            print("++--endwarmup")
            for i in range(REPET):
                tmp[i].clear()
        elif args.action == 'pop':
            tmp = {i: l.copy() for i in range(REPET)]
            print("++--endwarmup")
            for i in range(REPET):
                tmp2 = tmp[i]
                for k in range(args.extra):
                    tmp2.pop()
        elif args.action == 'extend':
            tmp = {i: l.copy() for i in range(REPET)}
            ml = l[:args.extra].copy()
            print("++--endwarmup")
            for i in range(REPET):
                tmp[i].extend(ml)
                    
        ##
    # DICTIONARY
    if args.data_structure == 'dict':
        #
        if 'insertion' in args.action:
            # cases when we need a list for the action
            l = []
            if args.type == 'integer':           
                from data import INTEGERS_L
                l = INTEGERS_L[:args.size].copy()
            elif args.type == 'float':
                from data import FLOAT_L
                l = FLOAT_L[:args.size].copy()
            elif args.type == 'str':
                from data import STRING_L
                l = STRING_L[:args.size].copy()
            if args.action == 'insertion':
                mdict = {dict() for _ in range(REPET)}
                print("++--endwarmup")
                for i in range(REPET):
                    mdict2 = mdict[i]
                    for k in l:
                        mdict2[k] = k
            # only 2 possibilities : insertion & insertion_comp
            else:
                print("++--endwarmup")
                for i in range(REPET):
                    {k: k for k in l}
        ## TYPE CHECKING
        tmp = dict()
        if args.type == 'integer':
            from data import INTEGERS_D
            tmp = INTEGERS_D
        elif args.type == 'float':
            from data import FLOAT_D
            tmp = FLOAT_D
        # else because you have only these choices
        elif args.type == 'str':
            from data import STRING_D
            tmp = STRING_D
        # take a slice form the dictionary
        l = [k for k in tmp]
        l = l[:args.size]
        d = {k: tmp[k] for k in l}

        ## ACTION CHECKING
        if args.action == 'iteration-key':
            print("++--endwarmup")                    
            for i in range(REPET):
                for k in d:
                    k
        elif args.action == 'iteration-kv':
            print("++--endwarmup")
            for i in range(REPET):
                for k, v in d:
                    (k, v)
        elif args.action == 'not-in':
            print("++--endwarmup")
            for _ in range(REPET):
                for _ in range(args.extra):
                    try:
                        d[None]
                    except KeyError:
                        pass
        elif args.action == 'random-access':
            ml = [k for k in d]
            length = len(ml)
            keys = [ml[random.randint(0, length)] for _ in range(args.extra)]
            print("++--endwarmup")
            for _ in range(REPET):
                for k in keys:
                    d[k]
        ##

    # SET
    if args.data_structure == 'set':
        if 'insertion' in args.action:
        # cases when we need a list for the action
            l = []
            if args.type == 'integer':
                from data import INTEGERS_L
                l = INTEGERS_L[:args.size].copy()
            elif args.type == 'float':
                from data import FLOAT_L
                l = FLOAT_L[:args.size].copy()
            elif args.type == 'str':
                from data import STRING_L
                l = STRING_L[:args.size].copy() 
                if args.action == 'insertion':
                    tmp = {i: set() for i in range(REPET)}
                    print("++--endwarmup")
                    for i in range(REPET):
                        tmp2 = tmp[i]
                        for e in l:
                            tpm2.add(e)
                # only 2 possibilities : insertion & insertion_comp
                else:
                    print("++--endwarmup")
                    for _ in range(REPET):
                        {e for e in l}
        ## TYPE CHECKING
        tmp = set()
        if args.type == 'integer':
            from data import INTEGERS_S
            tmp = INTEGERS_S
        elif args.type == 'float':
            from data import FLOAT_S
            tmp = FLOAT_S
        # else because you have only these choices
        elif args.type == 'str':
            from data import STRING_S
            tmp = STRING_S
        # take a slice form the dictionary
        l = [k for k in tmp]
        l = l[:args.size]
        s = {k: tmp[k] for k in l}

        ## ACTION CHECKING
        if args.action == 'iteration':
            print("++--endwarmup")
            for _ in range(REPET):
                for e in s:
                    e
        elif args.action == 'random-in':
            ml = list(s)
            length = len(ml)
            r = [ml[random.randint(0, length)] for _ in range(args.extra)]
            print("++--endwarmup")
            for _ in range(REPET):
                for a in r:
                    a in s
        elif args.action == 'not-in':
            for _ in range(REPET):
                for _ in range(args.extra):
                    None in s
        ##

if __name__ == '__main__':
    main()
