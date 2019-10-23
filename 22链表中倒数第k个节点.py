"""
题目：

输入一个链表，输出该链表中倒数第 k 个节点。
为了符合大多数人的习惯，本题从 1 开始计数，即链表的尾节点是倒数第 1 个节点。
例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。
这个链表的倒数第 3 个节点是值为 4 的节点。

举一反三：
当我们用一个指针遍历链表不能解决问题的时候，可以尝试用两个指针来遍历链表。
可以让其中一个指针遍历的速度快一些（比如一次在链表上走两步），
或者让它先在链表上走若干步。
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f'node({self.val})'


# 解法一：使用辅助空间
def find_kth_to_tail1(list_head, k):
    if list_head is None:
        return None
    if k <= 0:
        return None

    temp = []

    while list_head:
        temp.append(list_head)
        list_head = list_head.next

    if k > len(temp):
        return None
    else:
        return temp[-k]


# 解法二：使用单指针，进行两次遍历
def find_kth_to_tail2(list_head, k):
    if list_head is None:
        return None
    if k <= 0:
        return None

    length = 0
    tmp_list_head = list_head
    while tmp_list_head:
        length += 1
        tmp_list_head = tmp_list_head.next

    if k > length:
        return None

    target = length - k
    index = 0
    while index != target:
        list_head = list_head.next
        index += 1
    return list_head


# 解法三：使用双指针，进行一次遍历
def find_kth_to_tail3(list_head, k):
    if list_head is None:
        return None
    if k <= 0:
        return None

    p_left = p_right = list_head
    # 第一步：p_right 先走 k - 1 步
    for i in range(k - 1):
        p_right = p_right.next
        if p_right is None:
            return None
    # 第二步：p_left 和 p_right 一起走，直到 p_right.next 为 None
    while p_right.next:
        p_right = p_right.next
        p_left = p_left.next
    return p_left


def make_linked_list():
    nodes = [Node(i) for i in range(1, 6)]
    for i in range(len(nodes)):
        if i == len(nodes) - 1:
            break
        nodes[i].next = nodes[i + 1]
    return nodes


if __name__ == '__main__':
    print('=====正常情况1=====')
    linked_list = make_linked_list()
    k = 2
    print(f'链表为：{linked_list}，k为{k}')
    print(find_kth_to_tail1(linked_list[0], k))
    print(find_kth_to_tail2(linked_list[0], k))
    print(find_kth_to_tail3(linked_list[0], k))
    print()

    print('=====正常情况2=====')
    linked_list = make_linked_list()
    k = 5
    print(f'链表为：{linked_list}，k为{k}')
    print(find_kth_to_tail1(linked_list[0], k))
    print(find_kth_to_tail2(linked_list[0], k))
    print(find_kth_to_tail3(linked_list[0], k))
    print()

    print('=====正常情况3=====')
    linked_list = make_linked_list()
    k = 1
    print(f'链表为：{linked_list}，k为{k}')
    print(find_kth_to_tail1(linked_list[0], k))
    print(find_kth_to_tail2(linked_list[0], k))
    print(find_kth_to_tail3(linked_list[0], k))
    print()

    print('=====链表头指针为None=====')
    linked_list = None
    print(find_kth_to_tail1(linked_list, 2))
    print(find_kth_to_tail2(linked_list, 2))
    print(find_kth_to_tail3(linked_list, 2))
    print()

    print('=====k为负数、零、超界=====')
    linked_list = make_linked_list()
    for k in [-5, 0, 99]:
        print(f'k为{k}时：')
        print(find_kth_to_tail1(linked_list[0], k))
        print(find_kth_to_tail2(linked_list[0], k))
        print(find_kth_to_tail3(linked_list[0], k))
        print('-' * 20)
