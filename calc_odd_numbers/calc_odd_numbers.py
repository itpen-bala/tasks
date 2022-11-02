#      1
#     3 5
#    7 9 11
#  13 15 17 19
# 21 23 25 27 29
# ...

# Print pyramid of odd numbers (start with 1) and calculate numbers row of specified row 

def get_odd_nums_sum(target_row: int) -> None:
    row_nums = []
    row_border = 1
    num = 1
    
    while True:
        if not num % 2 == 0:
            print(f"{num} ", end='')
            row_nums.append(num)
            if len(row_nums) == row_border:
                print('\n', end='')
                if row_border == target_row:
                    break
                row_border += 1
                row_nums.clear()
        num += 1

    print(f"Result: {sum(row_nums)}")
