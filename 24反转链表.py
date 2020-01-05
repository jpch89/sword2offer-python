"""
题目：

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
链表节点定义如下：

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # 没有节点或者只有一个节点
        if pHead is None or pHead.next is None:
            return pHead

        pCurrent = pHead
        pNext = pCurrent.next
        pHead.next = None

        while pNext is not None:
            temp = pNext.next
            pNext.next = pCurrent
            pCurrent = pNext
            pNext = temp

        return pCurrent


if __name__ == "__main__":
    # 构造链表
    nodes = []
    for i in range(5):
        nodes.append(ListNode(i + 1))
    for i in range(4):
        nodes[i].next = nodes[i + 1]
    pHead = nodes[0]

    # 输出原始链表
    p = pHead
    print('原始链表为：')
    while p.next is not None:
        print(p.val, end=',')
        p = p.next
    print(p.val)

    # 反转链表
    p = Solution().ReverseList(pHead)
    print('链表反转后：')
    while p.next is not None:
        print(p.val, end=',')
        p = p.next
    print(p.val)

"""
原始链表为：
1,2,3,4,5
链表反转后：
5,4,3,2,1
"""
