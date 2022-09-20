def main():
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    duties = ['work', 'work', 'work', 'work', 'work', 'play', 'play']

    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))

    for i, m in enumerate(days, start=1):
        print(i, m)

    for m in zip(days, duties):
        print(m)

    for i, m in enumerate(zip(days, duties), start=1):
        print(i, m[0], 'is for', m[1])


if __name__ == '__main__':
    main()
