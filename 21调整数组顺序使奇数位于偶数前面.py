"""
题目：
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

牛客网题目描述：
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""

# 解法一：使用一个辅助数组，遍历两次
# 时间复杂度：O(n)
# 空间复杂度：O(n)
def reorder_array1(array):
    res = []

    for i in array:
        if i % 2 == 1:
            res.append(i)

    for i in array:
        if i % 2 == 0:
            res.append(i)

    return res

# 解法二：使用两个辅助数组，遍历一次
def reorder_array2(array):
    odd, even = [], []
    for i in array:
        odd.append(i) if i % 2 == 1 else even.append(i)
    return odd + even

# 解法三：列表解析式一行解
def reorder_array3(array):
    return [i for i in array if i % 2 == 1] + [i for i in array if i % 2 == 0]

# 解法四：lambda 表达式一行解
def reorder_array4(array):
    return sorted(array, key=lambda x: x % 2, reverse=True)

# 解法五：使用头尾指针，前偶后奇则交换顺序，直到头尾指针重叠或越过
# 注意：这种方法没有稳定性！
def reorder_array5(array):
    p_head = 0
    p_tail = len(array) - 1
    while p_head < p_tail:
        # p_head 找偶数
        while array[p_head] % 2:
            p_head += 1
            if p_head >= len(array):
                break
        # p_tail 找奇数
        while array[p_tail] % 2 == 0:
            p_tail -= 1
            if p_tail < 0:
                break
        # 交换
        if p_head < p_tail:
            array[p_head], array[p_tail] = array[p_tail], array[p_head]
            p_head += 1
            p_tail -= 1
    return array


if __name__ == '__main__':
    print(reorder_array1([1, 2, 3, 4, 5]))
    print(reorder_array1([2, 4, 5, 6, 8]))
    print(reorder_array1([2, 4, 6, 1, 3, 5]))
    print(reorder_array1([1, 3, 5, 2, 4, 6]))
    print(reorder_array1([1, 3, 5, 9, 7]))
    print(reorder_array1([2]))
    print()
    print(reorder_array2([1, 2, 3, 4, 5]))
    print(reorder_array2([2, 4, 5, 6, 8]))
    print(reorder_array2([2, 4, 6, 1, 3, 5]))
    print(reorder_array2([1, 3, 5, 2, 4, 6]))
    print(reorder_array2([1, 3, 5, 9, 7]))
    print(reorder_array2([2]))
    print()
    print(reorder_array3([1, 2, 3, 4, 5]))
    print(reorder_array3([2, 4, 5, 6, 8]))
    print(reorder_array3([2, 4, 6, 1, 3, 5]))
    print(reorder_array3([1, 3, 5, 2, 4, 6]))
    print(reorder_array3([1, 3, 5, 9, 7]))
    print(reorder_array3([2]))
    print()
    print(reorder_array4([1, 2, 3, 4, 5]))
    print(reorder_array4([2, 4, 5, 6, 8]))
    print(reorder_array4([2, 4, 6, 1, 3, 5]))
    print(reorder_array4([1, 3, 5, 2, 4, 6]))
    print(reorder_array4([1, 3, 5, 9, 7]))
    print(reorder_array4([2]))
    print()
    print(reorder_array5([1, 2, 3, 4, 5]))
    print(reorder_array5([2, 4, 5, 6, 8]))
    print(reorder_array5([2, 4, 6, 1, 3, 5]))
    print(reorder_array5([1, 3, 5, 2, 4, 6]))
    print(reorder_array5([1, 3, 5, 9, 7]))
    print(reorder_array5([2]))
    print()

"""
[1, 3, 5, 2, 4]
[5, 2, 4, 6, 8]
[1, 3, 5, 2, 4, 6]
[1, 3, 5, 2, 4, 6]
[1, 3, 5, 9, 7]
[2]

[1, 3, 5, 2, 4]
[5, 2, 4, 6, 8]
[1, 3, 5, 2, 4, 6]
[1, 3, 5, 2, 4, 6]
[1, 3, 5, 9, 7]
[2]

[1, 3, 5, 2, 4]
[5, 2, 4, 6, 8]
[1, 3, 5, 2, 4, 6]
[1, 3, 5, 2, 4, 6]
[1, 3, 5, 9, 7]
[2]

[1, 3, 5, 2, 4]
[5, 2, 4, 6, 8]
[1, 3, 5, 2, 4, 6]
[1, 3, 5, 2, 4, 6]
[1, 3, 5, 9, 7]
[2]

[1, 5, 3, 4, 2]
[5, 4, 2, 6, 8]
[5, 3, 1, 6, 4, 2]
[1, 3, 5, 2, 4, 6]
[1, 3, 5, 9, 7]
[2]
"""
