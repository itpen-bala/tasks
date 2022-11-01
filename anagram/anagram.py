# group_ann(['dog', 'cat', 'god', 'late', 'tale']) == [['dog', 'god'], ['cat'], ['late', 'tale']]

def group_ann(words: list) -> list:
    words_dict = {}
    result_list = []

    for word in words:
        word_list = list(word)
        word_list.sort()
        key_word = ''.join(word_list)
        if key_word not in words_dict:
            words_dict[key_word] = [word]
        else:
            words_dict[key_word].append(word)

    for el in words_dict:
        result_list.append(words_dict[el])

    return result_list


if __name__ == "__main__":
    print(group_ann(['dog', 'cat', 'god', 'late', 'tale']))

