def fizzbuzz(start, end):
    for num in range(start, end + 1):
        if (num % 3 == 0) and (num % 5 == 0):
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

if __name__ == '__main__':

    fizzbuzz(1, 100)
