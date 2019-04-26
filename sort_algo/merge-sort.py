"""
Different implementation of the merge sort
"""

import multiprocessing
import math

def merge_it(l1, l2):
    """
    Iterative version

    >>> l1 = [0,2,5,6]
    >>> l2 = [1,3,4]
    >>> merge_it(l1, l2)
    [0, 1, 2, 3, 4, 5, 6]
    >>> merge_it([1, 3, 4, 9], [1, 2, 5])
    [1, 1, 2, 3, 4, 5, 9]
    """
    n1 = len(l1)
    n2 = len(l2)
    res = [None for i in range(n1 + n2)]
    i ,j, k = 0, 0, 0
    while i < n1 and j < n2:
        if l1[i] < l2[j]:
            res[k] = l1[i]
            i = i + 1
        else:
            res[k] = l2[j]
            j = j + 1
        k = k + 1
    while i < n1:
        res[k] = l1[i]
        i = i + 1
        k = k + 1
    while j < n2:
        res[k] = l2[j]
        j = j + 1
        k = k + 1
    return res


def merge_rec(l1, l2):
    """
    Recursive version

    >>> l1 = [0,2,5,6]
    >>> l2 = [1,3,4]
    >>> merge_rec(l1, l2)
    [0, 1, 2, 3, 4, 5, 6]
    >>> merge_rec([1, 3, 4, 9], [1, 2, 5])
    [1, 1, 2, 3, 4, 5, 9]
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


def merge_sort(l, rec = False):
    """
    A sorting function implementing the merge sort algorithm

    >>> merge_sort([3, 1, 4, 1, 5, 9, 2])
    [1, 1, 2, 3, 4, 5, 9]
    >>> import random
    >>> n = random.randrange(20)
    >>> l = [random.randrange(20) for k in range(n)]
    >>> l1 = merge_sort(l)
    >>> len(l1) == len(l)
    True
    >>> all(l1[i] <= l1[i+1] for i in range(len(l1)-1))
    True
    >>> all(k in l for k in l1)
    True
    """
    if rec:
        merge = merge_rec
    else:
        merge = merge_it
    n = len(l)
    if n <= 1:
        return l.copy()
    else:
        l1 = merge_sort((l[0: ((n-1) // 2 + 1)]))
        l2 = merge_sort((l[((n-1) // 2 + 1): n]))
        return merge(l1, l2)


def merge_p(*args):
    # *args renvoie un tuple
    l1, l2 = args[0] if len(args) == 1 else args
    l1_length, l2_length = len(l1), len(l2)
    i, j = 0, 0
    merged = []
    while i < l1_length and j < l2_length:
        if l1[i] <= l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
    if i == l1_length:
        merged.extend(l2[j:])
    else:
        merged.extend(l1[i:])
    return merged


def merge_sort_parallel(l, n):
    """
    """
    processes = n
    pool = multiprocessing.Pool(processes=processes)
    size = int(math.ceil(float(len(l)) / processes))
    # pile de blocs à fusionner
    # sachant que pour une liste l, l[:len(l) + k ] est possible
    # pour tout k positif, donc on n'oublie aucune valeur
    stack = [l[i * size: (i + 1) * size] for i in range(processes)]
    stack = pool.map(merge_sort, l)
    
    data = pool.map(merge_sort, data)
    while len(data) > 1:
        extra = data.pop() if len(data) % 2 == 1 else None
        data = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
        data = pool.map(merge_p, data) + ([extra] if extra else [])
    return data[0]

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
