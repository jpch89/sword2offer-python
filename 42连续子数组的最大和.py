"""
题目：

输入一个整型数组，数组里有正数也有负数。
数组中的一个或连续多个整数组成一个子数组。
求所有子数组的和的最大值。
要求时间复杂度为 O(n)。

例如，输入的数组为 {1, -2, 3, 10, -4, 7, 2, -5}，
和的最大子数组为 {3, 10, -4, 7, 2}，
因此输出为该子数组的和 18。

牛客网举例：
例如，{6, -3, -2, 7, -15, 1, 2, 2}，
连续子数组的最大和为 8。
"""


# 用 while 循环
def find_greatest_sum_of_subarray1(array):
    max_sum = None
    length = len(array)
    index = 0

    if length == 0:
        return max_sum

    while index != length:
        if index == 0:
            temp_sum = max_sum = array[0]
            index += 1
            continue

        temp_sum += array[index]
        if temp_sum < array[index]:
            temp_sum = array[index]

        if temp_sum > max_sum:
            max_sum = temp_sum

        index += 1

    return max_sum


# 用 for 循环
def find_greatest_sum_of_subarray2(array):
    if not array:
        return

    max_sum = None

    for i in array:
        if max_sum is None:
            max_sum = tmp_sum = i
            continue

        if tmp_sum + i < i:
            tmp_sum = i
        else:
            tmp_sum += i

        if max_sum < tmp_sum:
            max_sum = tmp_sum

    return max_sum



if __name__ == '__main__':
    array1 = [1, -2, 3, 10, -4, 7, 2, -5]
    array2 = [6, -3, -2, 7, -15, 1, 2, 2]
    array3 = [2, 4, 7, 8, 1]
    array4 = [-1, -4, -5, -7, -3]

    print(find_greatest_sum_of_subarray1(array1))
    print(find_greatest_sum_of_subarray1(array2))
    print(find_greatest_sum_of_subarray1(array3))
    print(find_greatest_sum_of_subarray1(array4))

    print()
    print(find_greatest_sum_of_subarray2(array1))
    print(find_greatest_sum_of_subarray2(array2))
    print(find_greatest_sum_of_subarray2(array3))
    print(find_greatest_sum_of_subarray2(array4))

"""
18
8
22
-1

18
8
22
-1
"""
