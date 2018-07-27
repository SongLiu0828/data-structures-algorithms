# -*- coding : utf-8 -*-
"""后进先出，类似于盘子"""

class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
        #判断是否为空

    def push(self, item):
        self.items.append(item)
        #添加一个新的元item到栈顶

    def pop(self):
        return self.items.pop()
        #从栈中删除顶部项

    def peek(self):
        return self.items[len(self.items)-1]
        #从栈返回顶部项

    def size(self):
        return len(self.items)
        #返回栈中的item数量

s = Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
