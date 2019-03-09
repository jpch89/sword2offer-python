"""
题目：

用两个队列实现栈。
"""


class Queue:
    def __init__(self):
        self.q = []

    def __len__(self):
        return len(self.q)

    def inqueue(self, data):
        '入队，列表末尾为队尾'
        self.q.append(data)

    def dequeque(self):
        '出队，列表头部为队头'
        return self.q.pop(0)


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, data):
        """
        如果 q1 为空，直接调用 q1 的 inqueue 方法
        如果 q1 不为空，把 q1 所有的元素出队，入队到 q2
        把要插入的 data 入队 q1
        最后把 q2 的元素入队到 q1
        """
        if self.q1:
            while self.q1:
                self.q2.inqueue(self.q1.dequeque())
            self.q1.inqueue(data)
            while self.q2:
                self.q1.inqueue(self.q2.dequeque())
        else:
            self.q1.inqueue(data)

    def pop(self):
        return self.q1.dequeque()


if __name__ == '__main__':
    s = Stack()
    s.push('a')
    s.push('b')
    s.push('c')
    print(s.pop())
    print(s.pop())
    s.push('d')
    print(s.pop())
    print(s.pop())
