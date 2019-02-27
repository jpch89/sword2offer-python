"""
题目：设计一个类，我们只能生成该类的一个实例。
"""

class Singleton:
    __instance = None
    __init = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        if self.__class__.__init:
            return
        print('-----开始初始化-----')
        print(args)
        print(kwargs)
        print('-----结束初始化-----')
        self.__class__.__init = True

if __name__ == '__main__':
    singleton1 = Singleton(1, a=2, b=3)
    singleton2 = Singleton(2, a=3, b=4)
    singleton3 = Singleton(3, a=4, b=5)
    conditions = [singleton1 is singleton2, singleton2 is singleton3]
    print()
    print('是否为单例：', all(conditions))

"""
-----开始初始化-----
(1,)
{'a': 2, 'b': 3}
-----结束初始化-----

是否为单例： True
"""
