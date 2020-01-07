"""
题目：

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

链表节点定义如下：
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

团子注：本题写了两种解法，都已经测试通过！
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 方法一：依次取出头节点
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        
        head = pHead1 if pHead1.val < pHead2.val else pHead2
        p = head
        p1 = pHead1
        p2 = pHead2
        if p is p1:
            p1 = p1.next
        else:
            p2 = p2.next
        
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        
        if p1 is None:
            p.next = p2
        else:
            p.next = p1

        return head
    
    # 方法二：递归
    def Merge2(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        
        head = pHead1 if pHead1.val < pHead2.val else pHead2
        if head is pHead1:
            head.next = self.Merge2(pHead1.next, pHead2)
        else:
            head.next = self.Merge2(pHead1, pHead2.next)
        
        return head


if __name__ == "__main__":
    # 构造节点
    li = []
    for i in range(10):
        li.append(ListNode(i + 1))
    li1 = []
    li2 = []
    # 构造链表 {1, 3, 5, 7, 9} 和 {2, 4, 6, 8, 10}
    for i in range(10):
        li1.append(li[i]) if not i % 2 else li2.append(li[i])
    for i in range(8):
        li[i].next = li[i + 2]
    # 链表头节点
    head1 = li1[0]
    head2 = li2[0]
    # 输出原始链表
    print('链表 1 为：')
    p = head1
    while p.next is not None:
        print(p.val, end=', ')
        p = p.next
    print(p.val)
    print('链表 2 为：')
    p = head2
    while p.next is not None:
        print(p.val, end=', ')
        p = p.next
    print(p.val)
    # 输出合并后链表
    p = Solution().Merge2(head1, head2)
    print('合并后链表为：')
    while p.next is not None:
        print(p.val, end=', ')
        p = p.next
    print(p.val)

    print('=' * 30)

    # 构造链表 {1, 2, 2, 3} 和 {1, 2, 2, 3}
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(2)
    n4 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    head1 = n1
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(2)
    n4 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    head2 = n1
    # 输出原始链表
    print('链表 1 为：')
    p = head1
    while p.next is not None:
        print(p.val, end=', ')
        p = p.next
    print(p.val)
    print('链表 2 为：')
    p = head2
    while p.next is not None:
        print(p.val, end=', ')
        p = p.next
    print(p.val)
    # 输出合并后链表
    p = Solution().Merge2(head1, head2)
    print('合并后链表为：')
    while p.next is not None:
        print(p.val, end=', ')
        p = p.next
    print(p.val)

"""
链表 1 为：
1, 3, 5, 7, 9
链表 2 为：
2, 4, 6, 8, 10
合并后链表为：
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
==============================
链表 1 为：
1, 2, 2, 3
链表 2 为：
1, 2, 2, 3
合并后链表为：
1, 1, 2, 2, 2, 2, 3, 3
"""
