

import sys
import argparse


def main():
    """    """
    parser = argparse.ArgumentParser()
    # size
    parser.add_argument('--size', default=MAXSIZE, type=int)
    # data structure choice
    parser.add_argument('--data-structure', choices=['list', 'narray'],
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
    
