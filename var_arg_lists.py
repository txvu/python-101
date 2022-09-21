def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def log_msg(msg_type, msg, *params):
    pass


def main():
    print(addition(5, 10, 15, 30))


if __name__ == '__main__':
    main()
