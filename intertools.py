import itertools


def test_func(x):
    return x < 40


def main():
    print('\nitertools.cycle')
    seq1 = ['Joe', 'John', 'Mike']
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    print('\nitertools.count')
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))

    print('\nitertools.accumulate')
    vals = [10, 20, 30, 40, 50, 40, 30]
    acc1 = itertools.accumulate(vals)
    acc2 = itertools.accumulate(vals, max)
    print(list(acc1))
    print(list(acc2))

    print('\nitertools.chain')
    x = itertools.chain('ABCD', '1234')
    print(list(x))

    print('\nitertools.dropwhile - itertools.takewhile')
    print(list(itertools.dropwhile(test_func, vals)))
    print(list(itertools.takewhile(test_func, vals)))


if __name__ == '__main__':
    main()
