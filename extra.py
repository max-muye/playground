# 一些额外的函数
def in_in(lt, target, long=None):  # 判断是否在列表中,long为列表维度 # √
    if long == None:
        long = get_list_length(lt)
    tf = False
    if long == 1:
        if target in lt:
            tf = True
    else:
        try:
            for i in lt:
                tf = tf or in_in(i, target, long - 1)
        except:
            pass
    return tf


ii = in_in


def number_system_change(num, old_base, new_base):  # 进制转换 # √
    def nsc_n_to_10(num, base):
        num = list(num)
        res = 0
        for i in range(len(num)):
            res += int(num[i]) * base ** (len(num) - i - 1)
        return res

    def nsc_10_to_n(num, base):
        res = ""
        while num > 0:
            res += str(num % base)
            num //= base
        return int(res)

    return nsc_10_to_n(nsc_n_to_10(num, old_base), new_base)


nsc = number_system_change


def center_print(text, length, print_TF=True):  # 居中打印 # √
    if length < len(text):
        return False
    else:
        res = ""
        if length % 2 == len(text) % 2:
            res = (
                " " * (length - len(text) // 2) + text + " " * (length - len(text) // 2)
            )
        else:
            length -= 1
            res = center_print(text, length, False)
        if print_TF:
            print(res)
        return res


cp = center_print


def extra_print(text, length, char="#", print_TF=True, enter_TF=False):  # 特殊打印 # √
    print_TF_ = print_TF
    if type(text) in [int, float] or text == ".":
        text = str(text)

        def make_line(char, length, where, res):
            if type(where) == list:
                for i in where:
                    make_line(char, length, i, res)
            elif where == "top":
                res[0] = [char for x in range(length // 2)]
            elif where == "top right":
                for i in range(length):
                    if i <= length // 2:
                        res[i][-1] = char
            elif where == "top left":
                for i in range(length):
                    if i <= length // 2:
                        res[i][0] = char
            elif where == "middle":
                res[length // 2] = [char for x in range(length // 2)]
                if length % 2 == 0:
                    res[length // 2 - 1] = [char for x in range(length // 2)]
            elif where == "bottom":
                res[length - 1] = [char for x in range(length // 2)]
            elif where == "bottom right":
                for i in range(length):
                    if i >= length // 2:
                        res[i][-1] = char
            elif where == "bottom left":
                for i in range(length):
                    if i >= length // 2:
                        res[i][0] = char
            else:
                return False
            return res

        res = [[" " for x in range(length // 2)] for x in range(length)]
        if text == "1":
            res = make_line(
                char,
                length,
                [
                    "top right",
                    "bottom right",
                ],
                res,
            )
            return res
        elif text == "2":
            res = make_line(
                char,
                length,
                [
                    "top",
                    "top right",
                    "middle",
                    "bottom left",
                    "bottom",
                ],
                res,
            )
            return res
        elif text == "3":
            res = make_line(
                char,
                length,
                [
                    "top",
                    "top right",
                    "middle",
                    "bottom right",
                    "bottom",
                ],
                res,
            )
            return res
        elif text == "4":
            res = make_line(
                char,
                length,
                [
                    "top left",
                    "top right",
                    "middle",
                    "bottom right",
                ],
                res,
            )
            return res
        elif text == "5":
            res = make_line(
                char,
                length,
                [
                    "top",
                    "top left",
                    "middle",
                    "bottom right",
                    "bottom",
                ],
                res,
            )
            return res
        elif text == "6":
            res = make_line(
                char,
                length,
                [
                    "top",
                    "top left",
                    "middle",
                    "bottom right",
                    "bottom left",
                    "bottom",
                ],
                res,
            )
            return res
        elif text == "7":
            res = make_line(
                char,
                length,
                ["top", "top right", "bottom right"],
                res,
            )
            return res
        elif text == "8":
            res = make_line(
                char,
                length,
                [
                    "top",
                    "top left",
                    "top right",
                    "middle",
                    "bottom right",
                    "bottom left",
                    "bottom",
                ],
                res,
            )
            return res
        elif text == "9":
            res = make_line(
                char,
                length,
                [
                    "top",
                    "top left",
                    "top right",
                    "middle",
                    "bottom right",
                    "bottom",
                ],
                res,
            )
            return res
        elif text == "0":
            res = make_line(
                char,
                length,
                [
                    "top",
                    "top left",
                    "top right",
                    "bottom left",
                    "bottom right",
                    "bottom",
                ],
                res,
            )
            return res
        elif text == ".":
            res = [[" "] for x in range(length)]
            res[-1] = [char]
            return res
        else:
            res = [[] for x in range(length)]
            for i in text:
                k = extra_print(i, length, char, False)
                if enter_TF and print_TF:
                    for j in k:
                        for l in j:
                            print(l, end=" ")
                        print()
                    print()
                    print_TF_ = False
                for j in range(length):
                    res[j] = res[j] + ["   "] + k[j]
            if print_TF_:
                for i in res:
                    for j in i:
                        print(j, end=" ")
                    print()
                print()
            return res
    else:
        res = [[" " for x in range(length)] for x in range(length)]

        def make_line(char, length, where, res):
            res_even = length % 2 == 0
            if where == "topleft":
                if res_even:
                    res[0] = [char] * (length // 2) + res[0][length // 2 :]
                else:
                    res[0] = [char] * (length // 2 + 1) + res[0][length // 2 :]
            elif where == "topright":
                if res_even:
                    res[0] = res[0][: length // 2] + [char] * (length // 2)
                else:
                    res[0] = res[0][: length // 2] + [char] * (length // 2 + 1)
            elif where == "lefttop":
                x = res[length // 2][0]
                for i in range(length):
                    if i <= length // 2:
                        res[i][0] = char
                if res_even:
                    res[length // 2][0] = x
            elif where == "top":
                x = res[length // 2][length // 2]
                y = res[length // 2][length // 2 - 1]
                for i in range(length):
                    if i <= length // 2:
                        res[i][length // 2] = char
                        if res_even:
                            res[i][length // 2 - 1] = char
                if res_even:
                    res[length // 2][length // 2] = x
                    res[length // 2][length // 2 - 1] = y
            elif where == "righttop":
                x = res[length // 2][-1]
                for i in range(length):
                    if i <= length // 2:
                        res[i][-1] = char
                if res_even:
                    res[length // 2][-1] = x
            elif where == "left":
                if res_even:
                    res[length // 2] = [char] * (length // 2) + res[length // 2][
                        length // 2 :
                    ]
                    res[length // 2 - 1] = [char] * (length // 2) + res[
                        length // 2 - 1
                    ][length // 2 :]
                else:
                    res[length // 2] = [char] * (length // 2 + 1) + res[length // 2][
                        length // 2 + 1 :
                    ]
            elif where == "right":
                if res_even:
                    res[length // 2] = res[length // 2][: length // 2] + [char] * (
                        length // 2
                    )
                    res[length // 2 - 1] = res[length // 2 - 1][: length // 2] + [
                        char
                    ] * (length // 2)
                else:
                    res[length // 2] = res[length // 2][: length // 2] + [char] * (
                        length // 2 + 1
                    )
            elif where == "leftbottom":
                x = res[length // 2][0]
                for i in range(length):
                    if i >= length // 2:
                        res[i][0] = char
                if res_even:
                    res[length // 2][0] = x
            elif where == "bottom":
                x = res[length // 2][length // 2]
                y = res[length // 2][length // 2 - 1]
                for i in range(length):
                    if i >= length // 2:
                        res[i][length // 2] = char
                        if res_even:
                            res[i][length // 2 - 1] = char
                if res_even:
                    res[length // 2][length // 2] = x
                    res[length // 2][length // 2 - 1] = y
            elif where == "rightbottom":
                x = res[length // 2][-1]
                for i in range(length):
                    if i >= length // 2:
                        res[i][-1] = char
                if res_even:
                    res[length // 2][-1] = x
            elif where == "bottomleft":
                if res_even:
                    res[-1] = [char] * (length // 2) + res[-1][length // 2 :]
                else:
                    res[-1] = [char] * (length // 2 + 1) + res[-1][length // 2 + 1 :]

            elif where == "bottomright":
                if res_even:
                    res[-1] = res[-1][: length // 2] + [char] * (length // 2)
                else:
                    res[-1] = res[-1][: length // 2] + [char] * (length // 2 + 1)
            else:
                for i in where:
                    res = make_line(char, length, i, res)
            return res

        # 一些图形
        if text == "日":
            res = make_line(
                char,
                length,
                [
                    "topleft",
                    "topright",
                    "bottomleft",
                    "bottomright",
                    "righttop",
                    "rightbottom",
                    "lefttop",
                    "leftbottom",
                    "left",
                    "right",
                ],
                res,
            )
            return res
        elif text == "H":
            res = make_line(
                char,
                length,
                [
                    "righttop",
                    "rightbottom",
                    "lefttop",
                    "leftbottom",
                    "left",
                    "right",
                ],
                res,
            )
            return res
        elif text == "十":
            res = make_line(
                char,
                length,
                [
                    "top",
                    "bottom",
                    "left",
                    "right",
                ],
                res,
            )
            return res
        elif text == "工":
            res = make_line(
                char,
                length,
                ["topleft", "topright", "bottomleft", "bottomright", "top", "bottom"],
                res,
            )
            return res
        elif text == "三":
            res = make_line(
                char,
                length,
                [
                    "topleft",
                    "topright",
                    "bottomleft",
                    "bottomright",
                    "left",
                    "right",
                ],
                res,
            )
            return res
        elif text == "王":
            res = make_line(
                char,
                length,
                [
                    "topleft",
                    "topright",
                    "bottomleft",
                    "bottomright",
                    "left",
                    "right",
                    "top",
                    "bottom",
                ],
                res,
            )
            return res
        elif text == "口":
            res = make_line(
                char,
                length,
                [
                    "topleft",
                    "topright",
                    "bottomleft",
                    "bottomright",
                    "righttop",
                    "rightbottom",
                    "lefttop",
                    "leftbottom",
                ],
                res,
            )
            return res
        elif text == "田":
            res = make_line(
                char,
                length,
                [
                    "topleft",
                    "topright",
                    "lefttop",
                    "leftbottom",
                    "righttop",
                    "rightbottom",
                    "bottomleft",
                    "bottomright",
                    "left",
                    "right",
                    "top",
                    "bottom",
                ],
                res,
            )
            return res
        elif text == "日":
            res = make_line(
                char,
                length,
                [
                    "topleft",
                    "topright",
                    "lefttop",
                    "leftbottom",
                    "righttop",
                    "rightbottom",
                    "bottomleft",
                    "bottomright",
                    "left",
                    "right",
                ],
                res,
            )
            return res
        elif text == " ":
            return res
        else:
            res = [[] for x in range(length)]
            for i in text:
                if i in "1234567890":
                    i = int(i)
                k = extra_print(i, length, char, False)
                if enter_TF and print_TF:
                    for j in k:
                        for l in j:
                            print(l, end=" ")
                        print()
                    print()
                    print_TF_ = False
                for j in range(length):
                    res[j] = res[j] + ["   "] + k[j]
        if print_TF_:
            for i in res:
                for j in i:
                    print(j, end=" ")
                print()
            print()
        return res


ep = extra_print


def in_to_one_list(lt, long=None):  # 将多维列表转换为一维列表 # √
    if long == None:
        long = get_list_length(lt)
    res = []
    if long == 2:
        for i in lt:
            for j in i:
                res.append(j)
    elif long == 1:
        res = lt
    else:
        try:
            for i in lt:
                res += in_to_one_list(i, long - 1)
        except:
            pass
    return res


itol = in_to_one_list


def reverse_list(lt):  # 反转列表 # √
    res = []
    for i in lt:
        res.insert(0, i)
    return res


rl = reverse_list


def get_list_length(lt):  # 获取列表最大维度 # √
    res = []
    for i in lt:
        if type(i) == list:
            res.append(get_list_length(i) + 1)
        else:
            res.append(1)
    return max(res)


gll = get_list_length


def find_item(lt, target, long=None, now=[], res=[]):  # 查找列表中指定元素的索引 # √
    if long == None:
        long = get_list_length(lt)
    if long == 1:
        for i in range(len(lt)):
            if lt[i] == target:
                res.append(now + [i])
    else:
        for i in range(len(lt)):
            find_item(lt[i], target, long - 1, now + [i], res)
            if now:
                now.pop()
    return res


fi = find_item


def from_float_to_int(value: float):  # 将浮点数转换为整数,去掉小数点 # √
    return int("".join((str(x)) if x != "." else "" for x in list(str(value))))


ffti = from_float_to_int


def flip_list(lt):  # 将二维列表翻转 # √
    x = len(lt)
    y = len(lt[0])
    lt = itol(lt)
    res = []
    for i in range(y):
        res.append(lt[i * x : (i + 1) * x])
    return res


fl = flip_list
