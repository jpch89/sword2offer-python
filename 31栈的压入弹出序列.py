"""
题目：

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如，序列 {1, 2, 3, 4, 5} 是某栈的压入序列，序列 {4, 5, 3, 2, 1} 是该压栈序列对应的一个弹出序列，但 {4, 3, 5, 1, 2} 就不可能是该压栈序列的弹出序列。

牛客网题目描述：
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""


# 使用辅助栈，模拟过程
def is_pop_order(push_order, pop_order):
    stack = []
    index = 0
    length = len(pop_order)
    for i in push_order:
        stack.append(i)
        while stack[-1] == pop_order[index]:
            stack.pop()
            index += 1
            if index == length:
                return True
                # break
    return False
    # return True if index == length else False
    # return True if not stack else False


if __name__ == '__main__':
    push_order = [1, 2, 3, 4, 5]
    pop_order1 = [4, 5, 3, 2, 1]
    pop_order2 = [4, 3, 5, 1, 2]
    pop_order3 = [7, 8, 9, 10, 11]
    print(is_pop_order(push_order, pop_order1))
    print(is_pop_order(push_order, pop_order2))
    print(is_pop_order(push_order, pop_order3))

"""
True
False
False
"""
