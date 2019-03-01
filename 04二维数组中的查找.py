"""
题目：
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


# 解法一：书上的解法。
# 取右上角元素：
# 1. 等于要找的数，返回 true
# 2. 大于要找的数，列游标左移，缩小查找范围
# 3. 小于要找的数，行游标下移，缩小查找范围
def find_number1(matrix, rows, cols, num):
    """
    rows: 总行数
    cols: 总列数
    """
    # 行游标
    row = 0
    # 列游标
    col = cols - 1
    while col >= 0 and row <= rows - 1:
        top_right = matrix[row * cols + col]
        if top_right == num:
            return True
        elif top_right > num:
            col -= 1
        else:
            row += 1
    else:
        return False


# 解法二：自己的解法。
# 1. 搜索行，直到找到大于要找的数或到边界。
# 2. 搜索列，同上。
# 3. 缩小行、列查找范围。
# 4. 从 (行+1) 和 (列+1) 继续搜索。
def find_number2(matrix, rows, cols, num):
    # 定义行、列开始游标
    r_start = c_start = 0
    # 行结束游标
    r_end = rows - 1
    # 列结束游标
    c_end = cols - 1

    while r_start <= r_end and c_start <= c_end:
        for i in range(r_start, r_end + 1):
            # 计算每行元素
            r_elem = matrix[i * cols + c_start]
            if r_elem == num:
                return True
            elif r_elem < num:
                continue
            else:
                r_end = i - 1
                break
        for i in range(c_start, c_end + 1):
            # 计算每列元素
            c_elem = matrix[r_start * cols + i]
            if c_elem == num:
                return True
            elif c_elem < num:
                continue
            else:
                c_end = i - 1
                break
        r_start += 1
        c_start += 1
    else:
        return False


if __name__ == '__main__':
    matrix = [1, 2, 8, 9, 2, 4, 9, 12, 4, 7, 10, 13, 6, 8, 11, 15]
    num = 7
    print(f'二维矩阵为：{matrix}')
    print(f'要找的数为：{num}')
    print(f'解法一：{find_number1(matrix, 4, 4, num)}')
    print(f'解法二：{find_number2(matrix, 4, 4, num)}')

"""
二维矩阵为：[1, 2, 8, 9, 2, 4, 9, 12, 4, 7, 10, 13, 6, 8, 11, 15]
要找的数为：7
解法一：True
解法二：True
"""
