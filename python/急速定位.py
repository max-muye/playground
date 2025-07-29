import random

while True:
    msg = int(input("请输入格子数"))
    list0 = list(range(1, msg + 1))
    for i in range(random.randint(0, msg)):
        list0.remove(random.choice(list0))
    print(list0)
    lt, rt = 0, len(list0) - 1
    msg = int(input("请输入书本编号"))
    res = "没有找到书本"
    while lt <= rt:
        mid = (lt + rt) // 2
        if msg == list0[mid]:
            res = "找到书本，编号是第" + str(mid + 1) + "个"
            break
        elif msg < list0[mid]:
            rt = mid - 1
        else:
            lt = mid + 1
    print(res)
