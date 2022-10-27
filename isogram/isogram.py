def isogram(word):
    if len(word) == len(set(word)):
         return True
    else:
         return False

if __name__ == "__main__":
    print(isogram("abc"))
    print(isogram("abcc"))

