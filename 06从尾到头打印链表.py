"""
题目：

输入一个链表的头节点，从尾到头反过来打印出每个节点的值。
"""

# 定义节点
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# 解法一：使用栈结构
def reverse_print1(node):
    stack = []
    while node.next:
        stack.append(node.value)
        node = node.next
    stack.append(node.value)
    while stack:
        print(stack.pop(), end=' ')
    print()



# 解法二：使用递归（递归本质上就是栈结构）
def reverse_print2(node):
    if node.next is not None:
        reverse_print2(node.next)
    print(node.value, end=' ')


if __name__ == '__main__':
    # 1. 创建链表
    linkedlist = [Node(i) for i in range(5)]
    for i in range(4):
        linkedlist[i].next = linkedlist[i + 1]
    linkedlist = linkedlist[0]

    # 2. 测试结果
    reverse_print1(linkedlist)
    reverse_print2(linkedlist)

"""
4 3 2 1 0
4 3 2 1 0
"""
