"""
题目：

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数。
在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
"""


class MinStack:
    def __init__(self):
        self.data_stack = []
        self.min_stack = []

    def push(self, val):
        self.data_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if self.data_stack:
            self.min_stack.pop()
            return self.data_stack.pop()

    def top(self):
        if self.data_stack:
            return self.data_stack[-1]

    def min(self):
        if self.min_stack:
            return self.min_stack[-1]


if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(3)
    print('push 3')
    print('min', min_stack.min())
    print('top', min_stack.top())
    print()

    min_stack.push(4)
    print('push 4')
    print('min', min_stack.min())
    print('top', min_stack.top())
    print()

    min_stack.push(2)
    print('push 2')
    print('min', min_stack.min())
    print('top', min_stack.top())
    print()

    min_stack.push(1)
    print('push 1')
    print('min', min_stack.min())
    print('top', min_stack.top())
    print()

    print('pop', min_stack.pop())
    print('min', min_stack.min())
    print('top', min_stack.top())
    print()

    print('pop', min_stack.pop())
    print('min', min_stack.min())
    print('top', min_stack.top())
    print()

    min_stack.push(0)
    print('push 0')
    print('min', min_stack.min())
    print('top', min_stack.top())
    print()


"""
push 3
min 3
top 3

push 4
min 3
top 4

push 2
min 2
top 2

push 1
min 1
top 1

pop 1
min 2
top 2

pop 2
min 3
top 4

push 0
min 0
top 0
"""
