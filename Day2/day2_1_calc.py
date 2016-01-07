# -*- coding:utf-8 -*-
"""
__auther: super
run in python 2.x
"""


# 将传进来的表达式去括号 string为每次处理完后的表达是 source为初始字符串
def get_simple_express(string, source):
    # 是否有括号'('
    if string.count("(") > 0:
        start = string.index("(")
        if string.count(")") > 0:
            end = string.index(")")
        else:
            end = len(string)
        # 截取()之间的表达是，里面可能还有'('
        sub_string = string[start + 1:end]

        # 递归,将截取的表达是再去(,直到找到最近的最小的()
        get_simple_express(sub_string, source)

    # 找到最小的括号了，也就是没有括号了,开始下面的代码准备计算单一表达式
    else:
        min_string = string

        # 将没有括号的表达是交给另一个函数去计算去,返回一个值，返回string类型
        calc_result = calc_string(min_string)

        # 用结果替换掉计算搜索出来的表达式
        substr = "(" + min_string + ")"
        source = source.replace(substr, calc_result)

        # 如果整个表达是都没有括号了，成最后的单一表达式了，也就是最后结果了
        if source.count('(') == 0 and source.count(')') == 0:
            result = calc_string(source)
            print("本程序计算结果为: %s" % result)
        else:
            # 递归,开始新一轮的搜索、计算...
            return get_simple_express(source, source)


def format_str(string):
    string = string.replace('--', '+')
    string = string.replace('-+', '-')
    string = string.replace('+-', '-')
    string = string.replace('++', '+')
    return string


# 计算单一表达式，没有括号滴
def calc_string(string):
    fuhao_list = ('*', '/',)
    check_fuhao = ('*', '/', '+', '-')
    string = str(string)
    print('in_string : ' + string)

    # print('format string :'+ string)
    # 对string中查看有没有*号，先算乘法
    for f in fuhao_list:
        while string.count(f) > 0:
            string = format_str(string)
            position = string.index(f)
            starti = endi = 1
            # 获取符号前后的数字字符
            while position - starti >= 0 and not string[position - starti] in check_fuhao:
                starti += 1

            '''
            # 第一位为负号的情况 -10 + 3 ，多记一位
            if string[0] in check_fuhao and len(re.findall('[^1-9]', string[0:position])) == 1: starti += 1

            # 加号前面的数位负数 5-3+6
            if string[position - starti] == '-':
                string = string[0:position - starti] + '+' + string[position - starti:]
                position += 1
                starti += 1

            while position + endi < len(string) and not string[position + endi] in check_fuhao:
                endi += 1
            '''

            # 挨着符号的右边就是符号，肯定是负数比如：3*-2
            if endi == 1:
                endi += 1
                while position + endi < len(string) and not string[position + endi] in check_fuhao:
                    endi += 1

            x = string[position - starti + 1:position]
            y = string[position + 1:position + endi]

            # 如果是-2+3的情况

            # 获取乘法的两个数字，进行计算，获取结果
            if f == '+': result = str(int(x) + int(y))
            if f == '-': result = str(int(x) - int(y))
            if f == '*': result = str(int(x) * int(y))
            if f == '/': result = str(int(x) / int(y))
            need_replace_string = string[position - starti + 1:position + endi]
            string = string.replace(need_replace_string, result)

        else:  # 第一个运算符找完了
            continue

    # * / 运算符都算完了 就剩下 +- 号了,将-号转换为+-，分隔为列表 再计算
    else:
        string = format_str(string)
        tmpi = 0
        formatstr = string.replace('-','+-')
        liststr = formatstr.split('+')
        for i in liststr:
            if len(i) == 0: i = 0
            tmpi += int(i)
        return str(tmpi)


if __name__ == "__main__":
    a = "9*-3+(-2/1*4/-12+(-8/-2))-(-2*(-5/(-6-8/2)+4)/(5-2+6)*-2)-(4-12*+6/2)"
    #a = '-6-8*-2/-3'
    print('表达式为: %s' % a)
    print("eval函数计算结果为: %s" % eval(a))
    get_simple_express(a, a)

