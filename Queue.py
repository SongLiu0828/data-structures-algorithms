"""队列先进先出"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items = []
        #查看列表是否为空

    def enqueue(self. item):
        self.items.insert(0, item)
        #将新项添加到队尾

    def dequeue(self):
        return self.items.pop()
        #从队首移除项

    def size(self):
        return len(self.items)
        #返回队列中的项数
