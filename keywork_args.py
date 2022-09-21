def my_func(arg1, arg2, *, suppress_exception=False):
    pass


def main():
    my_func('Hello', 'World', suppress_exception=True)


if __name__ == '__main__':
    main()
