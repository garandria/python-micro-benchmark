
import sys
from dsloops import *
from generator import *
from array import *

MAXSIZE = 10000000

# object, int, float, str


def cmph(dtype, fct, size=MAXSIZE):
    if dtype == dict:
        return {i: fct for i in range(size)}
    elif dtype == array:
        t = type(fct)
        mt = ''
        if 'int' in str(type(t)):
            mt = 'b'
        elif 'str' in str(type(t)):
            mt = 'u'
            fct = 'a'
        elif 'float' in str(type(t)):
            mt = 'f'
        else:
            return None
        return array(mt, [fct for i in range(size)])
    else:
        # if we consider that the random objects do not
        # appear more than once (because there will be
        # only 1 element in the set in that case)        
        return dtype(fct for i in range(size))


def usage():
    print("Usage")
    print("python3 main.py -<opt>")
    print("Types:")
    print("\t-o for object")
    print("\t-i for integer")
    print("\t-f for float")
    print("\t-s for string")
    print("\tThe only types possible for an array are :")
    print("\tintegers, float and string")
    print("\t(this last will be converted to python unicode character)")
    print("Data Structures:")
    print("\t-L for list")
    print("\t-S for set")
    print("\t-D for dict")
    print("\t-A for array")
    print("Loop type:")
    print("\t-l for the for loop with range")
    print("\t-r for the for loop without range")
    print("\t-c for comprehension")
    print("\t-w for while loop")


def opt_type_checker(opt, t, size):
    if 'o' in opt:
        print("--++beginwarmup")
        xs = cmph(t, randomobj(), size)
        print("++--endwarmup")
        return xs
    elif 'i' in opt:
        print("--++beginwarmup")
        xs = cmph(t, randomint(), size)
        print("++--endwarmup")
        return xs
    elif 'f' in opt:
        print("--++beginwarmup")
        xs = cmph(t, randomfloat(), size)
        print("++--endwarmup")
        return xs
    elif 's' in opt:
        print("--++beginwarmup")
        xs = cmph(t, randomstr(), size)
        print("++--endwarmup")
        return xs
    else:
        print("Unprecised type")
        exit(0)


def main():
    if len(sys.argv) >= 2:
        opt = sys.argv[1]
        size = MAXSIZE
        if len(sys.argv) == 3:
            size = abs(int(sys.argv[-1]))
        if 'h' in opt:
            usage()
            exit(0)
        if 'L' in opt:
            xs = opt_type_checker(opt, list, size)
            if 'r' in opt:
                list_for_loop_with_range(xs, size)
            elif 'l' in opt:
                list_for_loop_without_range(xs)
            elif 'c' in opt:
                list_comprehension(xs)
            elif 'w' in opt:
                list_while_loop(xs, size)
            else:
                print("Loop not specified")
                exit(0)
        elif 'S' in opt:
            xs = opt_type_checker(opt, set, size)
            if 'l' in opt:
                set_for_loop_without_range(xs)
            elif 'c' in opt:
                set_comprehension(xs)
            else:
                print("Loop not specified")
                exit(0)
        elif 'T' in opt:
            xs = opt_type_checker(opt, tuple, size)
            if 'r' in opt:
                tuple_for_loop_with_range(xs, size)
            elif 'l' in opt:
                tuple_for_loop_without_range(xs)
            elif 'c' in opt:
                tuple_comprehension(xs)
            elif 'w' in opt:
                tuple_while_loop(xs, size)
            else:
                print("Loop not specified")
                exit(0)
        elif 'D' in opt:
            xs = opt_type_checker(opt, dict, size)
            if 'f' in opt:
                dict_for_loop_without_range(xs)
            elif 'c' in opt:
                dict_comprehension(xs)
            else:
                print("Loop not specified")
                exit(0)
        elif 'A' in opt:
            xs = opt_type_checker(opt, array, size)
            if xs == None:
                print("Invalid type for array")
                exit(0)
            if 'r' in opt:
                list_for_loop_with_range(xs, size)
            elif 'l' in opt:
                list_for_loop_without_range(xs)
            elif 'c' in opt:
                list_comprehension(xs)
            elif 'w' in opt:
                list_while_loop(xs, size)
            else:
                print("Loop not specified")
                exit(0)
    else:
        usage()
    

if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print("Invalid size {}".format(sys.argv[-1]))
        exit(0)
