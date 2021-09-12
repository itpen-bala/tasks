def is_palindrome(string):
    
    str_len = len(string)
    for delta in range(str_len):
        if string[delta] != string[str_len - 1 - delta]:
            return False
        if delta == int(str_len / 2):
            return True

if __name__ == "__main__":

    while True:
        word = input("Enter the word: ")
        print("Word \'" + word + "\' is palindrome: " + str(is_palindrome(word)))

