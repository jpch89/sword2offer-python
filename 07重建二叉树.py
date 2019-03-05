"""
题目：

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如，输入前序遍历序列 {1, 2, 4, 7, 3, 5, 6, 8}
和中序遍历序列 {4, 7 ,2, 1, 5, 3, 8, 6}，
则重建如图 2.6 所示的二叉树并输出它的头节点。

        1
      /   \
     2    3
    /    / \
   4    5  6
    \     /
    7    8
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None


def construct_root(preorder, prestart, preend, inorder, instart, inend):
    root = Node(preorder[prestart])

    # 只有一个节点：叶子结点
    if prestart == preend and instart == inend and preorder[prestart] == inorder[instart]:
        print('找到叶子节点，值为{}，先序遍历下标为{}'.format(root.value, prestart))
        return root

    # i 存放的是中序根节点的下标
    # 因为数字不重复，下面的循环可以用一句话代替
    # 不过用循环效率高一点
    # i = inorder.index(root.value)
    for i in range(instart, inend + 1):
        if root.value == inorder[i]:
            break
    else:
        print('出现异常，没有找到中序根节点')

    # 处理左子树
    left_len = i - instart
    left_prestart = prestart + 1
    left_preend = left_prestart + left_len - 1
    left_instart = instart
    left_inend = i - 1
    if left_len > 0:
        root.lchild = construct_root(preorder, left_prestart, left_preend, inorder, left_instart, left_inend)

    # 处理右子树
    right_len = inend- i
    right_prestart = left_preend + 1
    right_preend = preend
    right_instart = i + 1
    right_inend = inend
    if right_len > 0:
        root.rchild = construct_root(preorder, right_prestart, right_preend, inorder, right_instart, right_inend)
    return root


def postorder_traverse(root):
    "后序遍历：左 -- 右 -- 根。"
    if root.lchild is not None:
        postorder_traverse(root.lchild)
    if root.rchild is not None:
        postorder_traverse(root.rchild)
    print(root.value)

if __name__ == '__main__':
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7 ,2, 1, 5, 3, 8, 6]
    prestart = instart = 0
    preend = inend = len(preorder) - 1
    root = construct_root(preorder, prestart, preend, inorder, instart, inend)

    print('-' * 20)
    postorder_traverse(root)

"""
找到叶子节点，值为7，先序遍历下标为3
找到叶子节点，值为5，先序遍历下标为5
找到叶子节点，值为8，先序遍历下标为7
--------------------
7
4
2
5
8
6
3
1
"""
