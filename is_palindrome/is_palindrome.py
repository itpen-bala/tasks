def is_palindrome(string):
    
    right = int(len(string) / 2)
    left = right - 1
    if len(string) % 2 != 0:
        right += 1
    while left > -1:
        if string[left] != string[right]:
            return False
        left -= 1
        right += 1
    return True

if __name__ == "__main__":

    while True:
        s = input("Enter the word: ")
        print(is_palindrome(s))

