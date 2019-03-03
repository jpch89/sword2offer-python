"""
题目：

请实现一个函数，把字符串中的每个空格替换成"%20"。
例如，输入 "We are happy."，则输出 "We%20are%20happy."。
"""


# 解法一
# 使用原字符串，从前往后扫描
# 时间复杂度：O(n2)
def replace_space1(strli):
    length = strli.index(None)
    i = 0
    while i < length:
        if strli[i] == ' ':
            end = strli.index(None)  # 找到末尾
            for j in range(end + 2, i + 2, -1):
                strli[j] = strli[j - 2]
            strli[i:i + 3] = '%20'  # 切片赋值
            i += 3
        else:
            i += 1


# 解法二
# 使用原字符串，从后往前扫描
# 时间复杂度：O(n)
def replace_space2(strli):
    space_num = strli.count(' ')
    old_end = strli.index(None) - 1
    new_end = strli.index(None) + space_num * 2 - 1
    while old_end != new_end:
        if strli[old_end] == ' ':
            strli[new_end - 2:new_end + 1] = '%20'  # 切片赋值
            new_end -= 3
            old_end -= 1
        else:
            strli[new_end] = strli[old_end]
            new_end -= 1
            old_end -= 1


# 解法三
# string.replace(' ', '%20')


if __name__ == '__main__':
    string = 'We are happy.'
    strli = list(string) + [None] * 2 * len(string)
    print(f'带转换的字符串列表：{strli}')

    replace_space1(strli)
    print(f'解法一：{strli}')

    print()
    strli = list(string) + [None] * 2 * len(string)
    print(f'带转换的字符串列表：{strli}')
    replace_space2(strli)
    print(f'解法二：{strli}')

"""
待转换的字符串列表：['W', 'e', ' ', 'a', 'r', 'e', ' ', 'h', 'a', 'p', 'p', 'y', '.', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
解法一：['W', 'e', '%', '2', '0', 'a', 'r', 'e', '%', '2', '0', 'h', 'a', 'p', 'p', 'y', '.', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

待转换的字符串列表：['W', 'e', ' ', 'a', 'r', 'e', ' ', 'h', 'a', 'p', 'p', 'y', '.', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
解法二：['W', 'e', '%', '2', '0', 'a', 'r', 'e', '%', '2', '0', 'h', 'a', 'p', 'p', 'y', '.', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
"""
