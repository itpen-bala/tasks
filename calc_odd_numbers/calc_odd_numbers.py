     1
    3 5
   7 9 11
 13 15 17 19
21 23 25 27 29
...

#Посчитайте сумму н-го ряда пирамиды нечетных чисел (начало с 1)

def get_sum(row: int, max_num: int) -> int:
    count = 1
    row_size = 1
    
    for _ in range(max_num):
        if not count % 2 == 0:
            print(count)
        
    
    return 0
