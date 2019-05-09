"""
Main program
"""

import sys
import argparse
import random
import bench_list
import bench_set
import bench_dict


MAXSIZE = 10000
EXSIZE = MAXSIZE // 2

def main():
    """    """
    parser = argparse.ArgumentParser()
    # size
    parser.add_argument('--size', default=MAXSIZE, type=int)
    # data structure choice
    parser.add_argument('--data-structure', choices=['list', 'set', 'dict'],
                        help='data structure to do the test on', required=True)
    # types
    parser.add_argument('--type', choices=['integer', 'float', 'str'],
                        help='data type', required=True)
    #
    parser.add_argument('--action', choices=['iteration-for',
                                             'iteration-while',
                                             'iteration-for-range',
                                             'insertion-comp',
                                             'insertion-beginning',
                                             'insertion-middle',
                                             'insertion-end',
                                             'random-access',
                                             'random-removal',
                                             'clean',
                                             'create-beginning',
                                             'create-end',
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

    print("--++beginwarmup")
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
            bench_list.iteration_for(l)
        elif args.action == 'iteration-while':            
            bench_list.iteration_while(l)
        elif args.action == 'iteration-for-range':
            bench_list.iteration_for_range(l)
        elif args.action == 'insertion-comp':
            bench_list.comp(l)
        elif 'insertion' in args.action or 'create' in args.action:
            #
            slice_to_insert = l[:args.extra].copy()
            if args.action == 'insertion-beginning':
                bench_list.insertion_beginning(l, slice_to_insert)
            elif args.action == 'insertion-middle':                
                bench_list.insertion_middle(l, slice_to_insert)
            elif args.action == 'insertion-end':
                bench_list.insertion_end(l, slice_to_insert)
            elif args.action == 'create-beginning':
                bench_list.create_beginning(slice_to_insert)
            elif args.action == 'create-end':
                bench_list.create_end(slice_to_insert)
                ##
        elif args.action == 'random-access':
            bench_list.random_access(l, args.extra)
        elif args.action == 'random-removal':
            bench_list.random_removal(l, args.extra)
        elif args.action == 'clean':            
            bench_list.clean(l)
        elif args.action == 'pop':
            bench_list.my_pop(l, args.extra)
        elif args.action == 'extend':
            bench_list.my_extend(l, args.extra)
                    
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
                bench_dict.insertion(l)                
            # only 2 possibilities : insertion & insertion_comp
            else:
                bench_dict.comp(l)
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
            bench_dict.iteration_key(d)
        elif args.action == 'iteration-kv':
            bench_dict.iteration_kv(d)
        elif args.action == 'not-in':
            bench_dict.not_in(d, args.extra)
        elif args.action == 'random-access':
            bench_dict.random_access(d, args.extra)
        ##

    # SET
    if args.data_structure == 'set':
        if 'insertion' in args.action:
        # cases when we need a list for the action
            l = []
            if args.type == 'integer':
                from data import INTEGERS_L
                print('yep')
                l = INTEGERS_L[:args.size].copy()
            elif args.type == 'float':
                from data import FLOAT_L
                l = FLOAT_L[:args.size].copy()
            elif args.type == 'str':
                from data import STRING_L
                l = STRING_L[:args.size].copy() 
            if args.action == 'insertion':
                bench_set.insertion(l)
                # only 2 possibilities : insertion & insertion_comp
            else:
                bench_set.comp(l)
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
        s = {k for k in l}

        ## ACTION CHECKING
        if args.action == 'iteration':
            bench_set.iteration(s)
        elif args.action == 'random-in':
            bench_set.random_in(s, args.extra)
        elif args.action == 'not-in':
            bench_set.not_in(s, args.extra)
        ##

if __name__ == '__main__':
    main()
