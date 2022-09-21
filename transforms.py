def filter_func(x):
    if x % 2 == 0:
        return False
    return True


def filter_func2(x):
    if x.isupper():
        return False
    return True


def square_func(x):
    return x ** 2


def to_grade(x):
    if x >= 90:
        return 'A'
    elif 80 <= x < 90:
        return 'B'
    elif 70 <= x < 80:
        return 'C'
    elif 65 <= x < 70:
        return 'D'
    else:
        return 'F'


def main():
    nums = (1, 8, 4, 5, 13, 26, 323, 100, 435, 45, 23)
    chars = 'trhrteDFHWEFwgFgfd'
    grades = (23, 75, 43, 87, 94, 24, 76, 99, 34)

    odds = list(filter(filter_func, nums))
    print(odds)

    lowers = list(filter(filter_func2, chars))
    print(lowers)

    squares = list(map(square_func, nums))
    print(squares)

    grades = sorted(grades)
    letters = list(map(to_grade, grades))
    print(letters)


if __name__ == '__main__':
    main()
