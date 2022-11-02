#Реализуйте алгоритм, который принимает массив и перемещает все нули в конец, 
#сохраняя порядок остальных элементов.


def zero_process(arr: list) -> None:
    zero_list = []
    index = 0
    len_arr = len(arr)
    while index < len_arr:
        if arr[index] == 0:
            arr.append(arr.pop(index))
        index += 1

