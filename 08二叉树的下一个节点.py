"""
题目：

给定一颗二叉树和其中的一个节点，如何找出中序遍历序列的下一个节点？
树中的节点除了有两个分别指向左、右子节点的指针，还有一个指向父节点的指针。
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


def isleft(node):
    "判断 node 是不是左子节点。"
    return node.parent.left is node


def isright(node):
    "判断 node 是不是右子节点。"
    return node.parent.right is node


def isroot(node):
    "判断 node 是不是根节点。"
    return node.parent is None


def construct_tree():
    nodes_list = [Node(i) for i in 'abcdefghi']
    nodes_dict = dict(zip('abcdefghi', nodes_list))
    nodes_dict['a'].left = nodes_dict['b']
    nodes_dict['a'].right = nodes_dict['c']
    nodes_dict['b'].left = nodes_dict['d']
    nodes_dict['b'].right = nodes_dict['e']
    nodes_dict['e'].left = nodes_dict['h']
    nodes_dict['e'].right = nodes_dict['i']
    nodes_dict['c'].left = nodes_dict['f']
    nodes_dict['c'].right = nodes_dict['g']
    nodes_dict['b'].parent = nodes_dict['a']
    nodes_dict['d'].parent = nodes_dict['b']
    nodes_dict['e'].parent = nodes_dict['b']
    nodes_dict['h'].parent = nodes_dict['e']
    nodes_dict['i'].parent = nodes_dict['e']
    nodes_dict['c'].parent = nodes_dict['a']
    nodes_dict['f'].parent = nodes_dict['c']
    nodes_dict['g'].parent = nodes_dict['c']
    return nodes_dict


def inorder_traverse(root, li):
    if root.left is not None:
        inorder_traverse(root.left, li)
    li.append(root.value)
    if root.right is not None:
        inorder_traverse(root.right, li)


def next_inorder(node):
    next_node = None
    # 有右子树，返回右子树最左节点
    if node.right:
        next_node = node.right
        while next_node.left:
            next_node = next_node.left
        return next_node.value
    # 没有右子树，且是根节点，返回 None
    if isroot(node):
        return None
    # 没有右子树，如果是左节点，返回父节点
    if isleft(node):
        return node.parent.value
    # 没有右子树，如果是右节点，向上找非右节点的父节点
    if isright(node):
        next_node = node.parent
        while next_node is not None:
            # 如果是根节点，说明 node 是最后一个节点，返回 None
            if isroot(next_node):
                return None
            if isleft(next_node):
                return next_node.parent.value
            next_node = next_node.parent


def test_all_nodes(inorder, nodes):
    for i, node in enumerate(inorder):
        if i == len(inorder) - 1:
            break
        res = next_inorder(nodes[node]) is inorder[i + 1]
        print(f'{node}的下一个是{inorder[i + 1]}：{res}')
    res = next_inorder(nodes[node]) is None
    print(f'{node}的下一个是None：{res}')


if __name__ == '__main__':
    inorder = ['d', 'b', 'h', 'e', 'i', 'a', 'f', 'c', 'g']
    nodes = construct_tree()
    root = nodes['a']
    # 校验是否构建正确
    li = []
    inorder_traverse(root, li)
    print(f'题目顺序：{inorder}')
    print('构建顺序：%s' % li)
    print('是否构建正确：{}'.format(li == inorder))

    print()
    test_all_nodes(inorder, nodes)

"""
题目顺序：['d', 'b', 'h', 'e', 'i', 'a', 'f', 'c', 'g']
构建顺序：['d', 'b', 'h', 'e', 'i', 'a', 'f', 'c', 'g']
是否构建正确：True

d的下一个是b：True
b的下一个是h：True
h的下一个是e：True
e的下一个是i：True
i的下一个是a：True
a的下一个是f：True
f的下一个是c：True
c的下一个是g：True
g的下一个是None：True
"""
