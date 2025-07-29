# a=被除数 b=除数 c=小数点后几位
def perfect_division(a, b, c):
    # 获取小数点后的位数
    def point_num(num):
        # 将数字转换为字符串
        str_num = str(num)
        # 如果没有小数点，返回0
        if '.' not in str_num:
            return 0
        # 返回小数点后的位数
        return len(str_num.split('.')[1])
    
    # 获取a和b的小数位数
    a_point_num = point_num(a)
    b_point_num = point_num(b)
    
    # 将a和b转换为整数
    a_int = int(a * (10 ** a_point_num))
    b_int = int(b * (10 ** b_point_num))
    
    # 计算结果
    result = a_int / b_int
    
    # 调整小数点位置
    result = result * (10 ** (b_point_num - a_point_num))
    
    # 根据指定的小数位数c进行四舍五入
    result = round(result, c)
    
    return result

while True:
    a = float(input("请输入被除数: "))
    b = float(input("请输入除数: "))
    c = int(input("请输入小数位数: "))
    print(perfect_division(a, b, c))
