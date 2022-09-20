def main():
    list1 = [1, 2, 3, 0, 5, 6]
    list2 = ['hello', 'Isaac', 'a', 'World', 'abc']

    print(f'Any: {any(list1)} - {any(list2)}')  # True. Because at least one of the element is true
    print(f'All: {all(list1)} - {all(list2)}')  # False. Because 0 is false
    print(f'Min: {min(list1)} - {min(list2)}')
    print(f'Max: {max(list1)} - {max(list2)}')
    print(f'Sum: {sum(list1)}')


if __name__ == '__main__':
    main()
