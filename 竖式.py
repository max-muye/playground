from extra import *


def all_add(values: list):
    return sum(values)


def all_sub(values: list):
    return values[0] - sum(values[1:])


def one_mul(value1: int, value2: int, len_=None, print_TF=True):
    res = []
    if len_ == None:
        len_ = len(str(value1 * value2))
    if print_TF:
        print(" " * (len_ - len(str(value1))) + str(value1))
    print("*" + " " * (len_ - len(str(value2)) - 1) + str(value2))
    print("-" * (len_ + 1))
    for i, num in enumerate(reverse_list(list(str(value2)))):
        (
            res.append(
                " " * (len_ - len(str(value1 * int(num))) - i) + str(value1 * int(num))
            )
            if value1 * int(num) != 0
            else None
        )
    if len(res) > 1:
        for i in res:
            print(i)
        print("-" * (len_ + 1))
    print(" " * (len_ - len(str(value1 * value2))) + str(value1 * value2))
    return value1 * value2


def all_mul(values: list):
    res = 1
    for value in values:
        res *= value
    return res


def add(*values: int):
    max_len = max([len(str(value)) for value in values] + [len(str(sum(values))) - 1])
    for i, value in enumerate(values):
        value = " " * (max_len - len(str(value))) + str(value)
        print(" " + value) if i != len(values) - 1 else print("+" + value)
    print("-" * (max_len + 1))
    print(" " * (max_len - len(str(sum(values))) + 1) + str(sum(values)), end="\n\n")


def sub(*values: int):
    max_len = max(
        [len(str(value)) for value in values] + [len(str(all_sub(values))) - 1]
    )
    for i, value in enumerate(values):
        value = " " * (max_len - len(str(value)) - 1) + str(value)
        (
            print((" " if i != 0 else "") + value)
            if i != len(values) - 1
            else print("-" + value)
        )
    print("-" * (max_len + 1))
    print(
        " " * (max_len - len(str(all_sub(values)))) + str(all_sub(values)), end="\n\n"
    )


def mul(*values: int):
    len_ = len(str(all_mul(values)))
    n = one_mul(values[0], values[1], len_)
    for i, value in enumerate(values[2:]):
        n = one_mul(n, value, len_, False)
