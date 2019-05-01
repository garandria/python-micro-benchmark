"""
Main program
"""

import sys
import argparse


MAXSIZE = 10000
EXSIZE = MAXSIZE // 2


def main(argv):
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
    print('{}'.format(args))

    # LIST
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
            from bench_list import iteration_for
            iteration_for(l)
        elif args.action == 'iteration-while':
            from bench_list import iteration_while
            iteration_while(l)
        elif args.action == 'iteration-for-range':
            from bench_list import iteration_for_range
            iteration_for_range(l)
        elif args.action == 'iteration-comp':
            from bench_list import iteration_comp
            iteration_comp(l)
        elif args.action == 'insertion-beginning':
            from bench_list import insertion_beginning
            insertion_beginning(l, args.extra)
        elif args.action == 'insertion-middle':
            from bench_list import insertion_middle
            insertion_middle(l, args.extra)
        elif args.action == 'insertion-end':
            from bench_list import insertion_end
            insertion_end(l, args.extra)
        elif args.action == 'random-acces':
            from bench_list import random_access
            random_access(l)
        elif args.action == 'random-removal':
            from bench_list import random_removal
            random_removal(l, args.extra)
        elif args.action == 'clean':
            from bench_list import clean
            clean(l)
        elif args.action == 'pop':
            from bench_list import lpop
            lpop(l, args.extra)
        elif args.action == 'extend':
            from bench_list import lextend
            lextend(l, args.extra)
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
                from bench_dict import insertion
                insertion(l)
            # only 2 possibilities : insertion & insertion_comp
            else:
                from bench_dict import insertion_comp
                insertion_comp(l)        
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
            from bench_dict import iteration_key
            iteration_key(d)
        elif args.action == 'iteration-kv':
            from bench_dict import iteration_kv
            iteration_kv(d)
        elif args.action == 'not-in':
            from bench_dict import not_in
            not_in(d, args.extra)
        elif args.action == 'random-access':
            from bench_dict import random_access
            random_access(d, args.extra)
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
                    from bench_set import insertion
                    insertion(l)
                # only 2 possibilities : insertion & insertion_comp
                else:
                    from bench_set import insertion_comp
                    insertion_comp(l)
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
            from bench_set import iteration
            iteration(s)
        elif args.action == 'random-in':
            from bench_set import random_in
            random_in(s, args.extra)
        elif args.action == 'not-in':
            from bench_set import not_in
            not_in(s, args.extra)
        ##

if __name__ == '__main__':
    main(sys.argv)
