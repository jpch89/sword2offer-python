"""
题目一：求斐波那契数列的第 n 项。

写一个函数，输入 n，求斐波那契（Fibonacci）数列的第 n 项。
斐波那契数列的定义如下：
        |   0                   n = 0
f(n) = <    1                   n = 1
        \   f(n-1) + f(n-2)     n > 1
"""


# 解法一：递归
def fibo1(n):
    if n <= 1:
        return n
    else:
        return fibo1(n - 1) + fibo1(n - 2)


# 解法二：从前往后算
def fibo2(n):
    if n <= 1:
        return n
    a, b = 0, 1
    i = 1
    while i < n:
        a, b = b, a + b
        i += 1
    return b


# 解法三：带矩阵的数学公式
# 略（暂时没看懂）


if __name__ == '__main__':
    print(f'斐波那契数列的第7项为：{fibo1(7)}')
    print(f'斐波那契数列的第7项为：{fibo2(7)}')


"""
斐波那契数列的第7项为：13
斐波那契数列的第7项为：13
"""
