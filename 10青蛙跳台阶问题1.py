"""
题目二：青蛙跳台阶问题。

一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级台阶。
求该青蛙跳上一个 n 级台阶总共有多少种跳法。
"""


def frog_jump(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return frog_jump(n - 2) + frog_jump(n - 1)


if __name__ == '__main__':
    print(f'跳5级台阶的跳法：{frog_jump(5)}种')

"""
跳5级台阶的跳法：8种
"""
