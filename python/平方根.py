while True:
    msg = int(input("请输入:"))
    msg1 = int(input("请输入："))
    try_num = 0
    if msg == 1:
        print(1)
        continue

    for i in range(msg1):
        right = msg
        if i != 0:
            right = 9

        a = 1
        for j in range(i):
            a *= 10

        left = 0
        mid = (left + right) // 2

        while right - left != 1:
            if (mid / a + try_num) ** 2 > msg:
                right = mid
            else:
                left = mid
            mid = (left + right) // 2

        try_num += left / a

    print(try_num)
