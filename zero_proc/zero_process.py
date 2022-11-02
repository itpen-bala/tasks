#Реализуйте алгоритм, который принимает массив и перемещает все нули в конец, 
#сохраняя порядок остальных элементов.


def zero_process(arr: list) -> None:
    zero_list = []
    index = 0
    while index != len(arr):
        if arr[index] == 0:
            zero_list.append(arr.pop(index))
        index += 1

    for element in zero_list:
        arr.append(element)

