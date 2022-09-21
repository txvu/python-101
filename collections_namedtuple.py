# list = [] Mutable
# tuple = () Immutable
# set = {}
# dictionary = {}

import collections


def my_func(arg1, arg2, *, suppress_exception=False):
    pass


def main():
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(p1, p2)
    print(p1.x, p2.y)

    p1 = p1._replace(x=100)
    print(p1)


if __name__ == '__main__':
    main()
