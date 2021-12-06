def swap(a, b):
    a = a + b
    b = a - b
    a = a - b

    return a, b


if __name__ == "__main__":

    a, b = swap(3, 2)
    print('a = ', a)
    print('b = ', b)

