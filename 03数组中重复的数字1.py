"""
题目一：找出数组中重复的数字。

在一个长度为 n 的数组里的所有数字都在 0 到 n - 1 的范围内。数组中某些数字是重复的，但不知道有几个数字是重复的，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为 7 的数组 {2, 3, 1, 0, 2, 5, 3}，那么对应的输出是重复的数字 2 或者 3。
"""

# 解法一：排序 + 判断
# 时间复杂度：O(nlogn)
# 略


# 解法二：哈希表
# 时间复杂度：O(n)
# 空间复杂度：O(n)
def find_repeat2(array):
    my_dict = {}
    for i in array:
        if i in my_dict:
            return i
        else:
            my_dict[i] = 1


# 解法三：交换到正确位置
def find_repeat3(array):
    i = 0
    while i < len(array):
        m = array[i]
        if m == i:
            i += 1
            continue
        else:
            if m == array[m]:
                return m
            else:
                array[i], array[m] = array[m], array[i]


if __name__ == '__main__':
    array = [2, 3, 1, 0, 2, 5, 3]
    print(array)
    print(f'解法二：{find_repeat2(array)}')
    print(f'解法三：{find_repeat3(array)}')

    print()
    array = [0, 1, 2, 3, 4, 5]
    print(array)
    print(f'解法二：{find_repeat2(array)}')
    print(f'解法三：{find_repeat3(array)}')

"""
[2, 3, 1, 0, 2, 5, 3]
解法二：2
解法三：2

[0, 1, 2, 3, 4, 5]
解法二：None
解法三：None
"""
