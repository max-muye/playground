def combination(start, end, remaining_digits, result):
    if remaining_digits == 0:
        for num in result:
            if num != 0:
                print(num, end=" ")
        print()
    else:
        for current_num in range(start, end + 1):
            if current_num > result[remaining_digits]:
                result[remaining_digits - 1] = current_num
                combination(start, end, remaining_digits - 1, result)


while True:
    num_digits = int(input("位数："))
    combination(int(input("开始：")), int(input("结束：")), num_digits, [0] * (num_digits + 1))
