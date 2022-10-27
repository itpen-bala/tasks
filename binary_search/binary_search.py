def binary_search(sort_arr: tuple, target_val: int):
    start = 0
    end = len(sort_arr) - 1
    while start <= end:
        middle = start + (end - start) // 2
        if sort_arr[middle] < target_val:
            start = middle + 1
        elif sort_arr[middle] > target_val:
            end = middle - 1
        else:
           return middle
    return None 


if __name__ == "__main__":
    user_input = input("Enter sorted list of int numbers: ")
    sort_arr = tuple(map(int, user_input.split(", ")))
    user_input = input("Enter target value: ")
    target_val = int(user_input)

    index = binary_search(sort_arr, target_val)
    if index is None:
        print(f"Value {target_val} not found")
    else:
        print(f"Found value {target_val}. Index: {index}")

