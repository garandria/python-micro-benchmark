"""
I tried to isolate every function for
each data structure to make less operation
possible. It is not a quesiton of code
duplication or whatever.
"""
from array import *
from numpy import array as narray

#########
# LISTS #
#########


def list_for_loop_without_range(l):
    """
    Iterate in the list using
    a for loop without the range
    :parameter: a list
    :type: list
    :
    :rtype: float
    """
    print("++--endwarmup")
    for i in l:
        i

       
def list_for_loop_with_range(l, size):
    """
    Iterate in the list using
    a for loop with the range
    :parameter: a list
    :type: list
    :parameter: sizeof the list
    :type: int
    :
    :rtype: float
    """
    print("++--endwarmup")
    for i in range(0, size):
        l[i]


def list_comprehension(l):
    """
    Iterate in the list
    :parameter:
    :type:
    :
    :rtype: float
    """
    print("++--endwarmup")
    [i for i in l]


def list_while_loop(l, size):
    """
    iterate in the list using
    a while loop
    :parameter: a list
    :type: list
    :parameter: sizeof the list
    :type: int
    :
    :rtype: NoneType
    """
    print("++--endwarmup")
    i = 0
    while i < size:
        l[i]
        i += 1


########
# SETS #
########


def set_for_loop_without_range(l):
    """
    Iterate in the set using 
    a for loop without the range
    :parameter: a set
    :type: set
    :
    :rtype: float
    """
    print("++--endwarmup")
    for i in l:
        i    

def set_comprehension(l):
    """
    Iterate in the set
    :parameter:
    :type:
    :
    :rtype: float
    """
    print("++--endwarmup")
    {i for i in l}

#########
# TUPLE #
#########
    

def tuple_for_loop_without_range(l):
    """
    Iterate in the tuple using 
    a for loop without the range
    :parameter: a tuple
    :type: tuple
    :
    :rtype: float
    """
    print("++--endwarmup")
    for i in l:
        i 

def tuple_for_loop_with_range(l, size):
    """
    Iterate in the tuple using 
    a for loop with the range
    :parameter: a tuple
    :type: tuple
    :parameter: sizeof the tuple
    :type: int
    :
    :rtype: float
    """
    print("++--endwarmup")
    for i in range (0, size):
        l[i]    

def tuple_comprehension(l):
    """
    Iterate in the tuple
    :parameter:
    :type:
    :
    :rtype: float
    """
    print("++--endwarmup")
    (i for i in l)
    
def tuple_while_loop(l, size):
    """
    iterate in the tuple using
    a while loop
    :parameter: a tuple
    :type: tuple
    :parameter: sizeof the tuple
    :type: int
    :
    :rtype: NoneType   
    """
    print("++--endwarmup")
    i = 0
    while i < size:
        l[i]
        i += 1


########
# DICT #
########
    

def dict_for_loop_without_range(l):
    """
    Iterate in the dict using 
    a for loop without the range
    :parameter: a dict
    :type: dict
    :
    :rtype: float
    """
    print("++--endwarmup")
    for i in l:
        i    

def dict_comprehension(l):
    """
    Iterate in the dict
    :parameter:
    :type:
    :
    :rtype: float
    """
    print("++--endwarmup")
    {i: i for i in l}


#########
# ARRAY #
#########

    
def array_for_loop_without_range(l):
    """
    Iterate in the array using 
    a for loop without the range
    :parameter: a array
    :type: array
    :
    :rtype: float
    """
    print("++--endwarmup")
    for i in l:
        i    

def array_for_loop_with_range(l, size):
    """
    Iterate in the array using 
    a for loop with the range
    :parameter: a array
    :type: array
    :parameter: sizeof the array
    :type: int
    :
    :rtype: float
    """
    print("++--endwarmup")
    for i in range (0, size):
        l[i]    

def array_comprehension(l):
    """
    Iterate in the array
    :parameter:
    :type:
    :
    :rtype: float
    """
    print("++--endwarmup")
    array(l.typecode, [i for i in l])
    
def array_while_loop(l, size):
    """
    iterate in the array using
    a while loop
    :parameter: a array
    :type: array
    :parameter: sizeof the array
    :type: int
    :
    :rtype: NoneType
    """
    print("++--endwarmup")
    i = 0
    while i < size:
        l[i]
        i += 1


##############
# NUMPY ARRA #
##############

def narray_for_loop_without_range(l):
    """
    Iterate in the narray using
    a for loop without the range
    :parameter: a narray
    :type: narray
    :
    :rtype: float
    """
    print("++--endwarmup")
    for i in l:
        i

       
def narray_for_loop_with_range(l, size):
    """
    Iterate in the narray using
    a for loop with the range
    :parameter: a narray
    :type: narray
    :parameter: sizeof the narray
    :type: int
    :
    :rtype: float
    """
    print("++--endwarmup")
    for i in range(0, size):
        l[i]


def narray_comprehension(l):
    """
    Iterate in the narray
    :parameter:
    :type:
    :
    :rtype: float
    """
    print("++--endwarmup")
    narray([i for i in l])


def narray_while_loop(l, size):
    """
    iterate in the narray using
    a while loop
    :parameter: a narray
    :type: narray
    :parameter: sizeof the narray
    :type: int
    :
    :rtype: NoneType
    """
    print("++--endwarmup")
    i = 0
    while i < size:
        l[i]
        i += 1

