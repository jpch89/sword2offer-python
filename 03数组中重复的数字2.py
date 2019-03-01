"""
题目二：不修改数组找出重复的数字。

在一个长度为 n+1 的数组里的所有数字都在 1-n 的范围内，所以数组中至少有一个数字是重复的。
请找出数组中任意一个重复的数字，但不能修改输入的数组。
例如，如果输入长度为 8 的数组 {2, 3, 5, 4, 3, 2, 6, 7}，那么对应的输出是重复的数字 2 或者 3。
"""


# 解法一：使用辅助数组
# 需要 O(n) 的空间
def find_repeat1(arr):
    arr2 = [0] * len(arr)
    for i in arr:
        if arr2[i] == 0:
            arr2[i] += 1
        else:
            return i


# 解法二：二分统计
# 时间复杂度：O(nlogn)
# 空间复杂度：O(1)
def find_repeat2(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2

        # 统计出现次数
        cnt = 0
        for i in arr:
            if start + 1 <= i <= mid + 1:
                cnt += 1

        # 重复的数字在左边
        if cnt > mid + 1:
            end = mid
        # 重复的数字在右边
        else:
            start = mid + 1  # 注意这里很重要！
    return start


# 解法三：append + in
# 略


if __name__ == '__main__':
    arr = [2, 3, 5, 4, 3, 2, 6, 7]
    print(arr)
    print(f'解法一：{find_repeat1(arr)}')
    print(f'解法二：{find_repeat2(arr)}')

"""
[2, 3, 5, 4, 3, 2, 6, 7]
解法一：3
解法二：3
"""
