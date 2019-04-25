
"""MULTITHREADED MERGE SORT
"""

import math
import multiprocessing
import random
import sys
import time


def merge_it(list_1, list_2):
    """
    Iterative version of 2 lists merging
    (for the merge sort)
    """
    list_1len, list_2len = len(list_1), len(list_2)
    list_1index, list_2index = 0, 0
    res = []
    while list_1index < list_1len and list_2index < list_2len:
        """
           l1index                l1len
              v                     v            
        l1 = [  |  |  |  | ... |  ]
        same for l2
        
        """        
        if list_1[list_1index] <= list_2[list_2index]:
            res.append(list_1[list_1index])
            list_1index += 1
        else:
            res.append(list_2[list_2index])
            list_2index += 1
    if list_1index == list_1len:
        res.extend(list_2[list_2index:])
    else:
        res.extend(list_1[list_1index:])
    return res

def merge_rec(l1, l2):
    """
    Recursive version of merging
    return a list containing all elements de l1 and l2.
    If l1 and l2 are sorted, so is the returned list.
    """
    if l1 == []:
        return l2.copy()
    elif l2 == []:
        return l1.copy()
    else:
        if l1[0] <= l2[0]:
            return [l1[0]] + merge_rec(l1[1:], l2)
        else:
            return [l2[0]] + merge_rec(l1, l2[1:])


def merge_sort_it(mlist):
    """ merge sort iterative """
    length = len(mlist)
    if length <= 1:
        return l
    middle = length // 2
    left = merge_sort_it(mlist[:middle])
    right = merge_sort_it(l[middle:])
    return merge_it(left, right)


def merge_sort_rec(l):
    """
    merge sort recursive
    return a new list containing elements of l sorted by ascending order.
    """
    n = len(l)
    if n <= 1:
        return l.copy()
    else:
        middle = n // 2
        l1 = l[:middle]
        l2 = l[middle:]
        l1s = merge_sort_rec(l1)
        l2s = merge_sort_rec(l2)
        return merge_rec(l1s, l2s)




def merge_sort_parallel(l, nbproc):
    """
    :param: list to merge
    :type: list
    :param: number of threads
    :type: int

    Le principe est d'ajouter des blocs sur la pile
    `stack` puis chaque worker ira chercher 2 blocs pour
    effectuer une fusion (merge_it par exemple) puis empiler.
    """
    # pool of workers
    pool = multiprocessing.Pool(processes=nbproc)
    size = int(math.ceil(float(len(l)) / nbproc))
    # pile de blocs qui correspondront à une tâche (sur lequel
    # le processus va effectuer un tri fusion classique)
    stack = [l[i * size:(i + 1) * size] for i in range(nbproc)]
    stack = pool.map(merge_sort_it, stack)
    while len(stack) > 1:
        n = len(stack)
        bloc = None
        if n % 2 == 1:
            bloc = stack.pop()
            
        stack = [(stack[i], stack[i + 1]) for i in range(0, n, 2)]
        
        stack = pool.map(merge_it, stack) + ([bloc] if bloc else [])
    pool.
    return stack[0]             # le dernier bloc correspond à la liste triée
