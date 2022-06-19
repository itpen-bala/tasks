def is_all_brackets_are_paired(user_str):
    left_brack_cnt = 0
    rigth_brack_cnt = 0
    for char in user_str:
        if char == '(':
            left_brack_cnt += 1
        if char == ')':
            rigth_brack_cnt += 1
    if left_brack_cnt == rigth_brack_cnt and left_brack_cnt > 0 and rigth_brack_cnt > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    while True:
        user_str = input("Enter the string: ")
        result = is_all_brackets_are_paired(user_str)
        if result == True:
            print('All brackets are paired')
        if result == False:
            print('Not all brackets are paired')

