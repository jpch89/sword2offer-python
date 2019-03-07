"""
题目

用两个栈实现一个队列。
队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead，
分别完成在队列尾部插入节点和在队列头部删除节点的功能。
"""


class Stack:
    def __init__(self, *args):
        self.stack = list(args)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def __len__(self):  # 支持 bool 类型
        return len(self.stack)

    def __repr__(self):
        return "stack: " + str(self.stack)


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def appendTail(self, item):
        self.stack1.push(item)

    def deleteHead(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            item = self.stack1.pop()
            self.stack2.push(item)
        else:
            return self.stack2.pop()


if __name__ == '__main__':
    q = Queue()
    q.appendTail('a')
    q.appendTail('b')
    q.appendTail('c')
    print(q.deleteHead())
    print(q.deleteHead())
    q.appendTail('d')
    print(q.deleteHead())
    print(q.deleteHead())

"""
a
b
c
d
"""
