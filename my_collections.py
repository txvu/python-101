# list = [] Mutable
# tuple = () Immutable
# set = {}
# dictionary = {}
import collections


def my_func(arg1, arg2, *, suppress_exception=False):
    pass


def main():
    print('\nnamedtuple')
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(p1, p2)
    print(p1.x, p2.y)

    p1 = p1._replace(x=100)
    print(p1)

    print('\nnormaldict')
    fruits = ['pear', 'pear', 'orange', 'banana', 'apple', 'pear', 'orange', 'banana']
    fruit_counter1 = {}

    for fruit in fruits:
        if fruit in fruit_counter1.keys():
            fruit_counter1[fruit] += 1
        else:
            fruit_counter1[fruit] = 1

    for (k, v) in fruit_counter1.items():
        print(k + ': ' + str(v))

    print('\ndefaultdict')
    fruit_counter2 = collections.defaultdict(int)  # init each value to 0
    fruit_counter2 = collections.defaultdict(lambda: 100)  # init each value to 100

    for fruit in fruits:
        fruit_counter2[fruit] += 1

    for (k, v) in fruit_counter2.items():
        print(k + ': ' + str(v))

    print('\nCounter')
    class1 = ['a', 'b', 'c', 'c', 'd']
    class2 = ['e', 'f', 'c', 'd']

    c1 = collections.Counter(class1)
    c2 = collections.Counter(class2)

    print(c1['c'])
    print(sum(c1.values()), ' students in class 1')
    c1.update(class2)
    print(sum(c1.values()), ' students in class 1')

    print(c1.most_common(3))

    c1.subtract(class2)
    print(c1.most_common(3))

    print(c1 & c2)


if __name__ == '__main__':
    main()
