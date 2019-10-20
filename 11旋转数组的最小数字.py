"""
题目：

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 {3, 4, 5, 1, 2} 为 {1, 2, 3, 4, 5} 的一个旋转，该数组的最小值为 1。
"""


# 解法一：遍历找最小值
# 时间复杂度：O(n)
def findmin(arr):
    min_num = arr[0]
    for i in arr:
        if i < min_num:
            min_num = i
    return min_num


# 解法二：二分查找
# 时间复杂度：O(logn)
def findmin_bisect(arr):
    # 只旋转了 0 个元素的数组
    if arr[0] < arr[-1]:
        return arr[0]

    # 无法判定最小元素位置的数组
    p1 = 0
    p2 = len(arr) - 1
    mid = (p1 + p2) // 2
    if arr[p1] == arr[p2] == arr[mid]:
        return min(arr)

    while p2 - p1 > 1:
        if arr[mid] >= arr[p1]:
            p1 = mid
        else:
            p2 = mid
        mid = (p1 + p2) // 2
    return arr[p2]


# 解法三：先去重，再二分
def findmin_bisect2(arr):
    length = len(arr)
    left = 0
    right = length - 1

    # 根本没有旋转的数组（旋转了 0 项）
    if arr[0] < arr[-1]:
        return arr[0]

    # 数组长度大于 1 时，才有必要去重
    if length > 1:
        # 左去重
        while left + 1 < length and arr[left] == arr[left + 1]:
            left += 1
        # 右去重
        while right - 1 >= 0 and arr[right] == arr[right - 1]:
            right -= 1

    # 二分查找
    while right - left > 1:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid
        else:
            right = mid

    return arr[right]


if __name__ == '__main__':
    print(findmin([3, 4, 5, 1, 2]))
    print(findmin([1, 2, 3, 4, 5]))
    print(findmin([1, 1, 1, 1, 1]))
    print(findmin([1]))
    print(findmin([1, 0, 1, 1, 1]))
    print(findmin([1, 1, 1, 0, 1]))
    print(findmin([5, 5, 5, 3, 4, 5]))

    print()
    print(findmin_bisect([3, 4, 5, 1, 2]))
    print(findmin_bisect([1, 2, 3, 4, 5]))
    print(findmin_bisect([1, 1, 1, 1, 1]))
    print(findmin_bisect([1]))
    print(findmin_bisect([1, 0, 1, 1, 1]))
    print(findmin_bisect([1, 1, 1, 0, 1]))
    print(findmin_bisect([5, 5, 5, 3, 4, 5]))

    print()
    print(findmin_bisect2([3, 4, 5, 1, 2]))
    print(findmin_bisect2([1, 2, 3, 4, 5]))
    print(findmin_bisect2([1, 1, 1, 1, 1]))
    print(findmin_bisect2([1]))
    print(findmin_bisect2([1, 0, 1, 1, 1]))
    print(findmin_bisect2([1, 1, 1, 0, 1]))
    print(findmin_bisect2([5, 5, 5, 3, 4, 5]))

"""
1
1
1
1
0
0
3

1
1
1
1
0
0
3

1
1
1
1
0
0
3
"""
